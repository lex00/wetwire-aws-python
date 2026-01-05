"""Security resources: MyLambdaRole."""

from . import *  # noqa: F403


class MyLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class MyLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [MyLambdaRoleAllowStatement0]


class MyLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:CreateLogGroup']
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*')


class MyLambdaRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${AWS::StackName}:*')


class MyLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [MyLambdaRoleAllowStatement0_1, MyLambdaRoleAllowStatement1]


class MyLambdaRolePolicy:
    resource: iam.User.Policy
    policy_name = AWS_STACK_NAME
    policy_document = MyLambdaRolePolicies0PolicyDocument


class MyLambdaRole:
    resource: iam.Role
    assume_role_policy_document = MyLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [MyLambdaRolePolicy]
