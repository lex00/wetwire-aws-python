"""Storage resources: BucketToCopyC, BucketToCopyA, BucketToCopyB, BucketToCopyD."""

from . import *  # noqa: F403


class BucketToCopyCTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC(s3.Bucket):
    tags = [BucketToCopyCTagFilter]


class BucketToCopyATagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA(s3.Bucket):
    tags = [BucketToCopyATagFilter]


class BucketToCopyBTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB(s3.Bucket):
    tags = [BucketToCopyBTagFilter]


class BucketToCopyDTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD(s3.Bucket):
    tags = [BucketToCopyDTagFilter]
