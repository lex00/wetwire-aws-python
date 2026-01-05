"""Messaging resources: NeptuneAlarmTopic, NeptuneAlarmSubscription."""

from . import *  # noqa: F403


class NeptuneAlarmTopic(sns.Topic):
    display_name = Sub('${AWS::StackName} alarm topic')
    condition = 'CreateSnsTopic'


class NeptuneAlarmSubscription(sns.Subscription):
    endpoint = SNSEmailSubscription
    protocol = 'email'
    topic_arn = If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)
    condition = 'CreateSnsSubscription'
