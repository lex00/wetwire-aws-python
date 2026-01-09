"""Template outputs."""

from . import *  # noqa: F403


class AppBucketArnOutput(Output):
    """S3 Bucket"""

    value = AppBucket
    description = 'S3 Bucket'
