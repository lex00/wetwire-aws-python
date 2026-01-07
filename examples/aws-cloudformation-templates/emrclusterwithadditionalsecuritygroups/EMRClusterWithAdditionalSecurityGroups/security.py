"""Security resources: EMRClusterinstanceProfileRole, EMRClusterinstanceProfile, EMRClusterServiceRole."""

from . import *  # noqa: F403


class EMRClusterinstanceProfileRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EMRClusterinstanceProfileRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EMRClusterinstanceProfileRoleAllowStatement0]


class EMRClusterinstanceProfileRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = EMRClusterinstanceProfileRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role']
    path = '/'


class EMRClusterinstanceProfile(iam.InstanceProfile):
    resource: iam.InstanceProfile
    path = '/'
    roles = [EMRClusterinstanceProfileRole]


class EMRClusterServiceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['elasticmapreduce.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EMRClusterServiceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EMRClusterServiceRoleAllowStatement0]


class EMRClusterServiceRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = EMRClusterServiceRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole']
    path = '/'
