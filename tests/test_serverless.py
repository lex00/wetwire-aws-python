"""Tests for serverless (SAM) resource types."""

import json

import pytest

from wetwire_aws.resources import serverless


class TestServerlessImports:
    """Tests for importing serverless resources."""

    def test_import_serverless(self):
        """Should be able to import serverless module."""
        assert hasattr(serverless, "Function")
        assert serverless.Function._resource_type == "AWS::Serverless::Function"

    def test_import_all_sam_resources(self):
        """Should be able to import all 9 SAM resource types."""
        expected_resources = [
            "Function",
            "Api",
            "HttpApi",
            "SimpleTable",
            "LayerVersion",
            "StateMachine",
            "Application",
            "Connector",
            "GraphQLApi",
        ]
        for resource in expected_resources:
            assert hasattr(serverless, resource), f"Missing resource: {resource}"


class TestServerlessResourceTypes:
    """Tests for SAM resource type values."""

    @pytest.mark.parametrize(
        "resource_name,expected_type",
        [
            ("Function", "AWS::Serverless::Function"),
            ("Api", "AWS::Serverless::Api"),
            ("HttpApi", "AWS::Serverless::HttpApi"),
            ("SimpleTable", "AWS::Serverless::SimpleTable"),
            ("LayerVersion", "AWS::Serverless::LayerVersion"),
            ("StateMachine", "AWS::Serverless::StateMachine"),
            ("Application", "AWS::Serverless::Application"),
            ("Connector", "AWS::Serverless::Connector"),
            ("GraphQLApi", "AWS::Serverless::GraphQLApi"),
        ],
    )
    def test_resource_type_value(self, resource_name, expected_type):
        """Each resource should have correct _resource_type."""
        cls = getattr(serverless, resource_name)
        assert cls._resource_type == expected_type


class TestServerlessEnums:
    """Tests for SAM-specific enums."""

    def test_runtime_enum_exists(self):
        """Runtime enum should exist."""
        assert hasattr(serverless, "Runtime")

    def test_runtime_python_values(self):
        """Runtime should have Python runtimes."""
        assert serverless.Runtime.PYTHON3_9 == "python3.9"
        assert serverless.Runtime.PYTHON3_10 == "python3.10"
        assert serverless.Runtime.PYTHON3_11 == "python3.11"
        assert serverless.Runtime.PYTHON3_12 == "python3.12"
        assert serverless.Runtime.PYTHON3_13 == "python3.13"

    def test_runtime_nodejs_values(self):
        """Runtime should have Node.js runtimes."""
        assert serverless.Runtime.NODEJS18_X == "nodejs18.x"
        assert serverless.Runtime.NODEJS20_X == "nodejs20.x"
        assert serverless.Runtime.NODEJS22_X == "nodejs22.x"

    def test_runtime_java_values(self):
        """Runtime should have Java runtimes."""
        assert serverless.Runtime.JAVA11 == "java11"
        assert serverless.Runtime.JAVA17 == "java17"
        assert serverless.Runtime.JAVA21 == "java21"

    def test_runtime_dotnet_values(self):
        """Runtime should have .NET runtimes."""
        assert serverless.Runtime.DOTNET6 == "dotnet6"
        assert serverless.Runtime.DOTNET8 == "dotnet8"

    def test_runtime_provided_values(self):
        """Runtime should have custom runtime values."""
        assert serverless.Runtime.PROVIDED == "provided"
        assert serverless.Runtime.PROVIDED_AL2 == "provided.al2"
        assert serverless.Runtime.PROVIDED_AL2023 == "provided.al2023"

    def test_architecture_enum(self):
        """Architecture enum should have x86_64 and arm64."""
        assert serverless.Architecture.X86_64 == "x86_64"
        assert serverless.Architecture.ARM64 == "arm64"

    def test_package_type_enum(self):
        """PackageType enum should have Zip and Image."""
        assert serverless.PackageType.ZIP == "Zip"
        assert serverless.PackageType.IMAGE == "Image"

    def test_auth_type_enum(self):
        """AuthType enum should have auth types."""
        assert serverless.AuthType.NONE == "NONE"
        assert serverless.AuthType.AWS_IAM == "AWS_IAM"
        assert serverless.AuthType.COGNITO_USER_POOLS == "COGNITO_USER_POOLS"

    def test_http_api_auth_type_enum(self):
        """HttpApiAuthType enum should have HTTP API auth types."""
        assert serverless.HttpApiAuthType.NONE == "NONE"
        assert serverless.HttpApiAuthType.AWS_IAM == "AWS_IAM"
        assert serverless.HttpApiAuthType.JWT == "JWT"


