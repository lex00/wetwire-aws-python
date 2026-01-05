"""Security resources: EMRClusterinstanceProfileRole, EMRClusterinstanceProfile, EMRClusterServiceRole."""

from . import *  # noqa: F403


class EMRClusterinstanceProfileRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EMRClusterinstanceProfileRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterinstanceProfileRoleAllowStatement0]


class EMRClusterinstanceProfileRole(iam.Role):
    assume_role_policy_document = EMRClusterinstanceProfileRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role']
    path = '/'


class EMRClusterinstanceProfile(iam.InstanceProfile):
    path = '/'
    roles = [EMRClusterinstanceProfileRole]


class EMRClusterServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['elasticmapreduce.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EMRClusterServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterServiceRoleAllowStatement0]


class EMRClusterServiceRole(iam.Role):
    assume_role_policy_document = EMRClusterServiceRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole']
    path = '/'
