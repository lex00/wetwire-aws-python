"""Network resources: AdminMapping."""

from . import *  # noqa: F403


class AdminMapping(apigatewayv2.ApiMapping):
    api_id = AdminAPI
    api_mapping_key = 'corp/admin'
    domain_name = DomainName
    stage = 'Prod'
    depends_on = [AdminAPIProdStage]
