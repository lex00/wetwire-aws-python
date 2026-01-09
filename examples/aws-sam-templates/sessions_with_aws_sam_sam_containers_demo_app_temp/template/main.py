"""Stack resources."""

from . import *  # noqa: F403


class HelloWorldFunction(serverless.Function):
    package_type = 'Image'
    events = {
        'HelloWorld': {
            'Type': 'Api',
            'Properties': {
                'Path': '/hello',
                'Method': 'get',
            },
        },
    }


class GoodbyeWorldFunction(serverless.Function):
    package_type = 'Image'
    events = {
        'GoodbyeWorld': {
            'Type': 'Api',
            'Properties': {
                'Path': '/goodbye',
                'Method': 'get',
            },
        },
    }
