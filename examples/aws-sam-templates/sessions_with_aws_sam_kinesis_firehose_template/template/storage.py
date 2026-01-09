"""Storage resources: ProcessedDataBucket, RawDataBucket."""

from . import *  # noqa: F403


class ProcessedDataBucket(s3.Bucket):
    pass


class RawDataBucket(s3.Bucket):
    pass
