"""Storage resources: BucketToCopyA, BucketToCopyD, BucketToCopyC, BucketToCopyB."""

from . import *  # noqa: F403


class BucketToCopyATagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA:
    resource: s3.Bucket
    tags = [BucketToCopyATagFilter]


class BucketToCopyDTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD:
    resource: s3.Bucket
    tags = [BucketToCopyDTagFilter]


class BucketToCopyCTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC:
    resource: s3.Bucket
    tags = [BucketToCopyCTagFilter]


class BucketToCopyBTagFilter:
    resource: s3.Bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB:
    resource: s3.Bucket
    tags = [BucketToCopyBTagFilter]
