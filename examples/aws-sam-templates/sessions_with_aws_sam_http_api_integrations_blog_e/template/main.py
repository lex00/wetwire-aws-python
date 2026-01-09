"""Stack resources."""

from . import *  # noqa: F403


class MyHttpApi(serverless.HttpApi):
    definition_body = Transform(name='AWS::Include', parameters={
    'Location': './api.yaml',
})


class MyTriggeredLambda(serverless.Function):
    code_uri = 'src/'
    handler = 'app.lambdaHandler'
    runtime = 'nodejs16.x'
    policies = [{
        'SQSPollerPolicy': {
            'QueueName': MyQueue.QueueName,
        },
    }]
    events = {
        'SQSTrigger': {
            'Type': 'SQS',
            'Properties': {
                'Queue': MyQueue.Arn,
            },
        },
    }
