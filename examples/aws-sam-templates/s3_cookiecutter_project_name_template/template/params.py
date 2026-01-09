"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppBucketName(Parameter):
    """REQUIRED: Unique S3 bucket name to use for the app."""

    type = STRING
    description = 'REQUIRED: Unique S3 bucket name to use for the app.'
