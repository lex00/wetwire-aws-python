"""Storage resources: ConfigBucket."""

from . import *  # noqa: F403


class ConfigBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ConfigBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ConfigBucketMetadataTableEncryptionConfiguration


class ConfigBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ConfigBucketServerSideEncryptionRule]


class ConfigBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ConfigBucket(s3.Bucket):
    bucket_encryption = ConfigBucketBucketEncryption
    public_access_block_configuration = ConfigBucketPublicAccessBlockConfiguration
