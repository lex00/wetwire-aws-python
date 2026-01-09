"""Stack resources."""

from . import *  # noqa: F403


class MyApi(serverless.Api):
    stage_name = 'Prod'
    endpoint_configuration = 'REGIONAL'
    tracing_enabled = True
    auth = {
        'DefaultAuthorizer': 'AWS_IAM',
        'InvokeRole': 'CALLER_CREDENTIALS',
    }
    access_log_setting = {
        'DestinationArn': MyLogGroup.Arn,
        'Format': """{"requestId":"$context.requestId", "waf-error":"$context.waf.error", "waf-status":"$context.waf.status", "waf-latency":"$context.waf.latency", "waf-response":"$context.wafResponseCode", "authenticate-error":"$context.authenticate.error", "authenticate-status":"$context.authenticate.status", "authenticate-latency":"$context.authenticate.latency", "authorize-error":"$context.authorize.error", "authorize-status":"$context.authorize.status", "authorize-latency":"$context.authorize.latency", "integration-error":"$context.integration.error", "integration-status":"$context.integration.status", "integration-latency":"$context.integration.latency", "integration-requestId":"$context.integration.requestId", "integration-integrationStatus":"$context.integration.integrationStatus", "response-latency":"$context.responseLatency", "status":"$context.status"}
""",
    }


class MyLambdaFunction(serverless.Function):
    code_uri = 'src/'
    events = {
        'RootGet': {
            'Type': 'Api',
            'Properties': {
                'Path': '/',
                'Method': 'get',
                'RestApiId': MyApi,
            },
        },
    }
