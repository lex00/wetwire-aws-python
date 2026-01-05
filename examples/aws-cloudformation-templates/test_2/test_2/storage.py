"""Storage resources: NonExplodingBucket, Bucket."""

from . import *  # noqa: F403


class NonExplodingBucket(s3.Bucket):
    pass


class BucketOwnershipControlsRule:
    resource: s3.Bucket.OwnershipControlsRule
    # Unknown CF key: ExpirationInDays = '!Explode Retention'
    # Unknown CF key: Status = 'Enabled'


class BucketOwnershipControls:
    resource: s3.Bucket.OwnershipControls
    rules = [BucketOwnershipControlsRule]


class Bucket(s3.Bucket):
    lifecycle_configuration = BucketOwnershipControls
