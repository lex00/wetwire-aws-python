"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class S3BucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = S3BucketServerSideEncryptionByDefault


class S3BucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [S3BucketServerSideEncryptionRule]


class S3BucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class S3Bucket(s3.Bucket):
    resource: s3.Bucket
    bucket_encryption = S3BucketBucketEncryption
    public_access_block_configuration = S3BucketPublicAccessBlockConfiguration
