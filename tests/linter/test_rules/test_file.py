"""Tests for file-level rules.

Rules:
    WAW010: Split large files
    WAW012: Detect duplicate resource class names
"""

from wetwire_aws.linter import (
    DuplicateResource,
    FileTooLarge,
    lint_code,
)


class TestFileTooLarge:
    """Tests for WAW010: file size limit."""

    def test_detects_file_over_limit(self):
        """Should detect files with > 15 @wetwire_aws classes."""
        # Generate code with 16 classes
        classes = "\n\n".join(
            f"@wetwire_aws\nclass Resource{i}:\n    resource: ec2.Instance"
            for i in range(16)
        )
        code = f"from . import *\n\n{classes}"

        issues = lint_code(code, rules=[FileTooLarge()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW010"
        assert "16 resources" in issues[0].message
        assert "max 15" in issues[0].message

    def test_allows_file_at_limit(self):
        """Should not flag files with exactly 15 resources."""
        classes = "\n\n".join(
            f"@wetwire_aws\nclass Resource{i}:\n    resource: ec2.Instance"
            for i in range(15)
        )
        code = f"from . import *\n\n{classes}"

        issues = lint_code(code, rules=[FileTooLarge()])
        assert len(issues) == 0

    def test_allows_small_files(self):
        """Should not flag small files."""
        code = """from . import *

@wetwire_aws
class MyBucket:
    resource: s3.Bucket

@wetwire_aws
class MyRole:
    resource: iam.Role
"""
        issues = lint_code(code, rules=[FileTooLarge()])
        assert len(issues) == 0

    def test_ignores_non_wetwire_classes(self):
        """Should only count @wetwire_aws decorated classes."""
        code = """from . import *

class HelperClass:
    pass

@dataclass
class DataClass:
    field: str

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
"""
        issues = lint_code(code, rules=[FileTooLarge()])
        assert len(issues) == 0


class TestDuplicateResource:
    """Tests for WAW012: duplicate resource class names."""

    def test_detects_duplicate_class_names(self):
        """Should detect duplicate @wetwire_aws class names in same file."""
        code = """
@wetwire_aws
class MyBucket:
    resource: s3.Bucket
    bucket_name = "bucket-1"

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
    bucket_name = "bucket-2"
"""
        issues = lint_code(code, rules=[DuplicateResource()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW012"
        assert "Duplicate resource class 'MyBucket'" in issues[0].message
        assert "first defined at line" in issues[0].message

    def test_detects_multiple_duplicates(self):
        """Should detect all duplicate definitions."""
        code = """
@wetwire_aws
class MyBucket:
    resource: s3.Bucket

@wetwire_aws
class MyBucket:
    resource: s3.Bucket

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
"""
        issues = lint_code(code, rules=[DuplicateResource()])
        assert len(issues) == 2  # Two duplicates (first is the original)

    def test_ignores_unique_classes(self):
        """Should not flag unique class names."""
        code = """
@wetwire_aws
class MyBucket:
    resource: s3.Bucket

@wetwire_aws
class MyVPC:
    resource: ec2.VPC

@wetwire_aws
class MyRole:
    resource: iam.Role
"""
        issues = lint_code(code, rules=[DuplicateResource()])
        assert len(issues) == 0

    def test_ignores_non_wetwire_classes(self):
        """Should not flag non-wetwire_aws classes with same name."""
        code = """
class MyBucket:
    pass

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
"""
        issues = lint_code(code, rules=[DuplicateResource()])
        assert len(issues) == 0

    def test_reports_correct_line_numbers(self):
        """Should report correct line numbers for duplicate definitions."""
        code = """
@wetwire_aws
class MyBucket:
    resource: s3.Bucket

@wetwire_aws
class OtherResource:
    resource: ec2.VPC

@wetwire_aws
class MyBucket:
    resource: s3.Bucket
"""
        issues = lint_code(code, rules=[DuplicateResource()])
        assert len(issues) == 1
        assert issues[0].line == 11  # Line of second MyBucket definition
        assert "first defined at line 3" in issues[0].message
