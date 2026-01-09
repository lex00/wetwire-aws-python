"""Stack resources."""

from . import *  # noqa: F403


class GenericRuleLambda(serverless.Function):
    handler = 'generic-by-params.handler'
    description = 'Validator lambda for config params'
    policies = [{
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'config:Put*',
                'config:Get*',
                'config:List*',
                'config:Describe*',
                'config:BatchGet*',
                'config:Select*',
            ],
            'Effect': 'Allow',
            'Resource': '*',
        },
    }]
