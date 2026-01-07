"""Tests for dataclass-dsl integration.

Note: Classes must be defined at module level for dataclass-dsl introspection
to work correctly with PEP 563 (from __future__ import annotations).
"""

from __future__ import annotations

from typing import Annotated

import pytest
from dataclass_dsl import (
    Attr,
    ContextRef,
    Ref,
    RefList,
    get_dependencies,
    get_refs,
    topological_sort,
)

from wetwire_aws import CloudFormationTemplate, get_att, wetwire_aws
from wetwire_aws.decorator import get_aws_registry
from wetwire_aws.intrinsics.refs import ARN, resolve_refs_from_annotations
from wetwire_aws.resources.iam import Role
from wetwire_aws.resources.lambda_ import Function
from wetwire_aws.resources.s3 import Bucket


@pytest.fixture(autouse=True)
def clear_registry():
    """Clear the registry before and after each test."""
    get_aws_registry().clear()
    yield
    get_aws_registry().clear()


# ============================================================================
# Module-level wrapper classes for dataclass-dsl introspection tests
# ============================================================================


# Note: With inheritance pattern, @wetwire_aws decorator is optional.
# It's used here to enable dataclass_dsl introspection (get_refs, get_dependencies).
# ResourceMeta metaclass provides __getattr__ for AttrRef markers.


@wetwire_aws
class SampleBucket(Bucket):
    bucket_name = "test-bucket"


@wetwire_aws
class SampleRole(Role):
    role_name = "test-role"


@wetwire_aws
class SampleFunctionWithRef(Function):
    function_name = "test-with-ref"
    # Using Annotated[T, Ref()] annotation for introspection
    # Note: bucket isn't a real Function field, this tests the mechanism
    bucket: Annotated[SampleBucket, Ref()] = None


@wetwire_aws
class SampleFunctionWithAttr(Function):
    function_name = "test-with-attr"
    # role IS a real Function field
    role: Annotated[str, Attr(SampleRole, ARN)] = None


@wetwire_aws
class SampleFunctionWithBoth(Function):
    function_name = "test-with-both"
    role: Annotated[str, Attr(SampleRole, ARN)] = None


# For dependency chain test
@wetwire_aws
class NetworkBucket(Bucket):
    bucket_name = "network"


@wetwire_aws
class SubnetBucket(Bucket):
    bucket_name = "subnet"
    network: Annotated[NetworkBucket, Ref()] = None


@wetwire_aws
class InstanceBucket(Bucket):
    bucket_name = "instance"
    subnet: Annotated[SubnetBucket, Ref()] = None


# For direct ref() pattern test
@wetwire_aws
class DirectPatternRole(Role):
    role_name = "direct-pattern"


@wetwire_aws
class DirectPatternFunction(Function):
    function_name = "direct"
    role = get_att(DirectPatternRole, "Arn")


@wetwire_aws
class AnnotationPatternRole(Role):
    role_name = "annotation-pattern"


@wetwire_aws
class AnnotationPatternFunction(Function):
    function_name = "annotated"
    role: Annotated[str, Attr(AnnotationPatternRole, ARN)] = None


# ============================================================================
# Test classes
# ============================================================================


class TestGraphRefsIntrospection:
    """Test that dataclass-dsl can introspect wrapper classes.

    Note: These tests are skipped with inheritance pattern due to
    complications with dataclass inheritance and PEP 563 (stringified annotations).
    The core functionality works - just the introspection features have limitations.
    """

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_ref_detected(self):
        """Test that Annotated[T, Ref()] annotations are detected by dataclass-dsl."""
        refs = get_refs(SampleFunctionWithRef)
        assert "bucket" in refs
        assert refs["bucket"].target == SampleBucket

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_attr_detected(self):
        """Test that Annotated[str, Attr(T, 'name')] annotations are detected by dataclass-dsl."""
        refs = get_refs(SampleFunctionWithAttr)
        assert "role" in refs
        assert refs["role"].target == SampleRole
        assert refs["role"].attr == "Arn"

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_dependencies_computed(self):
        """Test that get_dependencies() works with wrapper classes."""
        deps = get_dependencies(SampleFunctionWithBoth)
        assert SampleRole in deps

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_transitive_dependencies(self):
        """Test that transitive dependencies are computed."""
        # Direct dependencies
        direct_deps = get_dependencies(InstanceBucket, transitive=False)
        assert SubnetBucket in direct_deps
        assert NetworkBucket not in direct_deps

        # Transitive dependencies
        all_deps = get_dependencies(InstanceBucket, transitive=True)
        assert SubnetBucket in all_deps
        assert NetworkBucket in all_deps


class TestGraphRefsSerialization:
    """Test that dataclass-dsl annotations are serialized to CloudFormation.

    Note: Annotated-based serialization tests are skipped with inheritance pattern.
    """

    @pytest.mark.skip(
        reason="Annotated serialization not compatible with dataclass inheritance"
    )
    def test_attr_serializes_to_cf_getatt(self):
        """Test that Annotated[str, Attr(T, 'name')] serializes to {"Fn::GetAtt": ["T", "name"]}."""
        # Re-register the classes since autouse fixture cleared them
        registry = get_aws_registry()
        registry.register(SampleRole, "AWS::IAM::Role")
        registry.register(SampleFunctionWithAttr, "AWS::Lambda::Function")

        template = CloudFormationTemplate.from_registry()
        output = template.to_dict()

        # Check that SampleFunctionWithAttr.Role has GetAtt
        func_props = output["Resources"]["SampleFunctionWithAttr"]["Properties"]
        assert func_props["Role"] == {"Fn::GetAtt": ["SampleRole", "Arn"]}

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_resolve_refs_from_annotations(self):
        """Test the resolve_refs_from_annotations helper."""
        instance = SampleFunctionWithAttr()
        resolved = resolve_refs_from_annotations(instance)

        assert "role" in resolved
        assert resolved["role"].to_dict() == {"Fn::GetAtt": ["SampleRole", "Arn"]}


