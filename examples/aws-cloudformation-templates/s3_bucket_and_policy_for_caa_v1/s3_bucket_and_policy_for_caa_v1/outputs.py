"""Template outputs."""

from . import *  # noqa: F403


class BucketOutput:
    """S3 Bucket Name"""

    resource: Output
    value = Bucket
    description = 'S3 Bucket Name'


class BucketPolicyOutput:
    """S3 Bucket Policy Name"""

    resource: Output
    value = BucketPolicy
    description = 'S3 Bucket Policy Name'
