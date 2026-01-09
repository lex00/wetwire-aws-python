"""Stack resources."""

from . import *  # noqa: F403


class HttpApi(serverless.HttpApi):
    definition_body = {
        'openapi': '3.0',
        'info': {
            'title': Sub('${AWS::StackName}-HttpApi'),
            'version': '1.0',
        },
        'paths': {
            '/users/{id}': {
                'post': {
                    'responses': {},
                },
            },
        },
    }
    fail_on_warnings = True


class SaveUserEnvironment(serverless.Function.Environment):
    variables = {
        'TABLE_NAME': Users,
        'TABLE_ARN': Users.Arn,
    }


class SaveUser(serverless.Function):
    function_name = Sub('${AWS::StackName}-SaveUser')
    description = Sub('Stack ${StackTagName} Environment ${EnvironmentTagName} Function ${ResourceName}', {
    'ResourceName': 'SaveUser',
})
    code_uri = 'src/SaveUser'
    handler = 'Function::Function.Function::FunctionHandler'
    runtime = 'dotnetcore3.1'
    memory_size = 3008
    timeout = 30
    tracing = 'Active'
    policies = ['AWSXrayWriteOnlyAccess', {
        'DynamoDBCrudPolicy': {
            'TableName': Users,
        },
    }]
    events = {
        'HttpApiPOSTusersid': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/users/{id}',
                'Method': 'POST',
                'ApiId': HttpApi,
                'PayloadFormatVersion': '2.0',
                'TimeoutInMillis': 29000,
            },
        },
    }
    environment = SaveUserEnvironment
