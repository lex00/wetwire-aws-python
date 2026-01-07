"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """This name will be used as part of resource names"""

    type = STRING
    description = 'This name will be used as part of resource names'
    default = 'stacksets-sample'
