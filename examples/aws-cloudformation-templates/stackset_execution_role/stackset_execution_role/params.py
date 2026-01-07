"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AdministrationAccountId(Parameter):
    """Account ID where the StackSet administration role exists"""

    type = STRING
    description = 'Account ID where the StackSet administration role exists'
