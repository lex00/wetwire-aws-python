"""Monitoring resources: VPCFlowLogsLogGroup."""

from . import *  # noqa: F403


class VPCFlowLogsLogGroup(logs.LogGroup):
    retention_in_days = VPCFlowLogsLogGroupRetention
    kms_key_id = If("VPCFlowLogsCloudWatchKMSKeyCondition", VPCFlowLogsCloudWatchKMSKey, AWS_NO_VALUE)
