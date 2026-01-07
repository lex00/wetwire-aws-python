"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class VPCCidrBlock(Parameter):
    type = STRING
    default = '10.0.0.0/16'


class PublicCidrBlock1(Parameter):
    type = STRING
    default = '10.0.1.0/24'


class PublicCidrBlock2(Parameter):
    type = STRING
    default = '10.0.2.0/24'


class PublicCidrBlock3(Parameter):
    type = STRING
    default = '10.0.3.0/24'


class PrivateCidrBlock1(Parameter):
    type = STRING
    default = '10.0.4.0/24'


class PrivateCidrBlock2(Parameter):
    type = STRING
    default = '10.0.5.0/24'


class PrivateCidrBlock3(Parameter):
    type = STRING
    default = '10.0.6.0/24'


class EKSClusterVersion(Parameter):
    type = STRING


class NodeGroupInstanceTypes(Parameter):
    type = STRING
    default = 't3.medium'


class ServicePrincipalPartitionMapMapping(Mapping):
    map_data = {
        'aws': {
            'EC2': 'ec2.amazonaws.com',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
        'aws-cn': {
            'EC2': 'ec2.amazonaws.com.cn',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
        'aws-us-gov': {
            'EC2': 'ec2.amazonaws.com',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
    }
