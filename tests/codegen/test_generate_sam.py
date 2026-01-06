"""Tests for SAM resource generation in codegen/generate.py."""

from codegen.generate import (
    CF_TO_BOTOCORE_SERVICE,
    generate_service_package,
    load_enums_for_service,
)
from codegen.parse import parse_sam_resources


class TestServerlessServiceMapping:
    """Tests for serverless service mapping."""

    def test_serverless_in_botocore_mapping(self):
        """Serverless should be in CF_TO_BOTOCORE_SERVICE."""
        # serverless maps to None since it's not a botocore service
        assert "serverless" in CF_TO_BOTOCORE_SERVICE

    def test_serverless_maps_to_none(self):
        """Serverless should map to None (no botocore equivalent)."""
        assert CF_TO_BOTOCORE_SERVICE["serverless"] is None


class TestLoadEnumsForServerless:
    """Tests for loading enums for serverless service."""

    def test_returns_empty_dict_by_default(self):
        """load_enums_for_service should return empty dict for serverless."""
        # Serverless has no botocore enums by default
        result = load_enums_for_service("serverless")
        assert isinstance(result, dict)


class TestGenerateServerlessPackage:
    """Tests for generating serverless package."""

    def test_generates_package_files(self):
        """Should generate package files for serverless."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        assert isinstance(files, dict)
        assert len(files) > 0

    def test_generates_init_file(self):
        """Should generate __init__.py file."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        assert "serverless/__init__.py" in files

    def test_init_has_function_class(self):
        """__init__.py should contain Function class."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        init_content = files["serverless/__init__.py"]
        assert "class Function" in init_content
        assert "AWS::Serverless::Function" in init_content

    def test_init_has_all_resource_classes(self):
        """__init__.py should contain all SAM resource classes."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        init_content = files["serverless/__init__.py"]
        expected_classes = [
            "class Api",
            "class Application",
            "class Connector",
            "class Function",
            "class GraphQLApi",
            "class HttpApi",
            "class LayerVersion",
            "class SimpleTable",
            "class StateMachine",
        ]
        for class_def in expected_classes:
            assert class_def in init_content, f"Missing {class_def}"

    def test_generates_property_type_modules(self):
        """Should generate PropertyType submodules."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        # Function has many nested types (events, etc.)
        assert "serverless/Function.py" in files

    def test_generated_code_is_valid_python(self):
        """All generated files should be valid Python."""
        schema = parse_sam_resources()
        resources = [r for r in schema.resources if r.service == "serverless"]
        nested = [n for n in schema.nested_types if n.service == "serverless"]

        files = generate_service_package(
            service="serverless",
            resources=resources,
            nested_types=nested,
            cf_spec_version="SAM-2016-10-31",
        )

        for filename, content in files.items():
            if filename.endswith(".py"):
                compile(content, filename, "exec")
