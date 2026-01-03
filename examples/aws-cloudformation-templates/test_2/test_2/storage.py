"""Storage resources: Bucket, NonExplodingBucket."""

from . import *  # noqa: F403


class BucketRule:
    resource: s3outposts.Bucket.Rule
    expiration_in_days = '!Explode Retention'
    status = s3.BucketVersioningStatus.ENABLED


class BucketLifecycleConfiguration:
    resource: s3outposts.Bucket.LifecycleConfiguration
    rules = [BucketRule]


class Bucket:
    resource: s3.Bucket
    lifecycle_configuration = BucketLifecycleConfiguration


class NonExplodingBucket:
    resource: s3.Bucket
