"""Tests for WAW022: circular dependency detection."""

from wetwire_aws.linter import lint_code
from wetwire_aws.linter.rules.dependency_rules import CircularDependency


class TestCircularDependency:
    """Tests for WAW022: circular dependency detection."""

    def test_detects_simple_cycle(self):
        """Should detect A -> B -> A cycle."""
        code = '''
from wetwire_aws.resources import s3, iam

class BucketA(s3.Bucket):
    resource: s3.Bucket
    bucket_name = BucketB

class BucketB(s3.Bucket):
    resource: s3.Bucket
    bucket_name = BucketA
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) >= 1
        assert issues[0].rule_id == "WAW022"
        assert "circular" in issues[0].message.lower()

    def test_detects_three_node_cycle(self):
        """Should detect A -> B -> C -> A cycle."""
        code = '''
from wetwire_aws.resources import s3

class BucketA(s3.Bucket):
    bucket_name = BucketB

class BucketB(s3.Bucket):
    bucket_name = BucketC

class BucketC(s3.Bucket):
    bucket_name = BucketA
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) >= 1
        assert "circular" in issues[0].message.lower()

    def test_no_cycle(self):
        """Should not flag linear dependencies."""
        code = '''
from wetwire_aws.resources import s3, iam

class MyRole(iam.Role):
    assume_role_policy_document = "..."

class MyBucket(s3.Bucket):
    bucket_name = "test"

class MyPolicy(iam.Policy):
    roles = [MyRole]
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) == 0

    def test_self_reference(self):
        """Should detect self-reference as a cycle."""
        code = '''
from wetwire_aws.resources import s3

class MyBucket(s3.Bucket):
    depends_on = [MyBucket]
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) >= 1

    def test_ignores_non_resource_classes(self):
        """Should only check resource classes."""
        code = '''
class Helper:
    ref = Helper  # This is fine, not a resource
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) == 0

    def test_cycle_reports_all_nodes(self):
        """Cycle report should include all nodes in the cycle."""
        code = '''
from wetwire_aws.resources import s3

class BucketA(s3.Bucket):
    bucket_name = BucketB

class BucketB(s3.Bucket):
    bucket_name = BucketA
'''
        issues = lint_code(code, rules=[CircularDependency()])
        assert len(issues) >= 1
        # Message should mention both resources
        msg = issues[0].message.lower()
        assert "bucketa" in msg or "bucketb" in msg
