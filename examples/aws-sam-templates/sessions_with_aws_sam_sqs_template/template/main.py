"""Stack resources."""

from . import *  # noqa: F403


class TriggeredFunction(serverless.Function):
    handler = 'app.lambdaHandler'
    events = {
        'SQSEvent': {
            'Type': 'SQS',
            'Properties': {
                'Queue': RawQueue.Arn,
                'BatchSize': 10,
                'Enabled': True,
            },
        },
    }
