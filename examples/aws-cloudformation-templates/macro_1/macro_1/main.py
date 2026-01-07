"""Stack resources."""

from . import *  # noqa: F403


class ResourceFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'PowerUserAccess'


class MacroFunctionEnvironment(lambda_.Function.Environment):
    variables = {
        'LAMBDA_ARN': ResourceFunction.Arn,
    }


class MacroFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'macro.handler'
    environment = MacroFunctionEnvironment
