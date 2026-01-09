"""Tests for style-related rules.

Rules:
    WAW011: Use no-parens style for PropertyType wrappers
    WAW013: Use wrapper classes instead of inline constructors
    WAW014: Use wrapper classes instead of inline policy documents
    WAW015: Use wrapper classes instead of inline security group rules
    WAW016: Use wrapper classes instead of inline policy statements
    WAW017: Use wrapper class instead of inline property type dict
"""

from wetwire_aws.linter import (
    fix_code,
    lint_code,
)
from wetwire_aws.linter.rules import (
    InlinePropertyType,
    PropertyTypeAsRef,
)


class TestPropertyTypeAsRef:
    """Tests for WAW011: PropertyType wrappers should use no-parens style."""

    def test_detects_policy_document_wrapper_with_parens(self):
        """Should detect PolicyDocument wrapper used with ()."""
        code = """
@wetwire_aws
class MyPolicyDoc:
    resource: PolicyDocument
    statement = []

@wetwire_aws
class MyRole:
    resource: iam.Role
    assume_role_policy_document = MyPolicyDoc()
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW011"
        assert issues[0].suggestion == "MyPolicyDoc"

    def test_detects_policy_statement_wrapper_with_parens(self):
        """Should detect PolicyStatement wrapper used with ()."""
        code = """
@wetwire_aws
class AllowStatement:
    resource: PolicyStatement
    action = "sts:AssumeRole"

@wetwire_aws
class MyPolicyDoc:
    resource: PolicyDocument
    statement = [AllowStatement()]
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 1
        assert issues[0].suggestion == "AllowStatement"

    def test_detects_nested_property_type_wrapper_with_parens(self):
        """Should detect nested PropertyType wrapper (e.g., s3.Bucket.BucketEncryption) with ()."""
        code = """
@wetwire_aws
class MyBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    sse_algorithm = "AES256"

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
    bucket_encryption = MyBucketEncryption()
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 1
        assert issues[0].suggestion == "MyBucketEncryption"

    def test_ignores_resource_wrappers(self):
        """Should not flag resource wrappers (these are valid as class refs)."""
        code = """
@wetwire_aws
class MyVPC:
    resource: ec2.VPC
    cidr_block = "10.0.0.0/16"

@wetwire_aws
class MySubnet:
    resource: ec2.Subnet
    vpc_id = MyVPC
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 0

    def test_ignores_already_no_parens(self):
        """Should not flag PropertyType wrappers that already use no-parens style."""
        code = """
@wetwire_aws
class MyPolicyDoc:
    resource: PolicyDocument
    statement = []

@wetwire_aws
class MyRole:
    resource: iam.Role
    assume_role_policy_document = MyPolicyDoc
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 0

    def test_detects_multiple_in_list_with_parens(self):
        """Should detect multiple PropertyType wrappers with () in a list."""
        code = """
@wetwire_aws
class AllowStatement1:
    resource: PolicyStatement
    action = "s3:GetObject"

@wetwire_aws
class AllowStatement2:
    resource: PolicyStatement
    action = "s3:PutObject"

@wetwire_aws
class MyPolicyDoc:
    resource: PolicyDocument
    statement = [AllowStatement1(), AllowStatement2()]
"""
        issues = lint_code(code, rules=[PropertyTypeAsRef()])
        assert len(issues) == 2
        assert issues[0].suggestion == "AllowStatement1"
        assert issues[1].suggestion == "AllowStatement2"

    def test_fix_removes_parentheses(self):
        """Should fix by removing () from the wrapper."""
        code = """@wetwire_aws
class MyPolicyDoc:
    resource: PolicyDocument
    statement = []

@wetwire_aws
class MyRole:
    resource: iam.Role
    assume_role_policy_document = MyPolicyDoc()"""
        fixed = fix_code(code, rules=[PropertyTypeAsRef()], add_imports=False)
        assert (
            "assume_role_policy_document = MyPolicyDoc\n" in fixed
            or fixed.strip().endswith("assume_role_policy_document = MyPolicyDoc")
        )


class TestInlinePropertyType:
    """Tests for WAW017: inline property type dicts."""

    def test_detects_bucket_encryption_inline_dict(self):
        """Should detect bucket_encryption = {...} as inline dict.

        Note: Rule only flags dicts with >1 key to avoid simple key-value pairs.
        """
        code = '''bucket_encryption = {"Rules": [], "Enabled": True}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"
        assert "bucket_encryption" in issues[0].message

    def test_detects_versioning_configuration_inline_dict(self):
        """Should detect versioning_configuration = {...} as inline dict."""
        code = '''versioning_configuration = {"Status": "Enabled", "MFADelete": "Disabled"}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"

    def test_ignores_simple_dicts(self):
        """Should not flag simple dicts without property type suffixes."""
        code = '''my_stuff = {"key": "value", "another": "thing"}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 0

    def test_ignores_single_key_dicts(self):
        """Should not flag single-key dicts with empty values."""
        code = '''bucket_encryption = {"Rules": []}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 0

    def test_detects_single_key_dicts_with_complex_values(self):
        """Should flag single-key dicts with complex nested values."""
        code = '''bucket_encryption = {"ServerSideEncryptionConfiguration": [{"SSEAlgorithm": "AES256"}]}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"

    def test_ignores_class_references(self):
        """Should not flag when value is a class reference, not dict."""
        code = '''bucket_encryption = MyEncryptionClass'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 0

    def test_detects_cors_rules_inline_dict(self):
        """Should detect cors_rules = [...] with inline dicts."""
        code = '''cors_rules = [{"AllowedMethods": ["GET"], "AllowedOrigins": ["*"]}]'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"

    def test_detects_server_side_encryption_configuration(self):
        """Should detect server_side_encryption_configuration inline dict."""
        code = '''server_side_encryption_configuration = [{"Rule": {}, "Another": "key"}]'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"

    def test_detects_always_flag_fields(self):
        """Should detect fields in ALWAYS_FLAG set regardless of suffix."""
        code = '''filter = {"Prefix": "logs/", "Tags": []}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert "filter" in issues[0].message

    def test_detects_transition_field(self):
        """Should detect transition field in ALWAYS_FLAG."""
        code = '''transition = {"StorageClass": "GLACIER", "Days": 30}'''
        issues = lint_code(code, rules=[InlinePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW017"
