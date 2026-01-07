"""Template outputs."""

from . import *  # noqa: F403


class BucketOutput(Output):
    """S3 Bucket Name"""

    value = Bucket
    description = 'S3 Bucket Name'


class BucketPolicyOutput(Output):
    """S3 Bucket Policy Name"""

    value = BucketPolicy
    description = 'S3 Bucket Policy Name'
