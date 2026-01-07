"""Tests for CloudFormation template generation."""

import json
from dataclasses import dataclass
from typing import ClassVar

from wetwire_aws.base import CloudFormationResource
from wetwire_aws.intrinsics import Equals, GetAtt, Ref, Sub
from wetwire_aws.template import CloudFormationTemplate


@dataclass
class SampleBucket(CloudFormationResource):
    """Sample S3 bucket resource for testing."""

    _resource_type: ClassVar[str] = "AWS::S3::Bucket"
    bucket_name: str
    versioning_enabled: bool = False


@dataclass
class SampleQueue(CloudFormationResource):
    """Sample SQS queue resource for testing."""

    _resource_type: ClassVar[str] = "AWS::SQS::Queue"
    queue_name: str
    visibility_timeout: int = 30


@dataclass
class SampleFunction(CloudFormationResource):
    """Sample Lambda function resource for testing."""

    _resource_type: ClassVar[str] = "AWS::Lambda::Function"
    function_name: str
    runtime: str
    handler: str
    code_uri: str


class TestCloudFormationTemplate:
    """Tests for CloudFormationTemplate class."""

    def test_empty_template(self):
        """Empty template has correct structure."""
        template = CloudFormationTemplate(description="Test template")
        result = template.to_dict()

        assert result["AWSTemplateFormatVersion"] == "2010-09-09"
        assert result["Description"] == "Test template"
        assert result["Resources"] == {}

    def test_add_resource(self):
        """Adding a resource works correctly."""
        template = CloudFormationTemplate()
        bucket = SampleBucket(bucket_name="my-bucket")
        template.add_resource("MyBucket", bucket)

        result = template.to_dict()
        assert "MyBucket" in result["Resources"]
        assert result["Resources"]["MyBucket"]["Type"] == "AWS::S3::Bucket"

    def test_add_multiple_resources(self):
        """Adding multiple resources works correctly."""
        template = CloudFormationTemplate()
        template.add_resource("Bucket", SampleBucket(bucket_name="bucket"))
        template.add_resource("Queue", SampleQueue(queue_name="queue"))

        result = template.to_dict()
        assert len(result["Resources"]) == 2
        assert "Bucket" in result["Resources"]
        assert "Queue" in result["Resources"]

    def test_add_parameter(self):
        """Adding a parameter works correctly."""
        template = CloudFormationTemplate()
        template.add_parameter(
            "Environment",
            type="String",
            description="Deployment environment",
            allowed_values=["dev", "staging", "prod"],
            default="dev",
        )

        result = template.to_dict()
        assert "Parameters" in result
        assert "Environment" in result["Parameters"]
        assert result["Parameters"]["Environment"]["Type"] == "String"
        assert result["Parameters"]["Environment"]["Default"] == "dev"

    def test_add_output(self):
        """Adding an output works correctly."""
        template = CloudFormationTemplate()
        bucket = SampleBucket(bucket_name="my-bucket")
        template.add_resource("MyBucket", bucket)
        template.add_output(
            "BucketArn",
            value=GetAtt("MyBucket", "Arn"),
            description="The bucket ARN",
            export_name="MyStack-BucketArn",
        )

        result = template.to_dict()
        assert "Outputs" in result
        assert "BucketArn" in result["Outputs"]
        assert result["Outputs"]["BucketArn"]["Value"] == {
            "Fn::GetAtt": ["MyBucket", "Arn"]
        }
        assert result["Outputs"]["BucketArn"]["Export"]["Name"] == "MyStack-BucketArn"

    def test_add_condition(self):
        """Adding a condition works correctly."""
        template = CloudFormationTemplate()
        template.add_parameter("Environment", type="String", default="dev")
        template.add_condition("IsProd", Equals(Ref("Environment"), "prod"))

        result = template.to_dict()
        assert "Conditions" in result
        assert "IsProd" in result["Conditions"]

    def test_add_mapping(self):
        """Adding a mapping works correctly."""
        template = CloudFormationTemplate()
        template.add_mapping(
            "RegionMap",
            {
                "us-east-1": {"AMI": "ami-12345"},
                "us-west-2": {"AMI": "ami-67890"},
            },
        )

        result = template.to_dict()
        assert "Mappings" in result
        assert "RegionMap" in result["Mappings"]
        assert result["Mappings"]["RegionMap"]["us-east-1"]["AMI"] == "ami-12345"

    def test_to_json(self):
        """to_json() produces valid JSON."""
        template = CloudFormationTemplate(description="JSON test")
        template.add_resource("Bucket", SampleBucket(bucket_name="test"))

        json_str = template.to_json()
        parsed = json.loads(json_str)

        assert parsed["Description"] == "JSON test"
        assert "Bucket" in parsed["Resources"]

    def test_to_json_indent(self):
        """to_json() respects indent parameter."""
        template = CloudFormationTemplate()
        template.add_resource("Bucket", SampleBucket(bucket_name="test"))

        compact = template.to_json(indent=None)
        pretty = template.to_json(indent=2)

        assert "\n" not in compact
        assert "\n" in pretty

    def test_to_yaml(self):
        """to_yaml() produces valid YAML."""
        template = CloudFormationTemplate(description="YAML test")
        template.add_resource("Bucket", SampleBucket(bucket_name="test"))

        yaml_str = template.to_yaml()

        assert "AWSTemplateFormatVersion" in yaml_str
        assert "Description: YAML test" in yaml_str
        assert "Bucket:" in yaml_str

    def test_resource_with_depends_on(self):
        """Resource DependsOn is included."""
        template = CloudFormationTemplate()
        bucket = SampleBucket(bucket_name="bucket")
        queue = SampleQueue(queue_name="queue")
        queue.depends_on = [SampleBucket]

        template.add_resource("Bucket", bucket)
        template.add_resource("Queue", queue)

        result = template.to_dict()
        assert result["Resources"]["Queue"]["DependsOn"] == ["SampleBucket"]

    def test_resource_with_condition(self):
        """Resource Condition is included."""
        template = CloudFormationTemplate()
        template.add_parameter("CreateBucket", type="String", default="true")
        template.add_condition("ShouldCreate", Equals(Ref("CreateBucket"), "true"))

        bucket = SampleBucket(bucket_name="conditional-bucket")
        bucket.condition = "ShouldCreate"
        template.add_resource("Bucket", bucket)

        result = template.to_dict()
        assert result["Resources"]["Bucket"]["Condition"] == "ShouldCreate"

    def test_intrinsic_in_property(self):
        """Intrinsic functions in properties are serialized."""
        template = CloudFormationTemplate()
        template.add_parameter("BucketPrefix", type="String")

        bucket = SampleBucket(bucket_name=Sub("${BucketPrefix}-data"))
        template.add_resource("Bucket", bucket)

        result = template.to_dict()
        assert result["Resources"]["Bucket"]["Properties"]["BucketName"] == {
            "Fn::Sub": "${BucketPrefix}-data"
        }


