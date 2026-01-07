"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class NotificationBucket(Parameter):
    """S3 bucket name that is the trigger to lambda"""

    type = STRING
    description = 'S3 bucket name that is the trigger to lambda'
