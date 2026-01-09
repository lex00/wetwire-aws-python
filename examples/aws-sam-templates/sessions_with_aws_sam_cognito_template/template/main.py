"""Stack resources."""

from . import *  # noqa: F403


class TriggerFunction(serverless.Function):
    timeout = 5
    handler = 'app.lambdaHandler'
    runtime = 'nodejs16.x'
    code_uri = 'src/'
    events = {
        'CognitoTrigger': {
            'Type': 'Cognito',
            'Properties': {
                'Trigger': 'PreTokenGeneration',
                'UserPool': UserPool,
            },
        },
    }
    condition = 'ScopeGroups'