class TestTemplateIntegration:
    """Integration tests for complete templates."""

    def test_complete_stack(self):
        """Complete stack with all components."""
        template = CloudFormationTemplate(
            description="Complete test stack",
            transform=["AWS::Serverless-2016-10-31"],
        )

        # Parameters
        template.add_parameter(
            "Environment",
            type="String",
            allowed_values=["dev", "prod"],
            default="dev",
        )

        # Conditions
        template.add_condition("IsProd", Equals(Ref("Environment"), "prod"))

        # Mappings
        template.add_mapping(
            "Config",
            {
                "dev": {"Retention": "7"},
                "prod": {"Retention": "30"},
            },
        )

        # Resources
        bucket = SampleBucket(
            bucket_name=Sub("${AWS::StackName}-data"),
            versioning_enabled=True,
        )
        template.add_resource("DataBucket", bucket)

        # Outputs
        template.add_output(
            "BucketName",
            value=Ref("DataBucket"),
            description="Name of the data bucket",
        )

        result = template.to_dict()

        # Verify structure
        assert result["AWSTemplateFormatVersion"] == "2010-09-09"
        assert result["Description"] == "Complete test stack"
        assert result["Transform"] == ["AWS::Serverless-2016-10-31"]
        assert "Parameters" in result
        assert "Conditions" in result
        assert "Mappings" in result
        assert "Resources" in result
        assert "Outputs" in result

    def test_template_validates_json(self):
        """Generated JSON is valid."""
        template = CloudFormationTemplate()
        template.add_resource("Bucket", SampleBucket(bucket_name="test"))
        template.add_resource("Queue", SampleQueue(queue_name="test"))

        json_str = template.to_json()

        # Should not raise
        parsed = json.loads(json_str)
        assert isinstance(parsed, dict)


