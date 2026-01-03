"""Storage resources: LoggingBucket, LoggingBucketPolicy."""

from . import *  # noqa: F403


class LoggingBucketRule:
    resource: s3outposts.Bucket.Rule
    # Unknown CF key: ObjectOwnership = 'ObjectWriter'


class LoggingBucketLifecycleConfiguration:
    resource: s3outposts.Bucket.LifecycleConfiguration
    rules = [LoggingBucketRule]


class LoggingBucketPublicAccessBlockConfiguration:
    resource: s3objectlambda.AccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class LoggingBucketServerSideEncryptionByDefault:
    resource: s3express.DirectoryBucket.ServerSideEncryptionByDefault
    kms_master_key_id = LoggingBucketKMSKey.Arn
    sse_algorithm = s3.ServerSideEncryption.AWSKMS


class LoggingBucketServerSideEncryptionRule:
    resource: s3express.DirectoryBucket.ServerSideEncryptionRule
    server_side_encryption_by_default = LoggingBucketServerSideEncryptionByDefault


class LoggingBucketBucketEncryption:
    resource: s3express.DirectoryBucket.BucketEncryption
    server_side_encryption_configuration = [LoggingBucketServerSideEncryptionRule]


class LoggingBucketMetricsConfiguration:
    resource: s3tables.TableBucket.MetricsConfiguration
    status = LoggingBucketVersioning


class LoggingBucket:
    resource: s3.Bucket
    bucket_name = Sub('${AppName}-logging-${Environment}-${AWS::AccountId}-${AWS::Region}')
    ownership_controls = LoggingBucketLifecycleConfiguration
    public_access_block_configuration = LoggingBucketPublicAccessBlockConfiguration
    access_control = 'LogDeliveryWrite'
    bucket_encryption = LoggingBucketBucketEncryption
    versioning_configuration = LoggingBucketMetricsConfiguration
    depends_on = [LoggingBucketKMSKey]
    deletion_policy = 'Retain'


class LoggingBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'LoggingBucketPermissions'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]


class LoggingBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class LoggingBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LoggingBucketPolicyAllowStatement0, LoggingBucketPolicyDenyStatement1]


class LoggingBucketPolicy:
    resource: s3.BucketPolicy
    bucket = LoggingBucket
    policy_document = LoggingBucketPolicyPolicyDocument
