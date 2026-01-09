"""Stack resources."""

from . import *  # noqa: F403


class Squared(serverless.Function):
    pass


class SwiftApi(serverless.Function):
    events = {
        'ApiTrigger': {
            'Type': 'Api',
            'Properties': {
                'Path': '/',
                'Method': 'get',
            },
        },
    }
