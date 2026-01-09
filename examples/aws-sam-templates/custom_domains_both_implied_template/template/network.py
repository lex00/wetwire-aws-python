"""Network resources: RestApiMapping, GeneratedZone."""

from . import *  # noqa: F403


class RestApiMapping(apigatewayv2.ApiMapping):
    api_id = RestApiGateway
    api_mapping_key = 'rest'
    domain_name = DomainName
    stage = RestApiGatewayProdStage  # noqa: WAW019 - SAM implicit resource
    depends_on = ["HttpApiGatewayhttpApiMapping"]  # SAM implicit resource


class GeneratedZone(route53.HostedZone):
    name = DomainName
    condition = 'CreateZone'
