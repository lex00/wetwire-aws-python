"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'DatetimeNow'
    value = Transform(name='DatetimeNow', parameters={
    'format': '%Y-%m-%dT%H:%M:%SZ',
})


class S3Bucket:
    resource: s3.Bucket
    tags = [S3BucketFilterTag]
