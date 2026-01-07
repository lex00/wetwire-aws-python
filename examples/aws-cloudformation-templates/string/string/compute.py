"""Compute resources: TransformFunction, TransformFunctionPermissions."""

from . import *  # noqa: F403


class TransformFunctionCode(lambda_.Function.Code):
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


class TransformFunction(lambda_.Function):
    code = TransformFunctionCode
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_12
    role = TransformExecutionRole.Arn


class TransformFunctionPermissions(lambda_.Permission):
    action = 'lambda:InvokeFunction'
    function_name = TransformFunction.Arn
    principal = 'cloudformation.amazonaws.com'
