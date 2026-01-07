"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EnvName(Parameter):
    """Name of an environment. 'dev', 'staging', 'prod' and any name."""

    type = STRING
    description = "Name of an environment. 'dev', 'staging', 'prod' and any name."
    allowed_pattern = '^.*[^0-9]$'
    constraint_description = 'Must end with non-numeric character.'


class LambdaHandlerPath(Parameter):
    """Path of a Lambda Handler."""

    type = STRING
    description = 'Path of a Lambda Handler.'
    allowed_pattern = '^.*[^0-9]$'
    constraint_description = 'Must end with non-numeric character.'
