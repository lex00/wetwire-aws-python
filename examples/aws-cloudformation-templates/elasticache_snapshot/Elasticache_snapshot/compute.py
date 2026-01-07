"""Compute resources: EnableShapshot, LambdaExecutePermission."""

from . import *  # noqa: F403


class EnableShapshotCode(lambda_.Function.Code):
    zip_file = {
        'Rain::Embed': 'elastic-code.js',
    }


class EnableShapshot(lambda_.Function):
    resource: lambda_.Function
    code = EnableShapshotCode
    handler = 'index.handler'
    memory_size = 128
    role = IamRoleLambda.Arn
    runtime = lambda_.Runtime.NODEJS20_X
    timeout = 30
    depends_on = [IamRoleLambda]
    condition = 'EnableBackups'
    deletion_policy = 'Delete'


class LambdaExecutePermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = EnableShapshot.Arn
    principal = 'elasticache.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    condition = 'EnableBackups'