class TestServerlessFunction:
    """Tests for serverless.Function resource."""

    def test_function_creation(self):
        """Should create a Function with basic properties."""
        func = serverless.Function(
            function_name="processor",
            runtime=serverless.Runtime.PYTHON3_12,
            handler="app.handler",
            code_uri="./src",
        )
        assert func.function_name == "processor"
        assert func.runtime == "python3.12"
        assert func.handler == "app.handler"
        assert func.code_uri == "./src"

    def test_function_with_memory_timeout(self):
        """Should create a Function with memory and timeout."""
        func = serverless.Function(
            handler="app.handler",
            memory_size=256,
            timeout=30,
        )
        assert func.memory_size == 256
        assert func.timeout == 30

    def test_function_to_dict(self):
        """Function.to_dict() should return valid CloudFormation structure."""
        func = serverless.Function(
            function_name="processor",
            runtime=serverless.Runtime.PYTHON3_12,
            handler="app.handler",
            code_uri="./src",
        )
        result = func.to_dict()

        assert result["Type"] == "AWS::Serverless::Function"
        assert "Properties" in result
        props = result["Properties"]
        assert props["FunctionName"] == "processor"
        assert props["Runtime"] == "python3.12"
        assert props["Handler"] == "app.handler"
        assert props["CodeUri"] == "./src"

    def test_function_with_environment(self):
        """Function should support environment variables."""
        env = serverless.Function.Environment(
            variables={"LOG_LEVEL": "DEBUG", "API_URL": "https://api.example.com"}
        )
        func = serverless.Function(
            handler="app.handler",
            environment=env,
        )
        result = func.to_dict()

        assert "Environment" in result["Properties"]
        assert result["Properties"]["Environment"]["Variables"]["LOG_LEVEL"] == "DEBUG"

    def test_function_with_vpc_config(self):
        """Function should support VPC configuration."""
        vpc = serverless.Function.VpcConfig(
            security_group_ids=["sg-12345"],
            subnet_ids=["subnet-1", "subnet-2"],
        )
        func = serverless.Function(
            handler="app.handler",
            vpc_config=vpc,
        )
        result = func.to_dict()

        assert "VpcConfig" in result["Properties"]
        vpc_config = result["Properties"]["VpcConfig"]
        assert vpc_config["SecurityGroupIds"] == ["sg-12345"]
        assert vpc_config["SubnetIds"] == ["subnet-1", "subnet-2"]

    def test_function_getatt_attributes(self):
        """Function should have GetAtt attributes."""
        assert serverless.Function.ARN == "Arn"


class TestServerlessApi:
    """Tests for serverless.Api resource."""

    def test_api_creation(self):
        """Should create an Api with basic properties."""
        api = serverless.Api(
            stage_name="prod",
            description="My API",
        )
        assert api.stage_name == "prod"
        assert api.description == "My API"

    def test_api_to_dict(self):
        """Api.to_dict() should return valid CloudFormation structure."""
        api = serverless.Api(
            stage_name="prod",
            cors="'*'",
        )
        result = api.to_dict()

        assert result["Type"] == "AWS::Serverless::Api"
        assert result["Properties"]["StageName"] == "prod"
        assert result["Properties"]["Cors"] == "'*'"

    def test_api_getatt_attributes(self):
        """Api should have GetAtt attributes."""
        assert serverless.Api.ROOTRESOURCEID == "RootResourceId"


class TestServerlessHttpApi:
    """Tests for serverless.HttpApi resource."""

    def test_httpapi_creation(self):
        """Should create an HttpApi with basic properties."""
        api = serverless.HttpApi(
            stage_name="$default",
            description="My HTTP API",
        )
        assert api.stage_name == "$default"
        assert api.description == "My HTTP API"

    def test_httpapi_with_cors(self):
        """HttpApi should support CORS configuration."""
        cors = serverless.HttpApi.CorsConfiguration(
            allow_origins=["https://example.com"],
            allow_methods=["GET", "POST"],
            allow_headers=["Content-Type"],
        )
        api = serverless.HttpApi(
            cors_configuration=cors,
        )
        result = api.to_dict()

        assert "CorsConfiguration" in result["Properties"]
        cors_config = result["Properties"]["CorsConfiguration"]
        assert cors_config["AllowOrigins"] == ["https://example.com"]

    def test_httpapi_getatt_attributes(self):
        """HttpApi should have GetAtt attributes."""
        assert serverless.HttpApi.APIENDPOINT == "ApiEndpoint"


class TestServerlessSimpleTable:
    """Tests for serverless.SimpleTable resource."""

    def test_simpletable_creation(self):
        """Should create a SimpleTable with basic properties."""
        table = serverless.SimpleTable(
            table_name="my-table",
        )
        assert table.table_name == "my-table"

    def test_simpletable_with_primary_key(self):
        """SimpleTable should support primary key configuration."""
        pk = serverless.SimpleTable.PrimaryKey(
            name="id",
            type_="String",
        )
        table = serverless.SimpleTable(
            table_name="my-table",
            primary_key=pk,
        )
        result = table.to_dict()

        assert "PrimaryKey" in result["Properties"]
        assert result["Properties"]["PrimaryKey"]["Name"] == "id"
        assert result["Properties"]["PrimaryKey"]["Type"] == "String"

    def test_simpletable_getatt_attributes(self):
        """SimpleTable should have GetAtt attributes."""
        assert serverless.SimpleTable.ARN == "Arn"


