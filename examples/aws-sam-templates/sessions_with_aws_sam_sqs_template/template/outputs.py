"""Template outputs."""

from . import *  # noqa: F403


class RawSqsUrlOutput(Output):
    """URL of the SQS Queue"""

    value = RawQueue
    description = 'URL of the SQS Queue'


class DeadLetterUrlOutput(Output):
    """URL of the SQS Queue"""

    value = DeadLetter
    description = 'URL of the SQS Queue'
