"""Storage resources: BucketToCopyD, BucketToCopyA, BucketToCopyB, BucketToCopyC."""

from . import *  # noqa: F403


class BucketToCopyDFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD:
    resource: s3.Bucket
    tags = [BucketToCopyDFilterTag]


class BucketToCopyAFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA:
    resource: s3.Bucket
    tags = [BucketToCopyAFilterTag]


class BucketToCopyBFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB:
    resource: s3.Bucket
    tags = [BucketToCopyBFilterTag]


class BucketToCopyCFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC:
    resource: s3.Bucket
    tags = [BucketToCopyCFilterTag]
