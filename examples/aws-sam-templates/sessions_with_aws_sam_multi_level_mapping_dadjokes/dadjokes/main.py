"""Stack resources."""

from . import *  # noqa: F403


class ReportingAPIV1(serverless.HttpApi):
    description = 'Jokes API'
    definition_body = {
        'openapi': '3.0.1',
        'info': {
            'title': 'Corp Dad Jokes',
        },
        'paths': {
            '/': {
                'get': {
                    'responses': {
                        'default': {
                            'description': 'Default response for GET /',
                        },
                    },
                    'x-amazon-apigateway-integration': {
                        'requestParameters': {
                            'overwrite:header.Accept': 'application/json',
                        },
                        'payloadFormatVersion': '1.0',
                        'type': 'http_proxy',
                        'httpMethod': 'ANY',
                        'uri': 'https://icanhazdadjoke.com/',
                        'connectionType': 'INTERNET',
                    },
                },
            },
        },
        'x-amazon-apigateway-importexport-version': '1.0',
    }
