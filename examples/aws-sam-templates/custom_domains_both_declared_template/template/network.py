"""Network resources: GeneratedZone, CustomDomainName, HttpApiMapping, RecordSet, RestApiMapping."""

from . import *  # noqa: F403


class GeneratedZone(route53.HostedZone):
    name = DomainName
    condition = 'CreateZone'


class CustomDomainNameDomainNameConfiguration(apigatewayv2.DomainName.DomainNameConfiguration):
    endpoint_type = 'REGIONAL'
    certificate_arn = If("CreateCert", GeneratedCert, CertArn)


class CustomDomainName(apigatewayv2.DomainName):
    domain_name = DomainName
    domain_name_configurations = [CustomDomainNameDomainNameConfiguration]


class HttpApiMapping(apigatewayv2.ApiMapping):
    api_id = HttpApiGateway
    api_mapping_key = 'http'
    domain_name = CustomDomainName
    stage = HttpApiGatewayApiGatewayDefaultStage  # noqa: WAW019 - SAM implicit resource


class RecordSetAliasTarget(route53.RecordSetGroup.AliasTarget):
    dns_name = CustomDomainName.RegionalDomainName
    hosted_zone_id = CustomDomainName.RegionalHostedZoneId


class RecordSet(route53.RecordSet):
    name = DomainName
    hosted_zone_id = If("CreateZone", GeneratedZone, ZoneId)
    alias_target = RecordSetAliasTarget
    type_ = 'A'


class RestApiMapping(apigatewayv2.ApiMapping):
    api_id = RestApiGateway
    api_mapping_key = 'rest'
    domain_name = CustomDomainName
    stage = RestApiGatewayProdStage  # noqa: WAW019 - SAM implicit resource
