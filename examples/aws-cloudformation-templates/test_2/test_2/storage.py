"""Storage resources: Bucket, NonExplodingBucket."""

from . import *  # noqa: F403


class BucketOwnershipControlsRule(s3.Bucket.OwnershipControlsRule):
    # Unknown CF key: ExpirationInDays = '!Explode Retention'
    # Unknown CF key: Status = 'Enabled'


class BucketOwnershipControls(s3.Bucket.OwnershipControls):
    rules = [BucketOwnershipControlsRule]


class Bucket(s3.Bucket):
    lifecycle_configuration = BucketOwnershipControls


class NonExplodingBucket(s3.Bucket):
    pass
