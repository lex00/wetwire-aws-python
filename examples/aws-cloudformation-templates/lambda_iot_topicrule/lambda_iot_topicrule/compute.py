"""Compute resources: MyLambda, MyLambdaVersion, MyLambdaPermission."""

from . import *  # noqa: F403


class MyLambdaCode(lambda_.Function.Code):
    zip_file = """exports.handler = async (event) => { console.log(event); return {'statusCode': 200, 'body': "OK"}; }
"""


class MyLambda(lambda_.Function):
    resource: lambda_.Function
    runtime = lambda_.Runtime.NODEJS20_X
    handler = 'index.handler'
    code = MyLambdaCode
    function_name = AWS_STACK_NAME
    role = MyLambdaRole.Arn


class MyLambdaVersion(lambda_.Version):
    resource: lambda_.Version
    function_name = AWS_STACK_NAME
    depends_on = [MyLambda]


class MyLambdaPermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = AWS_STACK_NAME
    principal = 'iot.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    source_arn = IoTTopicRule.Arn
