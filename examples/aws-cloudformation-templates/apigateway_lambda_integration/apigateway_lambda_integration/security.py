"""Security resources: LambdaIamRole."""

from . import *  # noqa: F403


class LambdaIamRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaIamRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIamRoleAllowStatement0]


class LambdaIamRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:CreateLogGroup']
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*')


class LambdaIamRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${LambdaFunctionName}:*')


class LambdaIamRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIamRoleAllowStatement0_1, LambdaIamRoleAllowStatement1]


class LambdaIamRolePolicy:
    resource: iam.User.Policy
    policy_name = 'LambdaApipolicy'
    policy_document = LambdaIamRolePolicies0PolicyDocument


class LambdaIamRole(iam.Role):
    assume_role_policy_document = LambdaIamRoleAssumeRolePolicyDocument
    role_name = 'LambdaRole'
    policies = [LambdaIamRolePolicy]
