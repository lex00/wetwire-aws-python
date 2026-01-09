"""Stack resources."""

from . import *  # noqa: F403


class AdminAPIEndpointConfiguration(serverless.Api.EndpointConfiguration):
    type_ = 'REGIONAL'


class AdminAPI(serverless.Api):
    description = 'Administrative API'
    stage_name = 'Prod'
    endpoint_configuration = AdminAPIEndpointConfiguration


class AdminFunction(serverless.Function):
    code_uri = 'src/admin/'
    events = {
        'CorpAdministration': {
            'Type': 'Api',
            'Properties': {
                'RestApiId': AdminAPI,
                'Method': 'GET',
                'Path': '/',
            },
        },
    }
