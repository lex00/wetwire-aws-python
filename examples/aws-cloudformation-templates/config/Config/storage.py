"""Storage resources: ConfigBucket."""

from . import *  # noqa: F403


class ConfigBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class ConfigBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ConfigBucketServerSideEncryptionByDefault


class ConfigBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [ConfigBucketServerSideEncryptionRule]


class ConfigBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ConfigBucket(s3.Bucket):
    bucket_encryption = ConfigBucketBucketEncryption
    public_access_block_configuration = ConfigBucketPublicAccessBlockConfiguration
