"""Template outputs."""

from . import *  # noqa: F403


class LambdaRoleARNOutput(Output):
    """Role for Lambda execution."""

    value = LambdaRole.Arn
    description = 'Role for Lambda execution.'
    export_name = 'LambdaRole'


class LambdaFunctionNameOutput(Output):
    value = LambdaFunction


class LambdaFunctionARNOutput(Output):
    """Lambda function ARN."""

    value = LambdaFunction.Arn
    description = 'Lambda function ARN.'
    export_name = Sub('LambdaARN-${EnvName}')
