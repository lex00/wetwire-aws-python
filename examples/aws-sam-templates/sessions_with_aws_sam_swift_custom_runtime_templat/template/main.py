"""Stack resources."""

from . import *  # noqa: F403


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


class Squared(serverless.Function):
    pass
