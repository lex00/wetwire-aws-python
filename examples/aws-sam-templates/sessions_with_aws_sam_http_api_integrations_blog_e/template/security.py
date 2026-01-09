"""Security resources: MyHttpApiRole."""

from . import *  # noqa: F403


class MyHttpApiRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'apigateway.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class MyHttpApiRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [MyHttpApiRoleAllowStatement0]


class MyHttpApiRolePolicy(iam.User.Policy):
    policy_name = 'ApiDirectWriteToSQS'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['sqs:SendMessage'],
            'Effect': 'Allow',
            'Resource': [MyQueue.Arn],
        },
    }


class MyHttpApiRole(iam.Role):
    assume_role_policy_document = MyHttpApiRoleAssumeRolePolicyDocument
    policies = [MyHttpApiRolePolicy]
