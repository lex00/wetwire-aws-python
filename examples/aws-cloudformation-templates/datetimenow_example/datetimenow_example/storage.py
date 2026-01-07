"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketTagFilter(s3.Bucket.TagFilter):
    key = 'DatetimeNow'
    value = Transform(name='DatetimeNow', parameters={
    'format': '%Y-%m-%dT%H:%M:%SZ',
})


class S3Bucket(s3.Bucket):
    resource: s3.Bucket
    tags = [S3BucketTagFilter]
