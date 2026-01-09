"""Stack resources."""

from . import *  # noqa: F403


class HttpApiHttpApiAuth(serverless.HttpApi.HttpApiAuth):
    authorizers = {
        'GeneralAuth': {
            'AuthorizationScopes': ['email'],
            'IdentitySource': '$request.header.Authorization',
            'JwtConfiguration': {
                'issuer': Sub('https://cognito-idp.${AWS::Region}.amazonaws.com/${UserPoolId}'),
                'audience': [Audience],
            },
        },
    }


class HttpApiCorsConfiguration(serverless.HttpApi.CorsConfiguration):
    allow_methods = ['GET']
    allow_origins = ['http://localhost:8080']


class HttpApi(serverless.HttpApi):
    auth = HttpApiHttpApiAuth
    cors_configuration = HttpApiCorsConfiguration


class SimpleAuthLambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'RootGet': {
            'Type': 'HttpApi',
            'Properties': {
                'Auth': {
                    'Authorizer': 'GeneralAuth',
                },
                'Path': '/simple',
                'Method': 'get',
                'ApiId': HttpApi,
            },
        },
    }


class BothLambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'DosGet': {
            'Type': 'HttpApi',
            'Properties': {
                'Auth': {
                    'Authorizer': 'GeneralAuth',
                    'AuthorizationScopes': [
                        Sub('Admins-${Audience}'),
                        Sub('SU-${Audience}'),
                    ],
                },
                'Path': '/both',
                'Method': 'get',
                'ApiId': HttpApi,
            },
        },
    }


class SULambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'DosGet': {
            'Type': 'HttpApi',
            'Properties': {
                'Auth': {
                    'Authorizer': 'GeneralAuth',
                    'AuthorizationScopes': [Sub('SU-${Audience}')],
                },
                'Path': '/su',
                'Method': 'get',
                'ApiId': HttpApi,
            },
        },
    }


class CatchAllLambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'RootGet': {
            'Type': 'HttpApi',
        },
    }


class AdminLambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'DosGet': {
            'Type': 'HttpApi',
            'Properties': {
                'Auth': {
                    'Authorizer': 'GeneralAuth',
                    'AuthorizationScopes': [Sub('Admins-${Audience}')],
                },
                'Path': '/admin',
                'Method': 'get',
                'ApiId': HttpApi,
            },
        },
    }


class LambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'RootGet': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/',
                'Method': 'get',
                'ApiId': HttpApi,
            },
        },
    }
