"""
Test cross-file references with `from . import *` pattern.

This tests the CRITICAL feature that users can:
1. Define resources in separate files
2. Use `from . import *` in __init__.py
3. Have cross-file references resolve correctly

This is the recommended user pattern and MUST work.
"""

from __future__ import annotations

import pytest
from dataclass_dsl import is_attr_ref

from wetwire_aws import CloudFormationTemplate
from wetwire_aws.decorator import get_aws_registry


@pytest.fixture(autouse=True)
def clear_registry():
    """Clear the registry before and after each test."""
    get_aws_registry().clear()
    yield
    get_aws_registry().clear()


class TestCrossFileReferences:
    """Test that resources defined in separate files can reference each other."""

    def test_cross_file_import_star_pattern(self):
        """
        Test that `from . import *` pattern works for cross-file references.

        This simulates a user project structure:
        - resources/__init__.py: `from . import *`
        - resources/role.py: defines AppRole
        - resources/function.py: defines AppFunction with role = AppRole.Arn
        """
        # Import the test package - this uses `from . import *` pattern
        from tests.cross_file_test import AppFunction, AppRole

        # Verify both classes are imported
        assert AppRole is not None
        assert AppFunction is not None

        # Verify the no-parens cross-file reference is detected
        # With inheritance pattern, the value is a class attribute
        role_value = getattr(AppFunction, "role", None)
        assert is_attr_ref(role_value), "role should be an AttrRef (no-parens pattern)"
        assert role_value.target.__name__ == "AppRole", "AttrRef should reference AppRole"
        assert role_value.attr == "Arn", "AttrRef should reference 'Arn' attribute"

    def test_cross_file_serialization(self):
        """Test that cross-file references serialize correctly to CloudFormation."""
        # Import via the package
        from tests.cross_file_test import AppFunction, AppRole

        # Re-register after fixture cleared them
        registry = get_aws_registry()
        registry.register(AppRole, "AWS::IAM::Role")
        registry.register(AppFunction, "AWS::Lambda::Function")

        # Generate template
        template = CloudFormationTemplate.from_registry()
        output = template.to_dict()

        # Verify resources are in the template
        assert "AppRole" in output["Resources"]
        assert "AppFunction" in output["Resources"]

        # Verify the cross-file reference is serialized correctly
        # The no-parens pattern (role = AppRole.Arn) should serialize to GetAtt
        func_props = output["Resources"]["AppFunction"]["Properties"]
        assert func_props["Role"] == {"Fn::GetAtt": ["AppRole", "Arn"]}, (
            "Cross-file no-parens reference (AppRole.Arn) should serialize to GetAtt"
        )

    def test_cross_file_dependency_order(self):
        """Test that cross-file dependencies are ordered correctly.

        NOTE: This test verifies that the topological sort works correctly.
        Due to a known issue with dataclass-dsl's decorator pattern (see #10),
        the AttrRef.target points to the pre-decorated class while imports
        return the decorated class. The topological sort in template.py
        works around this by comparing class names instead of identity.
        """
        from tests.cross_file_test import AppFunction, AppRole

        # Re-register (fixture may have cleared registry, but import re-populates)
        registry = get_aws_registry()

        # Ensure both classes are registered
        if "AppRole" not in registry:
            registry.register(AppRole, "AWS::IAM::Role")
        if "AppFunction" not in registry:
            registry.register(AppFunction, "AWS::Lambda::Function")

        # Debug: Check if role attribute is detected as AttrRef
        role_attr = getattr(AppFunction, "role", None)
        assert is_attr_ref(role_attr), (
            f"AppFunction.role should be AttrRef, got: {type(role_attr).__name__}"
        )
        # Compare by name, not identity (due to decorator creating new class)
        assert role_attr.target.__name__ == "AppRole", (
            f"AttrRef target should be AppRole class, got: {role_attr.target.__name__}"
        )

        # Generate template
        template = CloudFormationTemplate.from_registry()
        output = template.to_dict()

        # Get resource order
        resource_names = list(output["Resources"].keys())

        # AppRole should come before AppFunction (dependency order)
        role_idx = resource_names.index("AppRole")
        func_idx = resource_names.index("AppFunction")
        assert role_idx < func_idx, (
            f"AppRole (idx={role_idx}) should appear before AppFunction (idx={func_idx}). "
            f"Template resource order: {resource_names}"
        )
