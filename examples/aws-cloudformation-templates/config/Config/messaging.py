"""Messaging resources: ConfigTopic, ConfigTopicPolicy."""

from . import *  # noqa: F403


class ConfigTopic:
    resource: sns.Topic


class ConfigTopicPolicyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'config.amazonaws.com',
    }
    action = 'SNS:Publish'
    resource_arn = '*'


class ConfigTopicPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ConfigTopicPolicyAllowStatement0]


class ConfigTopicPolicy:
    resource: sns.TopicPolicy
    policy_document = ConfigTopicPolicyPolicyDocument
    topics = [ConfigTopic]
