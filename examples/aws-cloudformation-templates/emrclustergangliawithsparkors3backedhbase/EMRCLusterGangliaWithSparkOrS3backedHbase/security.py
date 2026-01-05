"""Security resources: EMRClusterinstanceProfileRole, EMRClusterServiceRole, EMRClusterinstanceProfile."""

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


class EMRClusterinstanceProfileRole:
    resource: iam.Role
    assume_role_policy_document = EMRClusterinstanceProfileRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role']
    path = '/'


class EMRClusterServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['elasticmapreduce.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EMRClusterServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterServiceRoleAllowStatement0]


class EMRClusterServiceRole:
    resource: iam.Role
    assume_role_policy_document = EMRClusterServiceRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole']
    path = '/'


class EMRClusterinstanceProfile:
    resource: iam.InstanceProfile
    path = '/'
    roles = [EMRClusterinstanceProfileRole]
