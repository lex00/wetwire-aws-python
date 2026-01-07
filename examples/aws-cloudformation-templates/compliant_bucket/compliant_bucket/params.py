"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """This name be used as a prefix for resource names"""

    type = STRING
    description = 'This name be used as a prefix for resource names'
