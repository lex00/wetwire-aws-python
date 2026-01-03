"""Template outputs."""

from . import *  # noqa: F403


class AdministrationRoleArnOutput:
    """ARN of the StackSet administration role"""

    resource: Output
    value = AWSCloudFormationStackSetAdministrationRole.Arn
    description = 'ARN of the StackSet administration role'
    export_name = 'StackSetAdministrationRoleArn'
