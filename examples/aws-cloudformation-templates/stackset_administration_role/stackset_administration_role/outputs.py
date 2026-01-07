"""Template outputs."""

from . import *  # noqa: F403


class AdministrationRoleArnOutput(Output):
    """ARN of the StackSet administration role"""

    value = AWSCloudFormationStackSetAdministrationRole.Arn
    description = 'ARN of the StackSet administration role'
    export_name = 'StackSetAdministrationRoleArn'
