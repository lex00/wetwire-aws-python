"""Template outputs."""

from . import *  # noqa: F403


class TopicARNOutput:
    """ARN of newly created SNS Topic"""

    resource: Output
    value = SNSTopic
    description = 'ARN of newly created SNS Topic'


class QueueNameOutput:
    """Name of newly created SNS Topic"""

    resource: Output
    value = SNSTopic.TopicName
    description = 'Name of newly created SNS Topic'
