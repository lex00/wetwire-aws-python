"""Stack resources."""

from . import *  # noqa: F403


class HelloWorldFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'PARAM1': 'VALUE',
    }


class HelloWorldFunction(serverless.Function):
    code_uri = 'hello-world/'
    handler = 'bootstrap'
    runtime = 'provided.al2'
    tracing = 'Active'
    events = {
        'CatchAll': {
            'Type': 'Api',
            'Properties': {
                'Path': '/hello',
                'Method': 'GET',
            },
        },
    }
    environment = HelloWorldFunctionEnvironment
