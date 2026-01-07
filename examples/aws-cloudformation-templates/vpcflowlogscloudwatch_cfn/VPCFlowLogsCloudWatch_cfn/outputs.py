"""Template outputs."""

from . import *  # noqa: F403


class VPCFlowLogsLogGroupOutput(Output):
    """CloudWatch Log Group where VPC Flow Log data will be published"""

    value = VPCFlowLogsLogGroup
    description = 'CloudWatch Log Group where VPC Flow Log data will be published'
