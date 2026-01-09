"""Template outputs."""

from . import *  # noqa: F403


class AnalyticsStateMachineArnOutput(Output):
    """Analytics state machine ARN"""

    value = AnalyticsStateMachine
    description = 'Analytics state machine ARN'
