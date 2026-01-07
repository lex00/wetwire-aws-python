"""Network resources: VPCFlowLogsToCloudWatch."""

from . import *  # noqa: F403


class VPCFlowLogsToCloudWatchAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'VPC Flow Logs CloudWatch'


class VPCFlowLogsToCloudWatch(ec2.FlowLog):
    log_destination_type = 'cloud-watch-logs'
    log_group_name = VPCFlowLogsLogGroup
    deliver_logs_permission_arn = VPCFlowLogsRole.Arn
    log_format = VPCFlowLogsLogFormat
    max_aggregation_interval = VPCFlowLogsMaxAggregationInterval
    resource_id = VPCID
    resource_type = 'VPC'
    traffic_type = VPCFlowLogsTrafficType
    tags = [VPCFlowLogsToCloudWatchAssociationParameter]
