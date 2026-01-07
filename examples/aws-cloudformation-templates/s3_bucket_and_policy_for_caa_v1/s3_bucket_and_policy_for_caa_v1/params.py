"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class BucketName(Parameter):
    """The name of the S3 Bucket to create, make this unique"""

    type = STRING
    description = 'The name of the S3 Bucket to create, make this unique'


class PublisherAccountID(Parameter):
    """The AWS account ID with whom you are sharing access"""

    type = STRING
    description = 'The AWS account ID with whom you are sharing access'
