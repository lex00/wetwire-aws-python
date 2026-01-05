"""Compute resources: LambdaFunction."""

from . import *  # noqa: F403


class LambdaFunctionCode:
    resource: lambda_.Function.Code
    zip_file = """import json

def lambda_handler(event, context):
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
"""


class LambdaFunctionEnvironment:
    resource: lambda_.Function.Environment
    variables = {
        'ENV': EnvName,
        'TZ': 'UTC',
    }


class LambdaFunction(lambda_.Function):
    function_name = Sub('lambda-function-${EnvName}')
    description = 'LambdaFunction using python3.12.'
    runtime = lambda_.Runtime.PYTHON3_12
    code = LambdaFunctionCode
    handler = LambdaHandlerPath
    memory_size = 128
    timeout = 10
    role = LambdaRole.Arn
    environment = LambdaFunctionEnvironment
