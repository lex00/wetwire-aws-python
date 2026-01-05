"""Storage resources: Bucket, NonExplodingBucket."""

from . import *  # noqa: F403


class BucketOwnershipControlsRule:
    resource: s3.Bucket.OwnershipControlsRule
    # Unknown CF key: ExpirationInDays = '!Explode Retention'
    # Unknown CF key: Status = 'Enabled'


class BucketOwnershipControls:
    resource: s3.Bucket.OwnershipControls
    rules = [BucketOwnershipControlsRule]


class Bucket:
    resource: s3.Bucket
    lifecycle_configuration = BucketOwnershipControls


class NonExplodingBucket:
    resource: s3.Bucket
