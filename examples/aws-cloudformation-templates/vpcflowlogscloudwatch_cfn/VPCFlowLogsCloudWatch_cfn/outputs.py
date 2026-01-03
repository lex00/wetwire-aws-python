"""Template outputs."""

from . import *  # noqa: F403


class VPCFlowLogsLogGroupOutput:
    """CloudWatch Log Group where VPC Flow Log data will be published"""

    resource: Output
    value = VPCFlowLogsLogGroup
    description = 'CloudWatch Log Group where VPC Flow Log data will be published'
