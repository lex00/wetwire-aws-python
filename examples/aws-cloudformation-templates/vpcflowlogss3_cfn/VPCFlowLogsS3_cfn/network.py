"""Network resources: VPCFlowLogstoS3."""

from . import *  # noqa: F403


class VPCFlowLogstoS3AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'VPC Flow Logs S3'


class VPCFlowLogstoS3(ec2.FlowLog):
    log_destination_type = 's3'
    log_destination = If("VPCFlowLogsNewBucketCondition", VPCFlowLogsBucket.Arn, Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucketName}'))
    log_format = VPCFlowLogsLogFormat
    max_aggregation_interval = VPCFlowLogsMaxAggregationInterval
    resource_id = VPCID
    resource_type = 'VPC'
    traffic_type = VPCFlowLogsTrafficType
    tags = [VPCFlowLogstoS3AssociationParameter]
