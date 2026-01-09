"""Network resources: ReportingV2Mapping."""

from . import *  # noqa: F403


class ReportingV2Mapping(apigatewayv2.ApiMapping):
    api_id = ReportingAPIV2
    api_mapping_key = 'sales/reporting/v2'
    domain_name = DomainName
    stage = '$default'
    depends_on = [ReportingAPIV2ApiGatewayDefaultStage]
