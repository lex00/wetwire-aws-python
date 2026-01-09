"""Security resources: httpApiRole."""

from . import *  # noqa: F403


class httpApiRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'apigateway.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class httpApiRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [httpApiRoleAllowStatement0]


class httpApiRolePolicy(iam.User.Policy):
    policy_name = 'ApiDirectWriteToSQS'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['states:StartSyncExecution'],
            'Effect': 'Allow',
            'Resource': [urlStateMachine],
        },
    }


class httpApiRole(iam.Role):
    assume_role_policy_document = httpApiRoleAssumeRolePolicyDocument
    policies = [httpApiRolePolicy]
