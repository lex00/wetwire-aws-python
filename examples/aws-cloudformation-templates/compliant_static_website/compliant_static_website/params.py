"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """This name be used as a prefix for resource names"""

    type = STRING
    description = 'This name be used as a prefix for resource names'


class WebACL(Parameter):
    """The web acl id of a CLOUDFRONT scoped web acl in us-east-1"""

    type = STRING
    description = 'The web acl id of a CLOUDFRONT scoped web acl in us-east-1'
