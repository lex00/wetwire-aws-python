"""Tests for SAM spec definitions."""

from codegen.sam_spec import (
    SAM_PROPERTY_TYPES,
    SAM_RESOURCES,
    get_sam_property_types,
    get_sam_resources,
)


class TestSAMResources:
    """Tests for SAM resource definitions."""

    def test_sam_resources_dict_exists(self):
        """SAM_RESOURCES should be a non-empty dict."""
        assert isinstance(SAM_RESOURCES, dict)
        assert len(SAM_RESOURCES) > 0

    def test_all_nine_sam_resources_defined(self):
        """All 9 SAM resource types should be defined."""
        expected_resources = [
            "AWS::Serverless::Function",
            "AWS::Serverless::Api",
            "AWS::Serverless::HttpApi",
            "AWS::Serverless::SimpleTable",
            "AWS::Serverless::LayerVersion",
            "AWS::Serverless::StateMachine",
            "AWS::Serverless::Application",
            "AWS::Serverless::Connector",
            "AWS::Serverless::GraphQLApi",
        ]
        for resource_type in expected_resources:
            assert resource_type in SAM_RESOURCES, f"Missing {resource_type}"

    def test_function_has_required_properties(self):
        """Function should have Handler as required property."""
        func = SAM_RESOURCES["AWS::Serverless::Function"]
        props = func["Properties"]
        assert "Handler" in props
        # Handler is required for Zip package type
        # (but CodeUri/ImageUri may be alternatives)

    def test_function_has_common_properties(self):
        """Function should have common SAM properties."""
        func = SAM_RESOURCES["AWS::Serverless::Function"]
        props = func["Properties"]
        expected_props = [
            "FunctionName",
            "Runtime",
            "Handler",
            "CodeUri",
            "Description",
            "MemorySize",
            "Timeout",
            "Environment",
            "Events",
            "Policies",
            "Architectures",
        ]
        for prop in expected_props:
            assert prop in props, f"Function missing property {prop}"

    def test_function_has_attributes(self):
        """Function should have Arn attribute for GetAtt."""
        func = SAM_RESOURCES["AWS::Serverless::Function"]
        assert "Attributes" in func
        attrs = func["Attributes"]
        assert "Arn" in attrs

    def test_api_has_properties(self):
        """Api should have StageName and other properties."""
        api = SAM_RESOURCES["AWS::Serverless::Api"]
        props = api["Properties"]
        assert "StageName" in props
        assert "DefinitionBody" in props or "DefinitionUri" in props

    def test_simple_table_has_properties(self):
        """SimpleTable should have PrimaryKey property."""
        table = SAM_RESOURCES["AWS::Serverless::SimpleTable"]
        props = table["Properties"]
        assert "PrimaryKey" in props

    def test_resource_has_documentation(self):
        """Resources should have Documentation field."""
        func = SAM_RESOURCES["AWS::Serverless::Function"]
        assert "Documentation" in func
        assert len(func["Documentation"]) > 0


class TestSAMPropertyTypes:
    """Tests for SAM property type definitions."""

    def test_sam_property_types_dict_exists(self):
        """SAM_PROPERTY_TYPES should be a dict."""
        assert isinstance(SAM_PROPERTY_TYPES, dict)

    def test_function_event_types_defined(self):
        """Function event types should be defined."""
        # Events are nested property types
        expected_event_types = [
            "AWS::Serverless::Function.ApiEvent",
            "AWS::Serverless::Function.S3Event",
            "AWS::Serverless::Function.SQSEvent",
            "AWS::Serverless::Function.ScheduleEvent",
        ]
        for event_type in expected_event_types:
            assert event_type in SAM_PROPERTY_TYPES, f"Missing {event_type}"

    def test_api_event_has_path_and_method(self):
        """ApiEvent should have Path and Method properties."""
        api_event = SAM_PROPERTY_TYPES["AWS::Serverless::Function.ApiEvent"]
        props = api_event["Properties"]
        assert "Path" in props
        assert "Method" in props

    def test_environment_type_defined(self):
        """Environment property type should be defined."""
        assert "AWS::Serverless::Function.Environment" in SAM_PROPERTY_TYPES
        env = SAM_PROPERTY_TYPES["AWS::Serverless::Function.Environment"]
        assert "Variables" in env["Properties"]


class TestSAMSpecHelpers:
    """Tests for helper functions."""

    def test_get_sam_resources_returns_dict(self):
        """get_sam_resources() should return resource definitions."""
        resources = get_sam_resources()
        assert isinstance(resources, dict)
        assert "AWS::Serverless::Function" in resources

    def test_get_sam_property_types_returns_dict(self):
        """get_sam_property_types() should return property type definitions."""
        prop_types = get_sam_property_types()
        assert isinstance(prop_types, dict)


class TestSAMEnums:
    """Tests for SAM enum definitions."""

    def test_runtime_values_defined(self):
        """Runtime enum values should be available."""
        from codegen.sam_spec import SAM_ENUMS

        assert "Runtime" in SAM_ENUMS
        runtimes = SAM_ENUMS["Runtime"]
        assert "python3.12" in runtimes
        assert "nodejs20.x" in runtimes

    def test_architecture_values_defined(self):
        """Architecture enum values should be available."""
        from codegen.sam_spec import SAM_ENUMS

        assert "Architecture" in SAM_ENUMS
        archs = SAM_ENUMS["Architecture"]
        assert "x86_64" in archs
        assert "arm64" in archs

    def test_package_type_values_defined(self):
        """PackageType enum values should be available."""
        from codegen.sam_spec import SAM_ENUMS

        assert "PackageType" in SAM_ENUMS
        pkg_types = SAM_ENUMS["PackageType"]
        assert "Zip" in pkg_types
        assert "Image" in pkg_types
