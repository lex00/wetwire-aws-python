"""Template outputs."""

from . import *  # noqa: F403


class LambdaRoleARNOutput:
    """Role for Lambda execution."""

    resource: Output
    value = LambdaRole.Arn
    description = 'Role for Lambda execution.'
    export_name = 'LambdaRole'


class LambdaFunctionNameOutput:
    resource: Output
    value = LambdaFunction


class LambdaFunctionARNOutput:
    """Lambda function ARN."""

    resource: Output
    value = LambdaFunction.Arn
    description = 'Lambda function ARN.'
    export_name = Sub('LambdaARN-${EnvName}')
