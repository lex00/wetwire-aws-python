"""Storage resources: BucketToCopyB, BucketToCopyA, BucketToCopyD, BucketToCopyC."""

from . import *  # noqa: F403


class BucketToCopyBFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyB:
    resource: s3.Bucket
    tags = [BucketToCopyBFilterTag]


class BucketToCopyAFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyA:
    resource: s3.Bucket
    tags = [BucketToCopyAFilterTag]


class BucketToCopyDFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my %s bucket %d'


class BucketToCopyD:
    resource: s3.Bucket
    tags = [BucketToCopyDFilterTag]


class BucketToCopyCFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'TestKey'
    value = 'my bucket %d'


class BucketToCopyC:
    resource: s3.Bucket
    tags = [BucketToCopyCFilterTag]
