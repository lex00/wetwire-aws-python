"""Storage resources: ConfigBucket."""

from . import *  # noqa: F403


class ConfigBucketServerSideEncryptionByDefault:
    resource: s3express.DirectoryBucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class ConfigBucketServerSideEncryptionRule:
    resource: s3express.DirectoryBucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ConfigBucketServerSideEncryptionByDefault


class ConfigBucketBucketEncryption:
    resource: s3express.DirectoryBucket.BucketEncryption
    server_side_encryption_configuration = [ConfigBucketServerSideEncryptionRule]


class ConfigBucketPublicAccessBlockConfiguration:
    resource: s3objectlambda.AccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ConfigBucket:
    resource: s3.Bucket
    bucket_encryption = ConfigBucketBucketEncryption
    public_access_block_configuration = ConfigBucketPublicAccessBlockConfiguration
