"""Storage resources: Bucket, NonExplodingBucket."""

from . import *  # noqa: F403


class BucketRule(s3.Bucket.Rule):
    expiration_in_days = '!Explode Retention'
    status = s3.BucketVersioningStatus.ENABLED


class BucketOwnershipControls(s3.Bucket.OwnershipControls):
    rules = [BucketRule]


class Bucket(s3.Bucket):
    lifecycle_configuration = BucketOwnershipControls


class NonExplodingBucket(s3.Bucket):
    pass
