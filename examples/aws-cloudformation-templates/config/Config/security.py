"""Security resources: ConfigRole, LambdaExecutionRole."""

from . import *  # noqa: F403


class ConfigRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['config.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ConfigRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ConfigRoleAllowStatement0]


class ConfigRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetBucketAcl'
    resource_arn = Join('', [
    'arn:aws:s3:::',
    ConfigBucket,
])


class ConfigRoleAllowStatement1:
    resource: PolicyStatement
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


class ConfigRoleAllowStatement2:
    resource: PolicyStatement
    action = 'config:Put*'
    resource_arn = '*'


class ConfigRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ConfigRoleAllowStatement0_1, ConfigRoleAllowStatement1, ConfigRoleAllowStatement2]


class ConfigRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'root'
    policy_document = ConfigRolePolicies0PolicyDocument


class ConfigRole:
    resource: iam.Role
    assume_role_policy_document = ConfigRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWS_ConfigRole']
    policies = [ConfigRolePolicy]


class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:*',
        'config:PutEvaluations',
        'ec2:DescribeVolumeAttribute',
    ]
    resource_arn = '*'


class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1]


class LambdaExecutionRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


class LambdaExecutionRole:
    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]
