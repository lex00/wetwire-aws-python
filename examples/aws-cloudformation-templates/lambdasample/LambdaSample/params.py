"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EnvName:
    """Name of an environment. 'dev', 'staging', 'prod' and any name."""

    resource: Parameter
    type = STRING
    description = "Name of an environment. 'dev', 'staging', 'prod' and any name."
    allowed_pattern = '^.*[^0-9]$'
    constraint_description = 'Must end with non-numeric character.'


class LambdaHandlerPath:
    """Path of a Lambda Handler."""

    resource: Parameter
    type = STRING
    description = 'Path of a Lambda Handler.'
    allowed_pattern = '^.*[^0-9]$'
    constraint_description = 'Must end with non-numeric character.'
