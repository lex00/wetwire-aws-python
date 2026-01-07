"""Messaging resources: DirectoryMonitoringTopic."""

from . import *  # noqa: F403


class DirectoryMonitoringTopicSubscription(sns.Topic.Subscription):
    endpoint = DirectoryMonitoringEmail
    protocol = 'email'


class DirectoryMonitoringTopic(sns.Topic):
    resource: sns.Topic
    kms_master_key_id = If("DirectoryMonitoringSNSTopicKMSKeyCondition", DirectoryMonitoringSNSTopicKMSKey, 'aws/sns')
    subscription = [DirectoryMonitoringTopicSubscription]
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }, {
        'Key': 'DirectoryID',
        'Value': DirectoryID,
    }]
