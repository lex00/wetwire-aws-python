"""Storage resources: BucketToCopyA, BucketToCopyB, BucketToCopyD, BucketToCopyC."""

from . import *  # noqa: F403


class BucketToCopyATagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyATagFilter]


class BucketToCopyBTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyBTagFilter]


class BucketToCopyDTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyDTagFilter]


class BucketToCopyCTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyCTagFilter]
