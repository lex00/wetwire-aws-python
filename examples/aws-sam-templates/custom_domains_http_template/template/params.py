"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName(Parameter):
    """Domain name for api"""

    type = STRING
    description = 'Domain name for api'


class ZoneId(Parameter):
    """Zone ID if exists. If not leave as none."""

    type = STRING
    description = 'Zone ID if exists. If not leave as none.'
    default = 'none'


class CertArn(Parameter):
    """Certificate ARN if exists. If not leave as none."""

    type = STRING
    description = 'Certificate ARN if exists. If not leave as none.'
    default = 'none'


class CreateZoneCondition(TemplateCondition):
    logical_id = 'CreateZone'
    expression = Equals(ZoneId, 'none')


class CreateCertCondition(TemplateCondition):
    logical_id = 'CreateCert'
    expression = Equals(CertArn, 'none')
