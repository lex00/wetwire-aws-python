"""Security resources: LambdaIAMRole."""

from . import *  # noqa: F403


class LambdaIAMRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaIAMRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaIAMRoleAllowStatement0]


class LambdaIAMRoleAllowStatement0_1(PolicyStatement):
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = 'arn:aws:logs:*:*:*'


class LambdaIAMRolePolicies0PolicyDocument(PolicyDocument):
    statement = [LambdaIAMRoleAllowStatement0_1]


class LambdaIAMRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = LambdaIAMRolePolicies0PolicyDocument


class LambdaIAMRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = LambdaIAMRoleAssumeRolePolicyDocument
    path = '/'
    policies = [LambdaIAMRolePolicy]
