"""Stack resources."""

from . import *  # noqa: F403


class ResourceFunction(serverless.Function):
    resource: serverless.Function
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'AmazonS3FullAccess'


class MacroFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'LAMBDA_ARN': ResourceFunction.Arn,
    }


class MacroFunction(serverless.Function):
    resource: serverless.Function
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'macro.handler'
    policies = 'AmazonS3FullAccess'
    environment = MacroFunctionEnvironment
