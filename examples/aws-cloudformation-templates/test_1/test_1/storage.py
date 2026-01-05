"""Storage resources: BucketToCopyD, BucketToCopyB, BucketToCopyA, BucketToCopyC."""

from . import *  # noqa: F403


class BucketToCopyDTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD(s3.Bucket):
    tags = [BucketToCopyDTagFilter]


class BucketToCopyBTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB(s3.Bucket):
    tags = [BucketToCopyBTagFilter]


class BucketToCopyATagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA(s3.Bucket):
    tags = [BucketToCopyATagFilter]


class BucketToCopyCTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC(s3.Bucket):
    tags = [BucketToCopyCTagFilter]
