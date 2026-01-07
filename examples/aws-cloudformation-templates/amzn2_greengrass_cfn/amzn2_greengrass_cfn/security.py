"""Security resources: LambdaExecutionRole, GreengrassResourceRole."""

from . import *  # noqa: F403


class LambdaExecutionRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'lambda.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class LambdaExecutionRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaExecutionRoleAllowStatement0]


class LambdaExecutionRoleAllowStatement0_1(PolicyStatement):
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


class LambdaExecutionRoleAllowStatement1(PolicyStatement):
    action = ['iot:*']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement2(PolicyStatement):
    action = ['greengrass:*']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement3(PolicyStatement):
    action = ['ec2:DescribeReservedInstancesOfferings']
    resource_arn = '*'


class LambdaExecutionRoleAllowStatement4(PolicyStatement):
    action = [
        'iam:CreateRole',
        'iam:AttachRolePolicy',
        'iam:GetRole',
        'iam:DeleteRole',
        'iam:PassRole',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/greengrass_cfn_${AWS::StackName}_ServiceRole')


class LambdaExecutionRolePolicies0PolicyDocument(PolicyDocument):
    statement = [LambdaExecutionRoleAllowStatement0_1, LambdaExecutionRoleAllowStatement1, LambdaExecutionRoleAllowStatement2, LambdaExecutionRoleAllowStatement3, LambdaExecutionRoleAllowStatement4]


class LambdaExecutionRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


class LambdaExecutionRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]


class GreengrassResourceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'greengrass.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class GreengrassResourceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [GreengrassResourceRoleAllowStatement0]


class GreengrassResourceRoleAllowStatement0_1(PolicyStatement):
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


class GreengrassResourceRoleAllowStatement1(PolicyStatement):
    action = ['iot:*']
    resource_arn = '*'


class GreengrassResourceRolePolicies0PolicyDocument(PolicyDocument):
    statement = [GreengrassResourceRoleAllowStatement0_1, GreengrassResourceRoleAllowStatement1]


class GreengrassResourceRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = GreengrassResourceRolePolicies0PolicyDocument


class GreengrassResourceRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = GreengrassResourceRoleAssumeRolePolicyDocument
    policies = [GreengrassResourceRolePolicy]
