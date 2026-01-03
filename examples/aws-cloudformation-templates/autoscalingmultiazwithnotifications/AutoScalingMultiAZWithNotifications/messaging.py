"""Messaging resources: NotificationTopic."""

from . import *  # noqa: F403


class NotificationTopicSubscription:
    resource: sns.Topic.Subscription
    endpoint = OperatorEMail
    protocol = 'email'


class NotificationTopic:
    resource: sns.Topic
    display_name = Sub('${AWS::StackName}-NotificationTopic')
    subscription = [NotificationTopicSubscription]
    kms_master_key_id = KmsKeyArn
