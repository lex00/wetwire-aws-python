"""Security resources: LambdaRole."""

from . import *  # noqa: F403


class LambdaRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaRoleAllowStatement0]


class LambdaRole(iam.Role):
    role_name = 'lambda-role'
    assume_role_policy_document = LambdaRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/AWSLambdaExecute', 'arn:aws:iam::aws:policy/AmazonS3FullAccess', 'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess', 'arn:aws:iam::aws:policy/AmazonKinesisFullAccess']
    path = '/'
