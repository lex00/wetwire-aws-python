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
        # Inheritance pattern: class FunctionArnOutput(Output)
        assert "class FunctionArnOutput(Output):" in code
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
        # Inheritance pattern: class Environment(Parameter)
        assert "class Environment(Parameter):" in code
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
        # Inheritance pattern: class ApiEndpointOutput(Output)
        assert "class ApiEndpointOutput(Output):" in code
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
        # Inheritance pattern: class TableArnOutput(Output)
        assert "class TableArnOutput(Output):" in code
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


class TestSAMImplicitResources:
    """Tests for handling SAM implicit resources (auto-created by SAM transform).

    SAM automatically creates resources like roles, API stages, and deployments.
    Templates may reference these implicit resources, so the importer should
    handle them gracefully instead of raising errors.
    """

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "sam_implicit_resources.yaml")
        return generate_code(template)

    def test_generates_valid_python(self, code):
        """Template with implicit resource refs should still produce valid Python."""
        compile(code, "<test>", "exec")

    def test_has_explicit_function(self, code):
        """Explicitly defined resources should be generated normally."""
        assert "class MyFunction(serverless.Function):" in code

    def test_has_bucket_with_depends_on(self, code):
        """Bucket should be generated with depends_on referencing implicit role."""
        assert "class MyBucket(s3.Bucket):" in code
        # The depends_on should use explicit Ref for the implicit resource
        assert "depends_on" in code

    def test_output_with_implicit_getatt(self, code):
        """Output referencing implicit resource should use GetAtt intrinsic."""
        # Should have GetAtt for the implicit MyFunctionRole with noqa comment
        assert 'GetAtt("MyFunctionRole", "Arn")' in code
        assert "noqa: WAW020" in code

    def test_output_with_explicit_resource(self, code):
        """Output referencing explicit resource should use no-parens pattern."""
        # MyFunction.Arn should use the normal no-parens pattern
        assert "MyFunction.Arn" in code

    def test_imports_ref_or_getatt_if_needed(self, code):
        """Should import Ref/GetAtt when used for implicit resources."""
        # Either Ref or GetAtt should be imported
        has_ref_import = "from wetwire_aws.intrinsics import" in code and "Ref" in code
        has_getatt_import = (
            "from wetwire_aws.intrinsics import" in code and "GetAtt" in code
        )
        assert has_ref_import or has_getatt_import


class TestCookiecutterFiltering:
    """Tests for cookiecutter template filtering.

    The import script should skip templates containing cookiecutter variables
    but still import valid templates from cookiecutter project directories.
    """

    def test_has_cookiecutter_syntax_detects_variables(self, tmp_path):
        """Templates with {{cookiecutter.foo}} should be detected."""
        # Import the function we're testing
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from import_sam_samples import has_cookiecutter_syntax

        # Create template with cookiecutter syntax
        template = tmp_path / "template.yaml"
        template.write_text("""
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: {{cookiecutter.function_name}}
""")
        assert has_cookiecutter_syntax(template) is True

    def test_has_cookiecutter_syntax_with_spaces(self, tmp_path):
        """Templates with {{ cookiecutter.foo }} should be detected."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from import_sam_samples import has_cookiecutter_syntax

        template = tmp_path / "template.yaml"
        template.write_text("""
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: {{ cookiecutter.function_name }}
""")
        assert has_cookiecutter_syntax(template) is True

    def test_has_cookiecutter_syntax_clean_template(self, tmp_path):
        """Templates without cookiecutter syntax should pass."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from import_sam_samples import has_cookiecutter_syntax

        template = tmp_path / "template.yaml"
        template.write_text("""
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: my-function
""")
        assert has_cookiecutter_syntax(template) is False

    def test_cookiecutter_directory_not_excluded(self):
        """Cookiecutter directories should not be excluded by path alone."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from import_sam_samples import EXCLUDE_PATTERNS

        # "cookiecutter" should not be in EXCLUDE_PATTERNS
        assert "cookiecutter" not in EXCLUDE_PATTERNS

    def test_sam_repos_includes_crud_sample(self):
        """SAM_REPOS should include sam-python-crud-sample."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from import_sam_samples import SAM_REPOS

        repo_names = [r["name"] for r in SAM_REPOS]
        assert "sam-python-crud-sample" in repo_names
