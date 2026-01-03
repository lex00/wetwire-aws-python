"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'Current'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Operation': 'Current',
})


class S3BucketFilterTag1:
    resource: s3outposts.Bucket.FilterTag
    key = 'Add'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Days': Days,
    'Operation': 'Add',
})


class S3BucketFilterTag2:
    resource: s3outposts.Bucket.FilterTag
    key = 'Subtract'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Days': Days,
    'Operation': 'Subtract',
})


class S3BucketFilterTag3:
    resource: s3outposts.Bucket.FilterTag
    key = 'Days'
    value = Transform(name='Date', parameters={
    'Date': Date,
    'Date2': Date2,
    'Operation': 'Days',
})


class S3Bucket:
    resource: s3.Bucket
    tags = [S3BucketFilterTag, S3BucketFilterTag1, S3BucketFilterTag2, S3BucketFilterTag3]
