"""Compute resources: S3TriggerLambdaFunction, LambdaInvokePermission."""

from . import *  # noqa: F403


class S3TriggerLambdaFunctionCode:
    resource: lambda_.Function.Code
    zip_file = """import json
def lambda_handler(event,context):
    print(event)
    return "Hello... This is a test S3 trigger Lambda Function"
"""


class S3TriggerLambdaFunction(lambda_.Function):
    code = S3TriggerLambdaFunctionCode
    handler = 'index.lambda_handler'
    role = LambdaIAMRole.Arn
    runtime = lambda_.Runtime.PYTHON3_9
    timeout = 30


class LambdaInvokePermission(lambda_.Permission):
    function_name = S3TriggerLambdaFunction.Arn
    action = 'lambda:InvokeFunction'
    principal = 's3.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    source_arn = Sub('arn:${AWS::Partition}:s3:::${NotificationBucket}')
