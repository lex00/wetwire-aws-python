"""Security resources: DeliveryRole."""

from . import *  # noqa: F403


class DeliveryRoleAllowStatement0(PolicyStatement):
    sid = ''
    principal = {
        'Service': 'firehose.amazonaws.com',
    }
    action = 'sts:AssumeRole'
    condition = {
        STRING_EQUALS: {
            'sts:ExternalId': AWS_ACCOUNT_ID,
        },
    }


class DeliveryRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DeliveryRoleAllowStatement0]


class DeliveryRoleAllowStatement0_1(PolicyStatement):
    action = [
        's3:AbortMultipartUpload',
        's3:GetBucketLocation',
        's3:GetObject',
        's3:ListBucket',
        's3:ListBucketMultipartUploads',
        's3:PutObject',
    ]
    resource_arn = [
        Join('', [
    'arn:aws:s3:::',
    DestinationBucketName,
]),
        Join('', [
    'arn:aws:s3:::',
    DestinationBucketName,
    '/*',
]),
    ]


class DeliveryRoleAllowStatement1(PolicyStatement):
    action = ['logs:PutLogEvents']
    resource_arn = Join('', [
    Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/kinesisfirehose/'),
    LogGroupName,
    ':*',
])


class DeliveryRolePolicies0PolicyDocument(PolicyDocument):
    statement = [DeliveryRoleAllowStatement0_1, DeliveryRoleAllowStatement1]


class DeliveryRolePolicy(iam.User.Policy):
    policy_name = 'firehose_delivery_policy'
    policy_document = DeliveryRolePolicies0PolicyDocument


class DeliveryRole(iam.Role):
    assume_role_policy_document = DeliveryRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DeliveryRolePolicy]
