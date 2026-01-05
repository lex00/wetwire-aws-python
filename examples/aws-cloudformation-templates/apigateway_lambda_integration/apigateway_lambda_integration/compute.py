"""Compute resources: LambdaFunction, LambdaApiGatewayInvoke."""

from . import *  # noqa: F403


class LambdaFunctionCode:
    resource: lambda_.Function.Code
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


class LambdaFunction(lambda_.Function):
    code = LambdaFunctionCode
    handler = 'index.lambda_handler'
    function_name = LambdaFunctionName
    memory_size = '128'
    runtime = lambda_.Runtime.PYTHON3_12
    timeout = '10'
    role = LambdaIamRole.Arn


class LambdaApiGatewayInvoke(lambda_.Permission):
    action = 'lambda:InvokeFunction'
    function_name = LambdaFunction.Arn
    principal = 'apigateway.amazonaws.com'
    source_arn = Join('', [
    'arn:aws:execute-api:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    RestApi,
    '/*/*/*',
])
