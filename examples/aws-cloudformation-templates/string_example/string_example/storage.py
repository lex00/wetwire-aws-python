"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketTagFilter(s3.Bucket.TagFilter):
    key = 'Upper'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Upper',
})


class S3BucketTagFilter1(s3.Bucket.TagFilter):
    key = 'Lower'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Lower',
})


class S3BucketTagFilter2(s3.Bucket.TagFilter):
    key = 'Capitalize'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Capitalize',
})


class S3BucketTagFilter3(s3.Bucket.TagFilter):
    key = 'Title'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Title',
})


class S3BucketTagFilter4(s3.Bucket.TagFilter):
    key = 'Replace'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Replace',
    'Old': ' ',
    'New': '_',
})


class S3BucketTagFilter5(s3.Bucket.TagFilter):
    key = 'Strip'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Strip',
    'Chars': 'Tgif',
})


class S3BucketTagFilter6(s3.Bucket.TagFilter):
    key = 'ShortenLeft'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'MaxLength',
    'Length': 4,
    'StripFrom': 'Left',
})


class S3BucketTagFilter7(s3.Bucket.TagFilter):
    key = 'ShortenRight'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'MaxLength',
    'Length': 4,
})


class S3Bucket(s3.Bucket):
    tags = [S3BucketTagFilter, S3BucketTagFilter1, S3BucketTagFilter2, S3BucketTagFilter3, S3BucketTagFilter4, S3BucketTagFilter5, S3BucketTagFilter6, S3BucketTagFilter7]
