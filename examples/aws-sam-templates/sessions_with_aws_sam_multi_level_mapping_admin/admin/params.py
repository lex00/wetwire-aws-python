"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName(Parameter):
    """Domian name for api"""

    type = STRING
    description = 'Domian name for api'
