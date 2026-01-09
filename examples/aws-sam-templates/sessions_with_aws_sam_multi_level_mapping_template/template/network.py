"""Network resources: CustomDomainName, DomainRecordSet."""

from . import *  # noqa: F403


class CustomDomainNameDomainNameConfiguration(apigatewayv2.DomainName.DomainNameConfiguration):
    endpoint_type = 'REGIONAL'
    certificate_arn = CertArn


class CustomDomainName(apigatewayv2.DomainName):
    domain_name = DomainName
    domain_name_configurations = [CustomDomainNameDomainNameConfiguration]


class DomainRecordSetAliasTarget(route53.RecordSetGroup.AliasTarget):
    dns_name = CustomDomainName.RegionalDomainName
    hosted_zone_id = CustomDomainName.RegionalHostedZoneId


class DomainRecordSet(route53.RecordSet):
    name = DomainName
    hosted_zone_id = ZoneId
    alias_target = DomainRecordSetAliasTarget
    type_ = 'A'
