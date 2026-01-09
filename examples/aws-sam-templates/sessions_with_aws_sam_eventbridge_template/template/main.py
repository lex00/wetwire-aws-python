"""Stack resources."""

from . import *  # noqa: F403


class EndpointFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'EVENT_BUS_NAME': CustomBus,
    }


class EndpointFunction(serverless.Function):
    handler = 'endpoint.lambdaHandler'
    policies = [{
        'EventBridgePutEventsPolicy': {
            'EventBusName': CustomBus,
        },
    }]
    environment = EndpointFunctionEnvironment
    events = {
        'API': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/',
                'Method': 'POST',
            },
        },
    }


class TranslateFunctionAllowStatement0(PolicyStatement):
    action = ['translate:TranslateText']
    resource_arn = '*'


class TranslateFunctionPolicies1(PolicyDocument):
    statement = [TranslateFunctionAllowStatement0]


class TranslateFunction(serverless.Function):
    handler = 'translate.lambdaHandler'
    policies = [{
        'ComprehendBasicAccessPolicy': {},
    }, TranslateFunctionPolicies1]
    events = {
        'TranslateFilter': {
            'Type': 'EventBridgeRule',
            'Properties': {
                'EventBusName': CustomBus,
                'Pattern': {
                    'source': ['TextEndpoint'],
                    'detail-type': ['translate'],
                },
            },
        },
    }


class SentimentFunction(serverless.Function):
    handler = 'sentiment.lambdaHandler'
    policies = [{
        'ComprehendBasicAccessPolicy': {},
    }]
    events = {
        'SentimentFilter': {
            'Type': 'EventBridgeRule',
            'Properties': {
                'EventBusName': CustomBus,
                'Pattern': {
                    'source': ['TextEndpoint'],
                    'detail-type': ['sentiment'],
                },
            },
        },
    }
