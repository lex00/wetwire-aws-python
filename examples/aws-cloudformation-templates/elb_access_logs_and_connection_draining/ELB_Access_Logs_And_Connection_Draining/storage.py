"""Storage resources: LogsBucket, LogsBucketPolicy."""

from . import *  # noqa: F403


class LogsBucket:
    resource: s3.Bucket
    access_control = 'Private'
    deletion_policy = 'Retain'


class LogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'ELBAccessLogs20130930'
    principal = {
        'AWS': FindInMap("Region2ELBAccountId", AWS_REGION, 'AccountId'),
    }
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*')]


class LogsBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class LogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LogsBucketPolicyAllowStatement0, LogsBucketPolicyDenyStatement1]


class LogsBucketPolicy:
    resource: s3.BucketPolicy
    bucket = LogsBucket
    policy_document = LogsBucketPolicyPolicyDocument
