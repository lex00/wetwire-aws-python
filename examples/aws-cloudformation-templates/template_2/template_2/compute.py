"""Compute resources: ControlPlane, LaunchTemplate, ManagedNodeGroup."""

from . import *  # noqa: F403


class ControlPlaneResourcesVpcConfig(eks.Cluster.ResourcesVpcConfig):
    security_group_ids = [ControlPlaneSecurityGroup]
    subnet_ids = [PublicSubnet1, PublicSubnet2, PublicSubnet3, PrivateSubnet1, PrivateSubnet2, PrivateSubnet3]


class ControlPlane(eks.Cluster):
    name = Sub('${AWS::StackName}-cluster')
    resources_vpc_config = ControlPlaneResourcesVpcConfig
    role_arn = EKSClusterRole.Arn
    version = EKSClusterVersion


class LaunchTemplateEbs(ec2.LaunchTemplate.Ebs):
    iops = 3000
    throughput = 125
    volume_size = 80
    volume_type = 'gp3'


class LaunchTemplateBlockDeviceMapping(ec2.LaunchTemplate.BlockDeviceMapping):
    device_name = '/dev/xvda'
    ebs = LaunchTemplateEbs


class LaunchTemplateMetadataOptions(ec2.LaunchTemplate.MetadataOptions):
    http_put_response_hop_limit = 2
    http_tokens = 'optional'


class LaunchTemplateTagSpecification(ec2.LaunchTemplate.TagSpecification):
    resource_type = 'instance'
    tags = [{
        'Key': 'Name',
        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-name',
        'Value': Sub('ng-${AWS::StackName}'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-type',
        'Value': 'managed',
    }]


class LaunchTemplateTagSpecification1(ec2.LaunchTemplate.TagSpecification):
    resource_type = 'volume'
    tags = [{
        'Key': 'Name',
        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-name',
        'Value': Sub('ng-${AWS::StackName}'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-type',
        'Value': 'managed',
    }]


class LaunchTemplateTagSpecification2(ec2.LaunchTemplate.TagSpecification):
    resource_type = 'network-interface'
    tags = [{
        'Key': 'Name',
        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-name',
        'Value': Sub('ng-${AWS::StackName}'),
    }, {
        'Key': 'alpha.eksctl.io/nodegroup-type',
        'Value': 'managed',
    }]


class LaunchTemplateLaunchTemplateData(ec2.LaunchTemplate.LaunchTemplateData):
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    metadata_options = LaunchTemplateMetadataOptions
    security_group_ids = [ControlPlaneSecurityGroup]
    tag_specifications = [LaunchTemplateTagSpecification, LaunchTemplateTagSpecification1, LaunchTemplateTagSpecification2]


class LaunchTemplate(ec2.LaunchTemplate):
    launch_template_data = LaunchTemplateLaunchTemplateData
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')


class ManagedNodeGroupSsoIdentity(eks.Capability.SsoIdentity):
    id = LaunchTemplate


class ManagedNodeGroupScalingConfig(eks.Nodegroup.ScalingConfig):
    desired_size = 2
    max_size = 2
    min_size = 2


class ManagedNodeGroup(eks.Nodegroup):
    ami_type = 'AL2_x86_64'
    cluster_name = ControlPlane
    instance_types = [NodeGroupInstanceTypes]
    labels = {
        'alpha.eksctl.io/cluster-name': ControlPlane,
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
    }
    launch_template = ManagedNodeGroupSsoIdentity
    node_role = NodeInstanceRole.Arn
    nodegroup_name = Sub('ng-${AWS::StackName}')
    scaling_config = ManagedNodeGroupScalingConfig
    subnets = [PrivateSubnet1, PrivateSubnet2, PrivateSubnet3]
    tags = {
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
        'alpha.eksctl.io/nodegroup-type': 'managed',
    }
