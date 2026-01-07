"""Security resources: IAMAssumeInstanceRole, InstanceProfile."""

from . import *  # noqa: F403


class IAMAssumeInstanceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class IAMAssumeInstanceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [IAMAssumeInstanceRoleAllowStatement0]


class IAMAssumeInstanceRoleAllowStatement0_1(PolicyStatement):
    action = ['ec2:DescribeTags']
    resource_arn = '*'


class IAMAssumeInstanceRoleAllowStatement1(PolicyStatement):
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = '*'


class IAMAssumeInstanceRoleAllowStatement2(PolicyStatement):
    action = 'logs:*'
    resource_arn = '*'


class IAMAssumeInstanceRolePolicies0PolicyDocument(PolicyDocument):
    statement = [IAMAssumeInstanceRoleAllowStatement0_1, IAMAssumeInstanceRoleAllowStatement1, IAMAssumeInstanceRoleAllowStatement2]


class IAMAssumeInstanceRolePolicy(iam.User.Policy):
    policy_document = IAMAssumeInstanceRolePolicies0PolicyDocument
    policy_name = Join('-', [
    'IAM',
    'EC2',
    'Policy',
])


class IAMAssumeInstanceRole(iam.Role):
    assume_role_policy_document = IAMAssumeInstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [IAMAssumeInstanceRolePolicy]
    role_name = Join('-', [
    'IAM',
    'EC2',
    'Role',
])


class InstanceProfile(iam.InstanceProfile):
    instance_profile_name = Join('-', [
    'IAM',
    'InstanceProfile',
])
    path = '/'
    roles = [IAMAssumeInstanceRole]
