"""Stack resources."""

from . import *  # noqa: F403


class HelloWorldFunction(serverless.Function):
    code_uri = 'hello-world/'
    handler = 'app.lambdaHandler'
    runtime = 'nodejs16.x'
    events = {
        'HelloWorld': {
            'Type': 'Api',
            'Properties': {
                'Path': '/',
                'Method': 'get',
            },
        },
    }


class AppLayer(serverless.LayerVersion):
    description = 'app specific deps'
    content_uri = 'layer/'
    retention_policy = 'Delete'
