"""Security resources: LambdaExecutionRole, ConfigRole."""

from . import *  # noqa: F403


class LambdaExecutionRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaExecutionRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaExecutionRoleAllowStatement0]


class LambdaExecutionRoleAllowStatement0_1(PolicyStatement):
    action = [
        'logs:*',
        'config:PutEvaluations',
        'ec2:DescribeVolumeAttribute',
    ]
    resource_arn = '*'


class LambdaExecutionRolePolicies0PolicyDocument(PolicyDocument):
    statement = [LambdaExecutionRoleAllowStatement0_1]


class LambdaExecutionRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


class LambdaExecutionRole(iam.Role):
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]


class ConfigRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['config.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ConfigRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ConfigRoleAllowStatement0]


class ConfigRoleAllowStatement0_1(PolicyStatement):
    action = 's3:GetBucketAcl'
    resource_arn = Join('', [
    'arn:aws:s3:::',
    ConfigBucket,
])


class ConfigRoleAllowStatement1(PolicyStatement):
    action = 's3:PutObject'
    resource_arn = Join('', [
    'arn:aws:s3:::',
    ConfigBucket,
    '/AWSLogs/',
    AWS_ACCOUNT_ID,
    '/*',
])
    condition = {
        STRING_EQUALS: {
            's3:x-amz-acl': 'bucket-owner-full-control',
        },
    }


class ConfigRoleAllowStatement2(PolicyStatement):
    action = 'config:Put*'
    resource_arn = '*'


class ConfigRolePolicies0PolicyDocument(PolicyDocument):
    statement = [ConfigRoleAllowStatement0_1, ConfigRoleAllowStatement1, ConfigRoleAllowStatement2]


class ConfigRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = ConfigRolePolicies0PolicyDocument


class ConfigRole(iam.Role):
    assume_role_policy_document = ConfigRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWS_ConfigRole']
    policies = [ConfigRolePolicy]
