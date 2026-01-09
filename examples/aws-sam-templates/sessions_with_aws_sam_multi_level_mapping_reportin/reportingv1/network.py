"""Network resources: ReportingV1Mapping."""

from . import *  # noqa: F403


class ReportingV1Mapping(apigatewayv2.ApiMapping):
    api_id = ReportingAPIV1
    api_mapping_key = 'sales/reporting'
    domain_name = DomainName
    stage = '$default'
    depends_on = [ReportingAPIV1ApiGatewayDefaultStage]
