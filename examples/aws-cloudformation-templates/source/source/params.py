"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AccountIdDestination(Parameter):
    """Account Id of the destination AWS Account for replication (ie: 123456789012)."""

    type = STRING
    description = 'Account Id of the destination AWS Account for replication (ie: 123456789012).'
