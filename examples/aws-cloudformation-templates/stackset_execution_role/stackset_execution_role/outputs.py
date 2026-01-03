"""Template outputs."""

from . import *  # noqa: F403


class ExecutionRoleArnOutput:
    """ARN of the StackSet execution role"""

    resource: Output
    value = AWSCloudFormationStackSetExecutionRole.Arn
    description = 'ARN of the StackSet execution role'
