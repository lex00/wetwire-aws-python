"""Security resources: LambdaIamRole."""

from . import *  # noqa: F403


class LambdaIamRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaIamRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaIamRoleAllowStatement0]


class LambdaIamRoleAllowStatement0_1(PolicyStatement):
    action = ['logs:CreateLogGroup']
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*')


class LambdaIamRoleAllowStatement1(PolicyStatement):
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${LambdaFunctionName}:*')


class LambdaIamRolePolicies0PolicyDocument(PolicyDocument):
    statement = [LambdaIamRoleAllowStatement0_1, LambdaIamRoleAllowStatement1]


class LambdaIamRolePolicy(iam.User.Policy):
    policy_name = 'LambdaApipolicy'
    policy_document = LambdaIamRolePolicies0PolicyDocument


class LambdaIamRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = LambdaIamRoleAssumeRolePolicyDocument
    role_name = 'LambdaRole'
    policies = [LambdaIamRolePolicy]
