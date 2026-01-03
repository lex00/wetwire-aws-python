"""Template outputs."""

from . import *  # noqa: F403


class VPCFlowLogsBucketOutput:
    """S3 bucket name where VPC Flow Log data will be published"""

    resource: Output
    value = If("VPCFlowLogsNewBucketCondition", VPCFlowLogsBucket, VPCFlowLogsBucketName)
    description = 'S3 bucket name where VPC Flow Log data will be published'
