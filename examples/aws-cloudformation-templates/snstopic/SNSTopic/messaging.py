"""Messaging resources: SNSTopic, SNSSubscription."""

from . import *  # noqa: F403


class SNSTopic(sns.Topic):
    resource: sns.Topic


class SNSSubscription(sns.Subscription):
    resource: sns.Subscription
    endpoint = SubscriptionEndPoint
    protocol = SubscriptionProtocol
    topic_arn = SNSTopic
