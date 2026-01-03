"""Messaging resources: MyDeadLetterQueue, SQSQueue."""

from . import *  # noqa: F403


class MyDeadLetterQueue:
    resource: sqs.Queue
    message_retention_period = 1209600
    condition = 'CreateDeadLetterQueue'


class SQSQueue:
    resource: sqs.Queue
    delay_seconds = DelaySeconds
    maximum_message_size = MaximumMessageSize
    message_retention_period = MessageRetentionPeriod
    receive_message_wait_time_seconds = ReceiveMessageWaitTimeSeconds
    kms_master_key_id = If("IsKmsExist", KmsMasterKeyIdForSqs, AWS_NO_VALUE)
    redrive_policy = If("CreateDeadLetterQueue", {
    'deadLetterTargetArn': MyDeadLetterQueue.Arn,
    'maxReceiveCount': 5,
}, AWS_NO_VALUE)
    visibility_timeout = VisibilityTimeout
