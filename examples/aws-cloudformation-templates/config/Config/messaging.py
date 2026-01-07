"""Messaging resources: ConfigTopic, ConfigTopicPolicy."""

from . import *  # noqa: F403


class ConfigTopic(sns.Topic):
    resource: sns.Topic


class ConfigTopicPolicyAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'config.amazonaws.com',
    }
    action = 'SNS:Publish'
    resource_arn = '*'


class ConfigTopicPolicyPolicyDocument(PolicyDocument):
    statement = [ConfigTopicPolicyAllowStatement0]


class ConfigTopicPolicy(sns.TopicPolicy):
    resource: sns.TopicPolicy
    policy_document = ConfigTopicPolicyPolicyDocument
    topics = [ConfigTopic]
