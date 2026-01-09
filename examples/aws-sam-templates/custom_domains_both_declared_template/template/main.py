"""Stack resources."""

from . import *  # noqa: F403


class HttpApiGateway(serverless.HttpApi):
    pass


class HttpApiFunction(serverless.Function):
    inline_code = 'exports.handler = async (event) => JSON.stringify(event)'
    handler = 'index.handler'
    runtime = 'nodejs16.x'
    events = {
        'FetchHttpApi': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': HttpApiGateway,
                'Method': 'GET',
                'Path': '/',
            },
        },
    }


class RestApiGateway(serverless.Api):
    stage_name = 'Prod'


class RestApiFunction(serverless.Function):
    inline_code = """exports.handler = async (event) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  return response;
};
"""
    handler = 'index.handler'
    runtime = 'nodejs16.x'
    events = {
        'FetchRest': {
            'Type': 'Api',
            'Properties': {
                'RestApiId': RestApiGateway,
                'Method': 'GET',
                'Path': '/',
            },
        },
    }


class GeneratedCert(certificatemanager.Certificate):
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS
    condition = 'CreateCert'
