"""Template outputs."""

from . import *  # noqa: F403


class ExecutionRoleArnOutput(Output):
    """ARN of the StackSet execution role"""

    value = AWSCloudFormationStackSetExecutionRole.Arn
    description = 'ARN of the StackSet execution role'
