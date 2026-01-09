"""Tests for the graph module."""

import subprocess
import sys


class TestGraph:
    """Tests for Graph class."""

    def test_graph_from_registry_empty(self):
        """Test graph from empty registry."""
        from wetwire_aws.graph import Graph

        graph = Graph()
        assert graph.nodes == {}
        assert graph.edges == []

    def test_graph_to_dot_basic(self):
        """Test basic DOT output."""
        from wetwire_aws.graph import EdgeType, Graph

        graph = Graph()
        graph.nodes = {
            "MyBucket": "AWS::S3::Bucket",
            "MyFunction": "AWS::Lambda::Function",
        }
        graph.edges = [("MyFunction", "MyBucket", EdgeType.REF)]

        dot = graph.to_dot()
        assert "digraph" in dot
        assert "MyBucket" in dot
        assert "MyFunction" in dot
        assert "AWS::S3::Bucket" in dot
        assert "->" in dot

    def test_graph_to_dot_getatt_edge(self):
        """Test GetAtt edges have different style."""
        from wetwire_aws.graph import EdgeType, Graph

        graph = Graph()
        graph.nodes = {
            "MyRole": "AWS::IAM::Role",
            "MyFunction": "AWS::Lambda::Function",
        }
        graph.edges = [("MyFunction", "MyRole", EdgeType.GETATT)]

        dot = graph.to_dot()
        assert "color=" in dot or "style=" in dot  # GetAtt edge styled differently

    def test_graph_to_dot_clustered(self):
        """Test clustered output groups by service."""
        from wetwire_aws.graph import Graph

        graph = Graph()
        graph.nodes = {
            "Bucket1": "AWS::S3::Bucket",
            "Bucket2": "AWS::S3::Bucket",
            "Function1": "AWS::Lambda::Function",
        }
        graph.edges = []

        dot = graph.to_dot(cluster_by_service=True)
        assert "subgraph cluster_S3" in dot
        assert "subgraph cluster_Lambda" in dot

    def test_graph_to_mermaid_basic(self):
        """Test basic Mermaid output."""
        from wetwire_aws.graph import EdgeType, Graph

        graph = Graph()
        graph.nodes = {
            "MyBucket": "AWS::S3::Bucket",
            "MyFunction": "AWS::Lambda::Function",
        }
        graph.edges = [("MyFunction", "MyBucket", EdgeType.REF)]

        mermaid = graph.to_mermaid()
        assert "graph TD" in mermaid
        assert "MyBucket" in mermaid
        assert "MyFunction" in mermaid
        assert "-->" in mermaid

    def test_graph_to_mermaid_getatt(self):
        """Test Mermaid GetAtt edges have label."""
        from wetwire_aws.graph import EdgeType, Graph

        graph = Graph()
        graph.nodes = {
            "MyRole": "AWS::IAM::Role",
            "MyFunction": "AWS::Lambda::Function",
        }
        graph.edges = [("MyFunction", "MyRole", EdgeType.GETATT)]

        mermaid = graph.to_mermaid()
        assert "|GetAtt|" in mermaid

    def test_graph_group_by_service(self):
        """Test grouping resources by AWS service."""
        from wetwire_aws.graph import Graph

        graph = Graph()
        graph.nodes = {
            "Bucket1": "AWS::S3::Bucket",
            "Bucket2": "AWS::S3::Bucket",
            "Function1": "AWS::Lambda::Function",
            "Role1": "AWS::IAM::Role",
        }

        groups = graph._group_by_service()
        assert "S3" in groups
        assert "Lambda" in groups
        assert "IAM" in groups
        assert len(groups["S3"]) == 2
        assert len(groups["Lambda"]) == 1


class TestGraphCLI:
    """Tests for graph CLI command."""

    def test_graph_command_help(self):
        """Test graph command shows help."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "graph", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "graph" in result.stdout.lower()

    def test_graph_command_with_package(self, tmp_path):
        """Test graph command with a simple package."""
        # Create a simple test package
        pkg_dir = tmp_path / "test_pkg"
        pkg_dir.mkdir()

        init_content = '''
from wetwire_aws.loader import setup_resources
setup_resources(__file__, __name__, globals())
'''
        (pkg_dir / "__init__.py").write_text(init_content)

        resources_content = '''
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "test-bucket"

class MyFunction(lambda_.Function):
    function_name = "test-function"
    role = MyRole.Arn

class MyRole(iam.Role):
    role_name = "test-role"
    assume_role_policy_document = {"Version": "2012-10-17"}
'''
        (pkg_dir / "resources.py").write_text(resources_content)

        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "graph", str(pkg_dir)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "digraph" in result.stdout
        assert "MyBucket" in result.stdout
        assert "MyFunction" in result.stdout
        assert "MyRole" in result.stdout

    def test_graph_command_mermaid_format(self, tmp_path):
        """Test graph command with mermaid format."""
        pkg_dir = tmp_path / "test_pkg"
        pkg_dir.mkdir()

        init_content = '''
from wetwire_aws.loader import setup_resources
setup_resources(__file__, __name__, globals())
'''
        (pkg_dir / "__init__.py").write_text(init_content)

        resources_content = '''
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "test-bucket"
'''
        (pkg_dir / "resources.py").write_text(resources_content)

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "wetwire_aws.cli",
                "graph",
                str(pkg_dir),
                "-f",
                "mermaid",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "graph TD" in result.stdout
