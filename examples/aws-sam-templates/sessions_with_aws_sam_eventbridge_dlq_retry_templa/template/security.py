"""Security resources: EBRuleRole, MyHttpApiRole."""

from . import *  # noqa: F403


class EBRuleRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class EBRuleRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EBRuleRoleAllowStatement0]


class EBRuleRolePolicy(iam.User.Policy):
    policy_name = 'InvokeLambda'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['lambda:InvokeFunction'],
            'Effect': 'Allow',
            'Resource': [TriggeredFunction.Arn],
        },
    }


class EBRuleRolePolicy1(iam.User.Policy):
    policy_name = 'WriteToSQS'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['sqs:SendMessage'],
            'Effect': 'Allow',
            'Resource': [DLQueue.Arn],
        },
    }


class EBRuleRole(iam.Role):
    assume_role_policy_document = EBRuleRoleAssumeRolePolicyDocument
    policies = [EBRuleRolePolicy, EBRuleRolePolicy1]


class MyHttpApiRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'apigateway.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class MyHttpApiRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [MyHttpApiRoleAllowStatement0]


class MyHttpApiRolePolicy(iam.User.Policy):
    policy_name = 'ApiDirectWriteEventBridge'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['events:PutEvents'],
            'Effect': 'Allow',
            'Resource': [Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default')],
        },
    }


class MyHttpApiRole(iam.Role):
    assume_role_policy_document = MyHttpApiRoleAssumeRolePolicyDocument
    policies = [MyHttpApiRolePolicy]
