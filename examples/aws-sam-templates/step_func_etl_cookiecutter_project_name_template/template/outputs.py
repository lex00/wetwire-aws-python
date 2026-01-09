"""Template outputs."""

from . import *  # noqa: F403


class StateMachineRoleArnOutput(Output):
    """IAM role ARN"""

    value = StateMachineRole.Arn
    description = 'IAM role ARN'


class StateMachineArnOutput(Output):
    """State machine ARN"""

    value = StateMachine.Arn
    description = 'State machine ARN'


class FnCheckArnOutput(Output):
    """Check function ARN"""

    value = FnCheck.Arn
    description = 'Check function ARN'


class FnSuccessArnOutput(Output):
    """Success function ARN"""

    value = FnSuccess.Arn
    description = 'Success function ARN'


class FnFailureArnOutput(Output):
    """Failure function ARN"""

    value = FnFailure.Arn
    description = 'Failure function ARN'