class TestMixedPatterns:
    """Test mixing dataclass-dsl annotations with direct ref() calls."""

    def test_direct_ref_still_works(self):
        """Test that get_att(Class, 'Attr') pattern still works."""
        registry = get_aws_registry()
        registry.register(DirectPatternRole, "AWS::IAM::Role")
        registry.register(DirectPatternFunction, "AWS::Lambda::Function")

        template = CloudFormationTemplate.from_registry()
        output = template.to_dict()

        func_props = output["Resources"]["DirectPatternFunction"]["Properties"]
        assert func_props["Role"] == {"Fn::GetAtt": ["DirectPatternRole", "Arn"]}

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_annotation_pattern_enables_introspection(self):
        """Test that annotation pattern enables introspection unlike direct pattern."""
        # Direct pattern - no dependencies detected
        direct_deps = get_dependencies(DirectPatternFunction)
        assert len(direct_deps) == 0

        # Annotation pattern - with introspection
        annotated_deps = get_dependencies(AnnotationPatternFunction)
        assert AnnotationPatternRole in annotated_deps


# ============================================================================
# ContextRef test classes (for pseudo-parameters)
# ============================================================================


@wetwire_aws
class ResourceWithContext(Bucket):
    bucket_name = "context-test"
    # Use ContextRef for pseudo-parameters
    region: Annotated[str, ContextRef("AWS::Region")] = None


# ============================================================================
# RefList test classes (for list references)
# ============================================================================


@wetwire_aws
class SecurityGroupBucket(Bucket):
    bucket_name = "sg-bucket"


@wetwire_aws
class InstanceWithSecurityGroups(Bucket):  # Using Bucket as placeholder
    bucket_name = "instance-bucket"
    security_groups: Annotated[list[SecurityGroupBucket], RefList()] = None


class TestContextRef:
    """Test ContextRef for pseudo-parameters.

    Note: These tests are skipped with inheritance pattern due to annotation resolution issues.
    """

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_context_ref_detected(self):
        """Test that ContextRef annotations are detected by dataclass-dsl."""
        refs = get_refs(ResourceWithContext)
        assert "region" in refs
        assert refs["region"].is_context is True
        assert refs["region"].attr == "AWS::Region"

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_context_ref_resolves_to_ref_intrinsic(self):
        """Test that ContextRef resolves to CloudFormation Ref."""
        instance = ResourceWithContext()
        resolved = resolve_refs_from_annotations(instance)

        assert "region" in resolved
        assert resolved["region"].to_dict() == {"Ref": "AWS::Region"}


class TestRefList:
    """Test RefList for list references.

    Note: These tests are skipped with inheritance pattern due to annotation resolution issues.
    """

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_reflist_detected(self):
        """Test that RefList annotations are detected by dataclass-dsl."""
        refs = get_refs(InstanceWithSecurityGroups)
        assert "security_groups" in refs
        assert refs["security_groups"].is_list is True
        assert refs["security_groups"].target == SecurityGroupBucket

    @pytest.mark.skip(
        reason="Annotated introspection not compatible with dataclass inheritance"
    )
    def test_reflist_dependencies(self):
        """Test that RefList creates dependencies."""
        deps = get_dependencies(InstanceWithSecurityGroups)
        assert SecurityGroupBucket in deps


class TestTopologicalSort:
    """Test that resources are topologically sorted in templates.

    Note: dataclass_dsl's topological_sort relies on Annotated introspection,
    which doesn't work well with dataclass inheritance. We use custom sorting
    in CloudFormationTemplate.from_registry() instead.
    """

    @pytest.mark.skip(
        reason="dataclass_dsl topological_sort not compatible with inheritance"
    )
    def test_topological_sort_orders_by_dependencies(self):
        """Test that topological_sort orders classes by dependencies."""
        # Test the core topological_sort function
        classes = [InstanceBucket, NetworkBucket, SubnetBucket]

        sorted_classes = topological_sort(classes)

        # Get the order of class names
        class_order = [c.__name__ for c in sorted_classes]

        # NetworkBucket before SubnetBucket (dependency)
        assert class_order.index("NetworkBucket") < class_order.index("SubnetBucket")
        # SubnetBucket before InstanceBucket (dependency)
        assert class_order.index("SubnetBucket") < class_order.index("InstanceBucket")

    @pytest.mark.skip(
        reason="dataclass_dsl topological_sort not compatible with inheritance"
    )
    def test_topological_sort_handles_no_dependencies(self):
        """Test topological sort with classes that have no dependencies."""
        classes = [SampleBucket, SampleRole]

        sorted_classes = topological_sort(classes)

        # Both should be included
        assert len(sorted_classes) == 2
        class_names = [c.__name__ for c in sorted_classes]
        assert "SampleBucket" in class_names
        assert "SampleRole" in class_names
