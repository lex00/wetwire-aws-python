"""Security resources: LambdaIAMRole."""

from . import *  # noqa: F403


class LambdaIAMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0]


class LambdaIAMRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = 'arn:aws:logs:*:*:*'


class LambdaIAMRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0_1]


class LambdaIAMRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'root'
    policy_document = LambdaIAMRolePolicies0PolicyDocument


class LambdaIAMRole:
    resource: iam.Role
    assume_role_policy_document = LambdaIAMRoleAssumeRolePolicyDocument
    path = '/'
    policies = [LambdaIAMRolePolicy]
