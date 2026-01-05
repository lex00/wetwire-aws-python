"""Security resources: RootRole, PrivateProfile, BastionProfile."""

from . import *  # noqa: F403


class RootRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class RootRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0]


class RootRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'cloudformation:*'
    resource_arn = '*'


class RootRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0_1]


class RootRolePolicy:
    resource: iam.User.Policy
    policy_name = 'root'
    policy_document = RootRolePolicies0PolicyDocument


class RootRole(iam.Role):
    assume_role_policy_document = RootRoleAssumeRolePolicyDocument
    path = '/'
    policies = [RootRolePolicy]


class PrivateProfile(iam.InstanceProfile):
    path = '/'
    roles = [RootRole]


class BastionProfile(iam.InstanceProfile):
    path = '/'
    roles = [RootRole]
