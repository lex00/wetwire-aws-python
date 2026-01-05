"""Storage resources: Bucket, BucketPolicy."""

from . import *  # noqa: F403


class BucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class BucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = BucketServerSideEncryptionByDefault


class BucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [BucketServerSideEncryptionRule]


class BucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class BucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class Bucket(s3.Bucket):
    bucket_name = BucketName
    bucket_encryption = BucketBucketEncryption
    versioning_configuration = BucketDeleteMarkerReplication
    public_access_block_configuration = BucketPublicAccessBlockConfiguration


class BucketPolicyAllowStatement0(PolicyStatement):
    sid = 'CrossAccPolicyDoc'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${PublisherAccountID}:root')],
    }
    action = 's3:ListBucket'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${Bucket}')


class BucketPolicyAllowStatement1(PolicyStatement):
    sid = 'CrossAccPolicyDoc'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${PublisherAccountID}:root')],
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${Bucket}/*')


class BucketPolicyDenyStatement2(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${BucketName}'),
        Sub('arn:${AWS::Partition}:s3:::${BucketName}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class BucketPolicyPolicyDocument(PolicyDocument):
    statement = [BucketPolicyAllowStatement0, BucketPolicyAllowStatement1, BucketPolicyDenyStatement2]


class BucketPolicy(s3.BucketPolicy):
    bucket = Bucket
    policy_document = BucketPolicyPolicyDocument
