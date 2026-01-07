"""Compute resources: TransformFunction, TransformFunctionPermissions."""

from . import *  # noqa: F403


class TransformFunctionCode(lambda_.Function.Code):
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


class TransformFunction(lambda_.Function):
    description = 'Support for the PyPlate CloudFormation macro'
    code = TransformFunctionCode
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_11
    role = TransformExecutionRole.Arn
    timeout = LambdaTimeout


class TransformFunctionPermissions(lambda_.Permission):
    action = 'lambda:InvokeFunction'
    function_name = TransformFunction.Arn
    principal = 'cloudformation.amazonaws.com'
