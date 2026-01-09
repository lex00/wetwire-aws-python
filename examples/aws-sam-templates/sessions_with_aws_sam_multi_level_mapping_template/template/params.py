"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName(Parameter):
    """Domian name for api"""

    type = STRING
    description = 'Domian name for api'


class ZoneId(Parameter):
    """Zone ID"""

    type = STRING
    description = 'Zone ID'
    default = 'none'


class CertArn(Parameter):
    """Certificate ARN"""

    type = STRING
    description = 'Certificate ARN'
    default = 'none'
