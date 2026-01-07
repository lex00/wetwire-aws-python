"""Messaging resources: SNSTopic, SNSSubscription."""

from . import *  # noqa: F403


class SNSTopic(sns.Topic):
    pass


class SNSSubscription(sns.Subscription):
    endpoint = SubscriptionEndPoint
    protocol = SubscriptionProtocol
    topic_arn = SNSTopic
