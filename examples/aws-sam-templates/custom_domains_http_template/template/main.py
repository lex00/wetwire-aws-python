"""Stack resources."""

from . import *  # noqa: F403


class GeneratedCert(certificatemanager.Certificate):
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS
    condition = 'CreateCert'


class HttpApiGateway(serverless.HttpApi):
    domain = {
        'DomainName': DomainName,
        'CertificateArn': If("CreateCert", GeneratedCert, CertArn),
        'Route53': {
            'HostedZoneId': If("CreateZone", GeneratedZone, ZoneId),
        },
    }


class HttpApiFunction(serverless.Function):
    inline_code = 'exports.handler = async (event) => JSON.stringify(event)'
    handler = 'index.handler'
    runtime = 'nodejs16.x'
    timeout = 30
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
