"""Tests for file splitting utilities in linter/splitting.py."""


class TestSplittingUtilities:
    """Tests for file splitting utilities in linter/splitting.py."""

    def test_categorize_s3_as_storage(self):
        """S3 resources should categorize as storage."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::S3::Bucket") == "storage"

    def test_categorize_ec2_instance_as_compute(self):
        """EC2 Instance should categorize as compute."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::EC2::Instance") == "compute"

    def test_categorize_ec2_vpc_as_network(self):
        """EC2 VPC should categorize as network (not compute)."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::EC2::VPC") == "network"
        assert categorize_resource_type("AWS::EC2::Subnet") == "network"
        assert categorize_resource_type("AWS::EC2::SecurityGroup") == "network"

    def test_categorize_iam_as_security(self):
        """IAM resources should categorize as security."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::IAM::Role") == "security"

    def test_categorize_unknown_as_main(self):
        """Unknown resources should categorize as main."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::Unknown::Resource") == "main"
        assert categorize_resource_type("InvalidFormat") == "main"

    def test_is_ec2_network_type_core_types(self):
        """Core network types should be detected."""
        from wetwire_aws.linter.splitting import is_ec2_network_type

        assert is_ec2_network_type("VPC") is True
        assert is_ec2_network_type("Subnet") is True
        assert is_ec2_network_type("SecurityGroup") is True
        assert is_ec2_network_type("SecurityGroupIngress") is True
        assert is_ec2_network_type("SecurityGroupEgress") is True
        assert is_ec2_network_type("RouteTable") is True
        assert is_ec2_network_type("NetworkInterface") is True

    def test_is_ec2_network_type_compute_types(self):
        """Compute types should NOT be detected as network."""
        from wetwire_aws.linter.splitting import is_ec2_network_type

        assert is_ec2_network_type("Instance") is False
        assert is_ec2_network_type("LaunchTemplate") is False
        assert is_ec2_network_type("Volume") is False
        assert is_ec2_network_type("Snapshot") is False
        assert is_ec2_network_type("KeyPair") is False
        assert is_ec2_network_type("SpotFleet") is False

    def test_is_ec2_network_type_endpoint_types(self):
        """Endpoint types should be detected as network."""
        from wetwire_aws.linter.splitting import is_ec2_network_type

        assert is_ec2_network_type("VPCEndpoint") is True
        assert is_ec2_network_type("VPCEndpointService") is True
        assert is_ec2_network_type("ClientVpnEndpoint") is True

    def test_is_ec2_network_type_new_types(self):
        """Newly-added network types should be detected dynamically."""
        from wetwire_aws.linter.splitting import is_ec2_network_type

        # These were previously missing from the static list
        assert is_ec2_network_type("TransitGatewayRouteTable") is True
        assert is_ec2_network_type("TrafficMirrorSession") is True
        assert is_ec2_network_type("TrafficMirrorTarget") is True
        assert is_ec2_network_type("PrefixList") is True
        assert is_ec2_network_type("VerifiedAccessEndpoint") is True
        assert is_ec2_network_type("LocalGatewayRouteTable") is True

    def test_categorize_ec2_security_group_ingress(self):
        """SecurityGroupIngress should categorize as network via dynamic inference."""
        from wetwire_aws.linter.splitting import categorize_resource_type

        assert categorize_resource_type("AWS::EC2::SecurityGroupIngress") == "network"
        assert categorize_resource_type("AWS::EC2::SecurityGroupEgress") == "network"

    def test_suggest_file_splits_basic(self):
        """Test basic file splitting suggestion."""
        from wetwire_aws.linter.splitting import ResourceInfo, suggest_file_splits

        resources = [
            ResourceInfo("MyBucket", "AWS::S3::Bucket", set()),
            ResourceInfo("MyVPC", "AWS::EC2::VPC", set()),
            ResourceInfo("MyRole", "AWS::IAM::Role", set()),
        ]

        splits = suggest_file_splits(resources)

        assert "storage" in splits
        assert "MyBucket" in splits["storage"]
        assert "network" in splits
        assert "MyVPC" in splits["network"]
        assert "security" in splits
        assert "MyRole" in splits["security"]

    def test_suggest_file_splits_respects_max(self):
        """Test that file splits respect max_per_file."""
        from wetwire_aws.linter.splitting import ResourceInfo, suggest_file_splits

        # Create 20 S3 buckets
        resources = [
            ResourceInfo(f"Bucket{i}", "AWS::S3::Bucket", set()) for i in range(20)
        ]

        # With max 15, should split into storage1, storage2
        splits = suggest_file_splits(resources, max_per_file=15)

        assert "storage1" in splits or "storage2" in splits
        total_resources = sum(len(v) for v in splits.values())
        assert total_resources == 20

    def test_calculate_scc_weight(self):
        """Test SCC weight calculation."""
        from wetwire_aws.linter.splitting import (
            ResourceInfo,
            calculate_scc_weight,
        )

        resources = {
            "A": ResourceInfo("A", "AWS::S3::Bucket", {"B", "C"}),
            "B": ResourceInfo("B", "AWS::S3::Bucket", {"A"}),
            "C": ResourceInfo("C", "AWS::S3::Bucket", set()),
        }

        # A->B, B->A = 2 internal edges
        weight = calculate_scc_weight(["A", "B"], resources)
        assert weight == 2  # A depends on B, B depends on A
