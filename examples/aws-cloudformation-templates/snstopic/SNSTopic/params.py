"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class SubscriptionEndPoint(Parameter):
    """The endpoint that receives notifications from the Amazon SNS topic. The endpoint value depends on the protocol that you specify. This could be a URL or ARN"""

    type = STRING
    description = 'The endpoint that receives notifications from the Amazon SNS topic. The endpoint value depends on the protocol that you specify. This could be a URL or ARN'


class SubscriptionProtocol(Parameter):
    """The subscription's protocol"""

    type = STRING
    description = "The subscription's protocol"
    default = 'sqs'
    allowed_values = [
    'http',
    'https',
    'email',
    'email-json',
    'sms',
    'sqs',
    'application',
    'lambda',
]
