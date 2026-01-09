"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class StackTagName(Parameter):
    """Stack Name (injected by Stackery at deployment time)"""

    type = STRING
    description = 'Stack Name (injected by Stackery at deployment time)'


class EnvironmentTagName(Parameter):
    """Environment Name (injected by Stackery at deployment time)"""

    type = STRING
    description = 'Environment Name (injected by Stackery at deployment time)'
