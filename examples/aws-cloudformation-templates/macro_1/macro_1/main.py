"""Stack resources."""

from . import *  # noqa: F403


class ResourceFunction(serverless.Function):
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'PowerUserAccess'


class MacroFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'LAMBDA_ARN': ResourceFunction.Arn,
    }


class MacroFunction(serverless.Function):
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'macro.handler'
    environment = MacroFunctionEnvironment
