"""Stack resources."""

from . import *  # noqa: F403


class MyHttpApiCorsConfiguration(serverless.HttpApi.CorsConfiguration):
    allow_methods = ['GET']
    allow_origins = ['http://localhost:8080']


class MyHttpApi(serverless.HttpApi):
    access_log_settings = {
        'DestinationArn': MyLogGroup.Arn,
        'Format': '{ "requestId":"$context.requestId", "ip": "$context.identity.sourceIp", "requestTime":"$context.requestTime", "httpMethod":"$context.httpMethod","routeKey":"$context.routeKey", "status":"$context.status","protocol":"$context.protocol", "responseLength":"$context.responseLength", "integrationError":"$context.integrationErrorMessage" }',
    }
    cors_configuration = MyHttpApiCorsConfiguration


class HelloWorldFunction(serverless.Function):
    code_uri = 'src/'
    handler = 'app.lambdaHandler'
    runtime = 'nodejs16.x'
    events = {
        'HelloWorld': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/',
                'Method': 'GET',
                'ApiId': MyHttpApi,
            },
        },
    }
