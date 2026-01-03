"""Messaging resources: MyDeadLetterQueue, SQSQueue."""

from . import *  # noqa: F403


class MyDeadLetterQueue:
    resource: sqs.Queue
    fifo_queue = 'true'
    queue_name = Join('', [
    QueueName,
    'Deadletter',
    '.fifo',
])
    message_retention_period = 1209600
    condition = 'CreateDeadLetterQueue'


class SQSQueue:
    resource: sqs.Queue
    content_based_deduplication = ContentBasedDeduplication
    fifo_queue = 'true'
    queue_name = Join('', [
    QueueName,
    '.fifo',
])
    maximum_message_size = MaximumMessageSize
    message_retention_period = MessageRetentionPeriod
    receive_message_wait_time_seconds = ReceiveMessageWaitTimeSeconds
    redrive_policy = If("CreateDeadLetterQueue", {
    'deadLetterTargetArn': MyDeadLetterQueue.Arn,
    'maxReceiveCount': 5,
}, AWS_NO_VALUE)
    visibility_timeout = VisibilityTimeout
