"""Security resources: LambdaExecutionRole, GreengrassResourceRole."""

from . import *  # noqa: F403


class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'lambda.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


class LambdaExecutionRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement2:
    resource: PolicyStatement
    action = ['greengrass:*']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement3:
    resource: PolicyStatement
    action = ['ec2:DescribeReservedInstancesOfferings']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement4:
    resource: PolicyStatement
    action = [
        'iam:CreateRole',
        'iam:AttachRolePolicy',
        'iam:GetRole',
        'iam:DeleteRole',
        'iam:PassRole',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/greengrass_cfn_${AWS::StackName}_ServiceRole')


class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1, LambdaExecutionRoleAllowStatement1, LambdaExecutionRoleAllowStatement2, LambdaExecutionRoleAllowStatement3, LambdaExecutionRoleAllowStatement4]


class LambdaExecutionRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


class LambdaExecutionRole:
    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]


class GreengrassResourceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'greengrass.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class GreengrassResourceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0]


class GreengrassResourceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


class GreengrassResourceRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


class GreengrassResourceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0_1, GreengrassResourceRoleAllowStatement1]


class GreengrassResourceRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'root'
    policy_document = GreengrassResourceRolePolicies0PolicyDocument


class GreengrassResourceRole:
    resource: iam.Role
    assume_role_policy_document = GreengrassResourceRoleAssumeRolePolicyDocument
    policies = [GreengrassResourceRolePolicy]
