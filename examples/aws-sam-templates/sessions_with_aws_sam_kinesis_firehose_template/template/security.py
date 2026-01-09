"""Security resources: FirehoseAccessRole, KinesisAnalyticsAccessRole."""

from . import *  # noqa: F403


class FirehoseAccessRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'firehose.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class FirehoseAccessRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [FirehoseAccessRoleAllowStatement0]


class FirehoseAccessRolePolicy(iam.User.Policy):
    policy_name = 'S3WritePolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['s3:PutObject'],
            'Effect': 'Allow',
            'Resource': [
                RawDataBucket.Arn,
                Sub('${Arn}/*', {
    'Arn': RawDataBucket.Arn,
}),
                ProcessedDataBucket.Arn,
                Sub('${Arn}/*', {
    'Arn': ProcessedDataBucket.Arn,
}),
            ],
        },
    }


class FirehoseAccessRolePolicy1(iam.User.Policy):
    policy_name = 'LambdaInvokePolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['lambda:InvokeFunction'],
            'Effect': 'Allow',
            'Resource': [ProcessFunction.Arn],
        },
    }


class FirehoseAccessRole(iam.Role):
    assume_role_policy_document = FirehoseAccessRoleAssumeRolePolicyDocument
    policies = [FirehoseAccessRolePolicy, FirehoseAccessRolePolicy1]


class KinesisAnalyticsAccessRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'kinesisanalytics.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class KinesisAnalyticsAccessRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [KinesisAnalyticsAccessRoleAllowStatement0]


class KinesisAnalyticsAccessRolePolicy(iam.User.Policy):
    policy_name = 'KinesisAccessPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'firehose:DescribeDeliveryStream',
                'firehose:Get*',
                'kinesis:Describe*',
                'kinesis:Get*',
                'kinesis:List*',
                'kinesis:Put*',
            ],
            'Effect': 'Allow',
            'Resource': [Firehose.Arn],
        },
    }


class KinesisAnalyticsAccessRolePolicy1(iam.User.Policy):
    policy_name = 'LambdaAccessPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'lambda:InvokeFunction',
                'lambda:Get*',
            ],
            'Effect': 'Allow',
            'Resource': [
                CountFunction.Arn,
                Sub('${Func}:$LATEST', {
    'Func': CountFunction.Arn,
}),
            ],
        },
    }


class KinesisAnalyticsAccessRole(iam.Role):
    assume_role_policy_document = KinesisAnalyticsAccessRoleAssumeRolePolicyDocument
    policies = [KinesisAnalyticsAccessRolePolicy, KinesisAnalyticsAccessRolePolicy1]
