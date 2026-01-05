"""Storage resources: BucketToCopyB, BucketToCopyC, BucketToCopyD, BucketToCopyA."""

from . import *  # noqa: F403


class BucketToCopyBTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB(s3.Bucket):
    tags = [BucketToCopyBTagFilter]


class BucketToCopyCTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC(s3.Bucket):
    tags = [BucketToCopyCTagFilter]


class BucketToCopyDTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD(s3.Bucket):
    tags = [BucketToCopyDTagFilter]


class BucketToCopyATagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA(s3.Bucket):
    tags = [BucketToCopyATagFilter]
