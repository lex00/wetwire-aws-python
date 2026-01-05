"""Security resources: InstanceRole, InstanceProfile."""

from . import *  # noqa: F403


class InstanceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class InstanceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [InstanceRoleAllowStatement0]


class InstanceRoleAllowStatement0_1(PolicyStatement):
    action = [
        'ec2:Describe*',
        'ec2:CreateTags',
    ]
    resource_arn = '*'


class InstanceRolePolicies0PolicyDocument(PolicyDocument):
    statement = [InstanceRoleAllowStatement0_1]


class InstanceRolePolicy(iam.User.Policy):
    policy_name = 'taginstancepolicy'
    policy_document = InstanceRolePolicies0PolicyDocument


class InstanceRole(iam.Role):
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [InstanceRolePolicy]


class InstanceProfile(iam.InstanceProfile):
    path = '/'
    roles = [InstanceRole]
