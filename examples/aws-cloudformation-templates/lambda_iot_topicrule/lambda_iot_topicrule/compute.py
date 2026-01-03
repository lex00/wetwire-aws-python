"""Compute resources: MyLambda, MyLambdaPermission, MyLambdaVersion."""

from . import *  # noqa: F403


class MyLambdaCode:
    resource: lambda_.Function.Code
    zip_file = """exports.handler = async (event) => { console.log(event); return {'statusCode': 200, 'body': "OK"}; }
"""


class MyLambda:
    resource: lambda_.Function
    runtime = lambda_.Runtime.NODEJS20_X
    handler = 'index.handler'
    code = MyLambdaCode
    function_name = Sub('${AWS::StackName}')
    role = MyLambdaRole.Arn


class MyLambdaPermission:
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = Sub('${AWS::StackName}')
    principal = 'iot.amazonaws.com'
    source_account = Sub('${AWS::AccountId}')
    source_arn = IoTTopicRule.Arn


class MyLambdaVersion:
    resource: lambda_.Version
    function_name = Sub('${AWS::StackName}')
    depends_on = [MyLambda]
