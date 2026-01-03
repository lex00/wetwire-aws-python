"""Stack resources."""

from . import *  # noqa: F403


class ResourceFunction:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'PowerUserAccess'


class MacroFunctionEnvironment:
    resource: lambda_.Function.Environment
    variables = {
        'LAMBDA_ARN': ResourceFunction.Arn,
    }


class MacroFunction:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'macro.handler'
    environment = MacroFunctionEnvironment
