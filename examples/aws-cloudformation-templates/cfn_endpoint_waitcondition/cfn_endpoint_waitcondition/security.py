"""Security resources: RootRole, PrivateProfile, BastionProfile."""

from . import *  # noqa: F403


class RootRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class RootRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [RootRoleAllowStatement0]


class RootRoleAllowStatement0_1(PolicyStatement):
    action = 'cloudformation:*'
    resource_arn = '*'


class RootRolePolicies0PolicyDocument(PolicyDocument):
    statement = [RootRoleAllowStatement0_1]


class RootRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = RootRolePolicies0PolicyDocument


class RootRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = RootRoleAssumeRolePolicyDocument
    path = '/'
    policies = [RootRolePolicy]


class PrivateProfile(iam.InstanceProfile):
    resource: iam.InstanceProfile
    path = '/'
    roles = [RootRole]


class BastionProfile(iam.InstanceProfile):
    resource: iam.InstanceProfile
    path = '/'
    roles = [RootRole]
