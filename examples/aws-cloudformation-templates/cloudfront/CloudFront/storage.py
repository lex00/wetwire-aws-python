"""Storage resources: LoggingBucket, LoggingBucketPolicy."""

from . import *  # noqa: F403
from wetwire_aws.constants import BOOL


class LoggingBucketOwnershipControlsRule(s3.Bucket.OwnershipControlsRule):
    object_ownership = 'ObjectWriter'


class LoggingBucketOwnershipControls(s3.Bucket.OwnershipControls):
    rules = [LoggingBucketOwnershipControlsRule]


class LoggingBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class LoggingBucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    kms_master_key_id = LoggingBucketKMSKey.Arn
    sse_algorithm = s3.ServerSideEncryption.AWSKMS


class LoggingBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = LoggingBucketServerSideEncryptionByDefault


class LoggingBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [LoggingBucketServerSideEncryptionRule]


class LoggingBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = LoggingBucketVersioning


class LoggingBucket(s3.Bucket):
    resource: s3.Bucket
    bucket_name = Sub('${AppName}-logging-${Environment}-${AWS::AccountId}-${AWS::Region}')
    ownership_controls = LoggingBucketOwnershipControls
    public_access_block_configuration = LoggingBucketPublicAccessBlockConfiguration
    access_control = 'LogDeliveryWrite'
    bucket_encryption = LoggingBucketBucketEncryption
    versioning_configuration = LoggingBucketDeleteMarkerReplication
    depends_on = [LoggingBucketKMSKey]
    deletion_policy = 'Retain'


class LoggingBucketPolicyAllowStatement0(PolicyStatement):
    sid = 'LoggingBucketPermissions'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]


class LoggingBucketPolicyDenyStatement1(DenyStatement):
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


class LoggingBucketPolicyPolicyDocument(PolicyDocument):
    statement = [LoggingBucketPolicyAllowStatement0, LoggingBucketPolicyDenyStatement1]


class LoggingBucketPolicy(s3.BucketPolicy):
    resource: s3.BucketPolicy
    bucket = LoggingBucket
    policy_document = LoggingBucketPolicyPolicyDocument
