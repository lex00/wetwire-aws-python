"""Tests for SAM resource parsing in codegen/parse.py."""

from codegen.parse import (
    extract_resource_name,
    extract_service_name,
    parse_sam_resources,
)
from codegen.schema import IntermediateSchema


class TestExtractServiceName:
    """Tests for extracting service name from SAM resources."""

    def test_serverless_function(self):
        """AWS::Serverless::Function -> serverless."""
        assert extract_service_name("AWS::Serverless::Function") == "serverless"

    def test_serverless_api(self):
        """AWS::Serverless::Api -> serverless."""
        assert extract_service_name("AWS::Serverless::Api") == "serverless"


class TestExtractResourceName:
    """Tests for extracting resource name from SAM resources."""

    def test_serverless_function(self):
        """AWS::Serverless::Function -> Function."""
        assert extract_resource_name("AWS::Serverless::Function") == "Function"

    def test_serverless_state_machine(self):
        """AWS::Serverless::StateMachine -> StateMachine."""
        assert extract_resource_name("AWS::Serverless::StateMachine") == "StateMachine"


class TestParseSAMResources:
    """Tests for parse_sam_resources function."""

    def test_returns_intermediate_schema(self):
        """parse_sam_resources should return an IntermediateSchema."""
        schema = parse_sam_resources()
        assert isinstance(schema, IntermediateSchema)

    def test_has_all_nine_resources(self):
        """Schema should contain all 9 SAM resource types."""
        schema = parse_sam_resources()
        resource_names = {r.name for r in schema.resources}
        expected = {
            "Function",
            "Api",
            "HttpApi",
            "SimpleTable",
            "LayerVersion",
            "StateMachine",
            "Application",
            "Connector",
            "GraphQLApi",
        }
        assert expected.issubset(resource_names)

    def test_all_resources_have_serverless_service(self):
        """All SAM resources should have service='serverless'."""
        schema = parse_sam_resources()
        for resource in schema.resources:
            if resource.full_type.startswith("AWS::Serverless::"):
                assert resource.service == "serverless"

    def test_function_has_properties(self):
        """Function resource should have expected properties."""
        schema = parse_sam_resources()
        function = next(r for r in schema.resources if r.name == "Function")

        prop_names = {p.name for p in function.properties}
        assert "handler" in prop_names
        assert "runtime" in prop_names
        assert "code_uri" in prop_names
        assert "memory_size" in prop_names

    def test_function_has_attributes(self):
        """Function resource should have Arn attribute."""
        schema = parse_sam_resources()
        function = next(r for r in schema.resources if r.name == "Function")

        attr_names = {a.name for a in function.attributes}
        assert "Arn" in attr_names

    def test_has_nested_types(self):
        """Schema should contain SAM property types."""
        schema = parse_sam_resources()
        # Should have nested types like ApiEvent, S3Event, etc.
        nested_names = {n.name for n in schema.nested_types}
        assert "ApiEvent" in nested_names or len(schema.nested_types) > 0

    def test_api_event_has_path_method(self):
        """ApiEvent nested type should have Path and Method properties."""
        schema = parse_sam_resources()
        api_event = next((n for n in schema.nested_types if n.name == "ApiEvent"), None)
        if api_event:
            prop_names = {p.name for p in api_event.properties}
            assert "path" in prop_names
            assert "method" in prop_names

    def test_schema_domain_is_aws(self):
        """Schema domain should be 'aws'."""
        schema = parse_sam_resources()
        assert schema.domain == "aws"
