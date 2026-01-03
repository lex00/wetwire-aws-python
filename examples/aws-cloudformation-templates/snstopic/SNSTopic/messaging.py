"""Messaging resources: SNSTopic, SNSSubscription."""

from . import *  # noqa: F403


class SNSTopic:
    resource: sns.Topic


class SNSSubscription:
    resource: sns.Subscription
    endpoint = SubscriptionEndPoint
    protocol = SubscriptionProtocol
    topic_arn = SNSTopic
