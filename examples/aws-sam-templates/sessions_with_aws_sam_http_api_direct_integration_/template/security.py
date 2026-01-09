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


class MyHttpApiRolePolicy1(iam.User.Policy):
    policy_name = 'ApiDirectWriteEventBridge'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['events:PutEvents'],
            'Effect': 'Allow',
            'Resource': [Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default')],
        },
    }


class MyHttpApiRolePolicy2(iam.User.Policy):
    policy_name = 'ApiDirectWriteKinesis'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['kinesis:PutRecord'],
            'Effect': 'Allow',
            'Resource': [MyStream.Arn],
        },
    }


class MyHttpApiRole(iam.Role):
    assume_role_policy_document = MyHttpApiRoleAssumeRolePolicyDocument
    policies = [MyHttpApiRolePolicy, MyHttpApiRolePolicy1, MyHttpApiRolePolicy2]
