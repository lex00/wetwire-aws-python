"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3BucketFilterTag:
    resource: s3outposts.Bucket.FilterTag
    key = 'Upper'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Upper',
})


class S3BucketFilterTag1:
    resource: s3outposts.Bucket.FilterTag
    key = 'Lower'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Lower',
})


class S3BucketFilterTag2:
    resource: s3outposts.Bucket.FilterTag
    key = 'Capitalize'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Capitalize',
})


class S3BucketFilterTag3:
    resource: s3outposts.Bucket.FilterTag
    key = 'Title'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Title',
})


class S3BucketFilterTag4:
    resource: s3outposts.Bucket.FilterTag
    key = 'Replace'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Replace',
    'Old': ' ',
    'New': '_',
})


class S3BucketFilterTag5:
    resource: s3outposts.Bucket.FilterTag
    key = 'Strip'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'Strip',
    'Chars': 'Tgif',
})


class S3BucketFilterTag6:
    resource: s3outposts.Bucket.FilterTag
    key = 'ShortenLeft'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'MaxLength',
    'Length': 4,
    'StripFrom': 'Left',
})


class S3BucketFilterTag7:
    resource: s3outposts.Bucket.FilterTag
    key = 'ShortenRight'
    value = Transform(name='String', parameters={
    'InputString': InputString,
    'Operation': 'MaxLength',
    'Length': 4,
})


class S3Bucket:
    resource: s3.Bucket
    tags = [S3BucketFilterTag, S3BucketFilterTag1, S3BucketFilterTag2, S3BucketFilterTag3, S3BucketFilterTag4, S3BucketFilterTag5, S3BucketFilterTag6, S3BucketFilterTag7]
