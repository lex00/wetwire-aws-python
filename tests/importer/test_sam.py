"""Tests for SAM template import and code generation."""

from pathlib import Path

import pytest

from wetwire_aws.importer.codegen import generate_code
from wetwire_aws.importer.parser import parse_template

TEMPLATES_DIR = Path(__file__).parent / "templates"


class TestSAMFunctionTemplate:
    """Tests for generating code from sam_function.yaml."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "sam_function.yaml")
        return generate_code(template)

    def test_has_sam_docstring(self, code):
        assert '"""' in code
        assert "Simple SAM function" in code

    def test_has_serverless_import(self, code):
        assert "from wetwire_aws.resources import serverless" in code

    def test_has_function_class(self, code):
        # Inheritance pattern: class ProcessorFunction(serverless.Function)
        assert "class ProcessorFunction(serverless.Function):" in code

    def test_function_has_properties(self, code):
        assert "function_name = 'processor'" in code
        assert "runtime = 'python3.12'" in code
        assert "handler = 'app.handler'" in code
        assert "code_uri = './src'" in code
        assert "memory_size = 256" in code
        assert "timeout = 30" in code

    def test_has_output(self, code):
        assert "class FunctionArnOutput:" in code
        assert "value = ProcessorFunction.Arn" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestSAMApiFunctionTemplate:
    """Tests for generating code from sam_api_function.yaml."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "sam_api_function.yaml")
        return generate_code(template)

    def test_has_parameter(self, code):
        # Parameter class name is derived from the parameter name
        assert "class Environment:" in code
        assert "resource: Parameter" in code
        assert "default = 'dev'" in code

    def test_has_api_class(self, code):
        # Inheritance pattern: class MyApi(serverless.Api)
        assert "class MyApi(serverless.Api):" in code

    def test_api_has_stage_name_ref(self, code):
        # Stage name references the parameter (class name without Param suffix)
        assert "stage_name = Environment" in code

    def test_has_function_class(self, code):
        assert "class GetItemsFunction(serverless.Function):" in code

    def test_function_has_runtime(self, code):
        assert "runtime = 'python3.12'" in code

    def test_function_has_memory_and_timeout(self, code):
        assert "memory_size = 256" in code
        assert "timeout = 30" in code

    def test_function_has_environment_ref(self, code):
        # Environment variable references parameter (without Param suffix)
        # The variables dict should reference the Environment class
        assert "'ENVIRONMENT': Environment" in code

    def test_has_api_output(self, code):
        assert "class ApiEndpointOutput:" in code
        # Output uses Sub intrinsic
        assert "Sub(" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestSAMTableTemplate:
    """Tests for generating code from sam_table.yaml."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "sam_table.yaml")
        return generate_code(template)

    def test_has_serverless_import(self, code):
        assert "from wetwire_aws.resources import serverless" in code

    def test_has_table_class(self, code):
        # Inheritance pattern: class ItemsTable(serverless.SimpleTable)
        assert "class ItemsTable(serverless.SimpleTable):" in code

    def test_table_has_properties(self, code):
        assert "table_name = 'items-table'" in code

    def test_table_has_primary_key(self, code):
        # Primary key should be a nested property type
        assert "primary_key" in code

    def test_has_output(self, code):
        assert "class TableArnOutput:" in code
        assert "value = ItemsTable.Arn" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestSAMResourceTypeMapping:
    """Tests for SAM resource type to service mapping."""

    def test_function_maps_to_serverless(self):
        template = parse_template(TEMPLATES_DIR / "sam_function.yaml")
        code = generate_code(template)
        # Should import from serverless, not lambda_
        assert "serverless.Function" in code
        assert "lambda_.Function" not in code

    def test_api_maps_to_serverless(self):
        template = parse_template(TEMPLATES_DIR / "sam_api_function.yaml")
        code = generate_code(template)
        assert "serverless.Api" in code
        assert "apigateway.Api" not in code

    def test_simple_table_maps_to_serverless(self):
        template = parse_template(TEMPLATES_DIR / "sam_table.yaml")
        code = generate_code(template)
        assert "serverless.SimpleTable" in code
        assert "dynamodb.Table" not in code


class TestSAMTransformHeader:
    """Tests for SAM Transform header handling."""

    def test_function_template_has_transform(self):
        """SAM templates should include the Transform header."""
        template_path = TEMPLATES_DIR / "sam_function.yaml"
        content = template_path.read_text()
        assert "Transform: AWS::Serverless-2016-10-31" in content

    def test_api_template_has_transform(self):
        template_path = TEMPLATES_DIR / "sam_api_function.yaml"
        content = template_path.read_text()
        assert "Transform: AWS::Serverless-2016-10-31" in content

    def test_table_template_has_transform(self):
        template_path = TEMPLATES_DIR / "sam_table.yaml"
        content = template_path.read_text()
        assert "Transform: AWS::Serverless-2016-10-31" in content
