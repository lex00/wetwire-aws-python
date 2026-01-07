"""Template outputs."""

from . import *  # noqa: F403


class TopicARNOutput(Output):
    """ARN of newly created SNS Topic"""

    value = SNSTopic
    description = 'ARN of newly created SNS Topic'


class QueueNameOutput(Output):
    """Name of newly created SNS Topic"""

    value = SNSTopic.TopicName
    description = 'Name of newly created SNS Topic'