class TestServerlessLayerVersion:
    """Tests for serverless.LayerVersion resource."""

    def test_layerversion_creation(self):
        """Should create a LayerVersion with basic properties."""
        layer = serverless.LayerVersion(
            layer_name="my-layer",
            content_uri="./layer",
            compatible_runtimes=["python3.12", "python3.11"],
        )
        assert layer.layer_name == "my-layer"
        assert layer.content_uri == "./layer"
        assert layer.compatible_runtimes == ["python3.12", "python3.11"]

    def test_layerversion_getatt_attributes(self):
        """LayerVersion should have GetAtt attributes."""
        assert serverless.LayerVersion.ARN == "Arn"
        assert serverless.LayerVersion.LAYERVERSIONARN == "LayerVersionArn"


class TestServerlessStateMachine:
    """Tests for serverless.StateMachine resource."""

    def test_statemachine_creation(self):
        """Should create a StateMachine with basic properties."""
        sm = serverless.StateMachine(
            name="my-workflow",
            definition_uri="./statemachine.asl.json",
        )
        assert sm.name == "my-workflow"
        assert sm.definition_uri == "./statemachine.asl.json"

    def test_statemachine_with_inline_definition(self):
        """StateMachine should support inline definition."""
        definition = {
            "StartAt": "HelloWorld",
            "States": {
                "HelloWorld": {"Type": "Pass", "End": True},
            },
        }
        sm = serverless.StateMachine(
            definition=definition,
        )
        assert sm.definition == definition

    def test_statemachine_getatt_attributes(self):
        """StateMachine should have GetAtt attributes."""
        assert serverless.StateMachine.ARN == "Arn"
        assert serverless.StateMachine.NAME == "Name"


class TestServerlessApplication:
    """Tests for serverless.Application resource."""

    def test_application_creation(self):
        """Should create an Application with basic properties."""
        app = serverless.Application(
            location="arn:aws:serverlessrepo:us-east-1:123456789012:applications/my-app",
        )
        assert app.location.startswith("arn:aws:serverlessrepo")

    def test_application_with_parameters(self):
        """Application should support parameters."""
        app = serverless.Application(
            location="arn:aws:serverlessrepo:us-east-1:123456789012:applications/my-app",
            parameters={"Environment": "prod", "LogLevel": "INFO"},
        )
        assert app.parameters["Environment"] == "prod"

    def test_application_getatt_attributes(self):
        """Application should have GetAtt attributes."""
        assert serverless.Application.OUTPUTS == "Outputs"


class TestServerlessConnector:
    """Tests for serverless.Connector resource."""

    def test_connector_creation(self):
        """Should create a Connector with basic properties."""
        source = serverless.Connector.ConnectorSource(id="MyFunction")
        dest = serverless.Connector.ConnectorDestination(id="MyTable")
        conn = serverless.Connector(
            source=source,
            destination=dest,
            permissions=["Read", "Write"],
        )
        assert conn.permissions == ["Read", "Write"]


class TestServerlessGraphQLApi:
    """Tests for serverless.GraphQLApi resource."""

    def test_graphqlapi_creation(self):
        """Should create a GraphQLApi with basic properties."""
        api = serverless.GraphQLApi(
            name="my-graphql-api",
            schema_uri="./schema.graphql",
        )
        assert api.name == "my-graphql-api"
        assert api.schema_uri == "./schema.graphql"

    def test_graphqlapi_getatt_attributes(self):
        """GraphQLApi should have GetAtt attributes."""
        assert serverless.GraphQLApi.APIID == "ApiId"
        assert serverless.GraphQLApi.ARN == "Arn"
        assert serverless.GraphQLApi.GRAPHQLURL == "GraphQLUrl"


class TestServerlessSerialization:
    """Tests for SAM resource JSON serialization."""

    def test_function_serializes_to_valid_json(self):
        """Function should serialize to valid JSON."""
        func = serverless.Function(
            function_name="test",
            runtime=serverless.Runtime.PYTHON3_12,
            handler="app.handler",
            code_uri="./src",
        )
        result = func.to_dict()
        json_str = json.dumps(result)
        parsed = json.loads(json_str)
        assert parsed["Type"] == "AWS::Serverless::Function"

    def test_api_serializes_to_valid_json(self):
        """Api should serialize to valid JSON."""
        api = serverless.Api(
            stage_name="prod",
        )
        result = api.to_dict()
        json_str = json.dumps(result)
        parsed = json.loads(json_str)
        assert parsed["Type"] == "AWS::Serverless::Api"

    def test_nested_property_types_serialize(self):
        """Nested PropertyTypes should serialize correctly."""
        env = serverless.Function.Environment(
            variables={"KEY": "value"}
        )
        func = serverless.Function(
            handler="app.handler",
            environment=env,
        )
        result = func.to_dict()
        json_str = json.dumps(result)
        parsed = json.loads(json_str)
        assert parsed["Properties"]["Environment"]["Variables"]["KEY"] == "value"
