"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketTagFilter(s3.Bucket.TagFilter):
    key = 'Current'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Operation': 'Current',
})


class S3BucketTagFilter1(s3.Bucket.TagFilter):
    key = 'Add'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Days': Days,
    'Operation': 'Add',
})


class S3BucketTagFilter2(s3.Bucket.TagFilter):
    key = 'Subtract'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Days': Days,
    'Operation': 'Subtract',
})


class S3BucketTagFilter3(s3.Bucket.TagFilter):
    key = 'Days'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Date2': Date2,
    'Operation': 'Days',
})


class S3Bucket(s3.Bucket):
    resource: s3.Bucket
    tags = [S3BucketTagFilter, S3BucketTagFilter1, S3BucketTagFilter2, S3BucketTagFilter3]
