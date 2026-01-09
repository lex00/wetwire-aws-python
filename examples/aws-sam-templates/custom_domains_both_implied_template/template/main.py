"""Stack resources."""

from . import *  # noqa: F403


class GeneratedCert(certificatemanager.Certificate):
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS
    condition = 'CreateCert'


class RestApiGateway(serverless.Api):
    stage_name = 'Prod'


class HttpApiGateway(serverless.HttpApi):
    domain = {
        'DomainName': DomainName,
        'CertificateArn': If("CreateCert", GeneratedCert, CertArn),
        'Route53': {
            'HostedZoneId': If("CreateZone", GeneratedZone, ZoneId),
        },
        'BasePath': ['http'],
    }


class HttpApiFunction(serverless.Function):
    inline_code = 'exports.handler = async (event) => JSON.stringify(event)'
    handler = 'index.handler'
    runtime = 'nodejs16.x'
    events = {
        'FetchHttp': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': HttpApiGateway,
                'Method': 'GET',
                'Path': '/',
            },
        },
    }


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
