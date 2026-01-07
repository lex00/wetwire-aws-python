"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CodeBuildStack(Parameter):
    """Name of the code build stack which should have been deployed before this stack"""

    type = STRING
    description = 'Name of the code build stack which should have been deployed before this stack'
