"""Template outputs."""

from . import *  # noqa: F403


class QueueURLOutput:
    """URL of newly created SQS Queue"""

    resource: Output
    value = SQSQueue
    description = 'URL of newly created SQS Queue'


class QueueARNOutput:
    """ARN of newly created SQS Queue"""

    resource: Output
    value = SQSQueue.Arn
    description = 'ARN of newly created SQS Queue'


class QueueNameOutput:
    """Name newly created SQS Queue"""

    resource: Output
    value = SQSQueue.QueueName
    description = 'Name newly created SQS Queue'
