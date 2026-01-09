"""Storage resources: AppBucket."""

from . import *  # noqa: F403


class AppBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    bucket_key_enabled = True


class AppBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [AppBucketServerSideEncryptionRule]


class AppBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class AppBucket(s3.Bucket):
    bucket_name = AppBucketName
    bucket_encryption = AppBucketBucketEncryption
    versioning_configuration = AppBucketDeleteMarkerReplication
