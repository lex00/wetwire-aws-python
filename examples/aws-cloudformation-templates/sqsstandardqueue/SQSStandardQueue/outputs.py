"""Template outputs."""

from . import *  # noqa: F403


class QueueURLOutput(Output):
    """URL of newly created SQS Queue"""

    value = SQSQueue
    description = 'URL of newly created SQS Queue'


class QueueARNOutput(Output):
    """ARN of newly created SQS Queue"""

    value = SQSQueue.Arn
    description = 'ARN of newly created SQS Queue'


class QueueNameOutput(Output):
    """Name newly created SQS Queue"""

    value = SQSQueue.QueueName
    description = 'Name newly created SQS Queue'


class DeadLetterQueueURLOutput(Output):
    """URL of the dead letter queue"""

    value = MyDeadLetterQueue
    description = 'URL of the dead letter queue'
    condition = 'CreateDeadLetterQueue'


class DeadLetterQueueARNOutput(Output):
    """ARN of the dead letter queue"""

    value = MyDeadLetterQueue.Arn
    description = 'ARN of the dead letter queue'
    condition = 'CreateDeadLetterQueue'
