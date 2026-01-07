"""Template outputs."""

from . import *  # noqa: F403


class VPCFlowLogsBucketOutput(Output):
    """S3 bucket name where VPC Flow Log data will be published"""

    value = If("VPCFlowLogsNewBucketCondition", VPCFlowLogsBucket, VPCFlowLogsBucketName)
    description = 'S3 bucket name where VPC Flow Log data will be published'
