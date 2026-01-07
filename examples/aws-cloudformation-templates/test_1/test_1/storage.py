"""Storage resources: BucketToCopyD, BucketToCopyA, BucketToCopyC, BucketToCopyB."""

from . import *  # noqa: F403


class BucketToCopyDTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyDTagFilter]


class BucketToCopyATagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyATagFilter]


class BucketToCopyCTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyCTagFilter]


class BucketToCopyBTagFilter(s3.Bucket.TagFilter):
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB(s3.Bucket):
    resource: s3.Bucket
    tags = [BucketToCopyBTagFilter]