class TestSAMTemplateIntegration:
    """Integration tests for SAM templates."""

    def test_sam_transform_header(self):
        """SAM template should include Transform header."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            description="SAM function test",
            transform="AWS::Serverless-2016-10-31",
        )

        func = serverless.Function(
            function_name="processor",
            runtime=serverless.Runtime.PYTHON3_12,
            handler="app.handler",
            code_uri="./src",
        )
        template.add_resource("ProcessorFunction", func)

        result = template.to_dict()

        assert result["Transform"] == "AWS::Serverless-2016-10-31"
        assert "ProcessorFunction" in result["Resources"]
        assert (
            result["Resources"]["ProcessorFunction"]["Type"]
            == "AWS::Serverless::Function"
        )

    def test_sam_function_with_events(self):
        """SAM Function with events should serialize correctly."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            transform="AWS::Serverless-2016-10-31",
        )

        api_event = serverless.Function.ApiEvent(
            path="/process",
            method="POST",
        )
        func = serverless.Function(
            handler="app.handler",
            runtime=serverless.Runtime.PYTHON3_12,
            code_uri="./src",
            events={"ApiEvent": api_event},
        )
        template.add_resource("ProcessorFunction", func)

        result = template.to_dict()
        props = result["Resources"]["ProcessorFunction"]["Properties"]

        assert "Events" in props
        assert "ApiEvent" in props["Events"]
        assert props["Events"]["ApiEvent"]["Path"] == "/process"
        assert props["Events"]["ApiEvent"]["Method"] == "POST"

    def test_sam_api_resource(self):
        """SAM Api resource should serialize correctly."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            transform="AWS::Serverless-2016-10-31",
        )

        api = serverless.Api(
            stage_name="prod",
            cors="'*'",
        )
        template.add_resource("MyApi", api)

        result = template.to_dict()

        assert result["Resources"]["MyApi"]["Type"] == "AWS::Serverless::Api"
        assert result["Resources"]["MyApi"]["Properties"]["StageName"] == "prod"
        assert result["Resources"]["MyApi"]["Properties"]["Cors"] == "'*'"

    def test_sam_httpapi_with_cors(self):
        """SAM HttpApi with CORS should serialize correctly."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            transform="AWS::Serverless-2016-10-31",
        )

        cors = serverless.HttpApi.CorsConfiguration(
            allow_origins=["https://example.com"],
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )
        api = serverless.HttpApi(
            stage_name="$default",
            cors_configuration=cors,
        )
        template.add_resource("MyHttpApi", api)

        result = template.to_dict()
        props = result["Resources"]["MyHttpApi"]["Properties"]

        assert props["StageName"] == "$default"
        assert props["CorsConfiguration"]["AllowOrigins"] == ["https://example.com"]
        assert props["CorsConfiguration"]["AllowMethods"] == [
            "GET",
            "POST",
            "PUT",
            "DELETE",
        ]

    def test_sam_simpletable_resource(self):
        """SAM SimpleTable should serialize correctly."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            transform="AWS::Serverless-2016-10-31",
        )

        pk = serverless.SimpleTable.PrimaryKey(
            name="id",
            type_="String",
        )
        table = serverless.SimpleTable(
            table_name="my-table",
            primary_key=pk,
        )
        template.add_resource("MyTable", table)

        result = template.to_dict()
        props = result["Resources"]["MyTable"]["Properties"]

        assert result["Resources"]["MyTable"]["Type"] == "AWS::Serverless::SimpleTable"
        assert props["TableName"] == "my-table"
        assert props["PrimaryKey"]["Name"] == "id"
        assert props["PrimaryKey"]["Type"] == "String"

    def test_sam_statemachine_resource(self):
        """SAM StateMachine should serialize correctly."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            transform="AWS::Serverless-2016-10-31",
        )

        definition = {
            "StartAt": "HelloWorld",
            "States": {
                "HelloWorld": {
                    "Type": "Pass",
                    "Result": "Hello, World!",
                    "End": True,
                },
            },
        }
        sm = serverless.StateMachine(
            name="my-workflow",
            definition=definition,
        )
        template.add_resource("MyStateMachine", sm)

        result = template.to_dict()
        props = result["Resources"]["MyStateMachine"]["Properties"]

        assert (
            result["Resources"]["MyStateMachine"]["Type"]
            == "AWS::Serverless::StateMachine"
        )
        assert props["Name"] == "my-workflow"
        assert props["Definition"]["StartAt"] == "HelloWorld"

    def test_sam_complete_serverless_app(self):
        """Complete SAM application with multiple resources."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            description="Complete SAM application",
            transform="AWS::Serverless-2016-10-31",
        )

        # Add parameters
        template.add_parameter(
            "Environment",
            type="String",
            allowed_values=["dev", "staging", "prod"],
            default="dev",
        )

        # Add API
        api = serverless.Api(
            stage_name=Ref("Environment"),
        )
        template.add_resource("Api", api)

        # Add Function with events
        api_event = serverless.Function.ApiEvent(
            path="/items",
            method="GET",
            rest_api_id=Ref("Api"),
        )
        env = serverless.Function.Environment(
            variables={"TABLE_NAME": Ref("ItemsTable")},
        )
        func = serverless.Function(
            handler="src/handlers/items.handler",
            runtime=serverless.Runtime.PYTHON3_12,
            code_uri=".",
            memory_size=256,
            timeout=30,
            environment=env,
            events={"GetItems": api_event},
        )
        template.add_resource("GetItemsFunction", func)

        # Add SimpleTable
        pk = serverless.SimpleTable.PrimaryKey(name="id", type_="String")
        table = serverless.SimpleTable(
            table_name=Sub("${AWS::StackName}-items"),
            primary_key=pk,
        )
        template.add_resource("ItemsTable", table)

        # Add outputs
        template.add_output(
            "ApiUrl",
            value=Sub(
                "https://${Api}.execute-api.${AWS::Region}.amazonaws.com/${Environment}"
            ),
            description="API Gateway URL",
        )

        result = template.to_dict()

        # Verify structure
        assert result["Transform"] == "AWS::Serverless-2016-10-31"
        assert result["Description"] == "Complete SAM application"
        assert "Parameters" in result
        assert "Environment" in result["Parameters"]

        # Verify resources
        assert len(result["Resources"]) == 3
        assert result["Resources"]["Api"]["Type"] == "AWS::Serverless::Api"
        assert (
            result["Resources"]["GetItemsFunction"]["Type"]
            == "AWS::Serverless::Function"
        )
        assert (
            result["Resources"]["ItemsTable"]["Type"] == "AWS::Serverless::SimpleTable"
        )

        # Verify outputs
        assert "ApiUrl" in result["Outputs"]

        # Verify JSON is valid
        json_str = template.to_json()
        parsed = json.loads(json_str)
        assert parsed["Transform"] == "AWS::Serverless-2016-10-31"

    def test_sam_template_to_yaml(self):
        """SAM template should export to valid YAML."""
        from wetwire_aws.resources import serverless

        template = CloudFormationTemplate(
            description="SAM YAML test",
            transform="AWS::Serverless-2016-10-31",
        )

        func = serverless.Function(
            handler="app.handler",
            runtime=serverless.Runtime.NODEJS20_X,
            code_uri="./dist",
        )
        template.add_resource("MyFunction", func)

        yaml_str = template.to_yaml()

        assert "Transform: AWS::Serverless-2016-10-31" in yaml_str
        assert "AWS::Serverless::Function" in yaml_str
        assert "nodejs20.x" in yaml_str
