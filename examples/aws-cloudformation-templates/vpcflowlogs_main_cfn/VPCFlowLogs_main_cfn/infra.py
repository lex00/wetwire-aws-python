"""Infra resources: VPCFlowLogsS3Stack, VPCFlowLogsCloudWatchStack."""

from . import *  # noqa: F403


class VPCFlowLogsS3Stack(cloudformation.Stack):
    resource: cloudformation.Stack
    template_url = Sub('https://${TemplatesS3BucketName}.s3.${TemplatesS3BucketRegion}.${AWS::URLSuffix}/templates/VPCFlowLogsS3.cfn.yaml')
    parameters = {
        'S3AccessLogsBucketName': S3AccessLogsBucketName,
        'VPCFlowLogsBucketKeyEnabled': VPCFlowLogsBucketKeyEnabled,
        'VPCFlowLogsBucketKMSKey': VPCFlowLogsBucketKMSKey,
        'VPCFlowLogsBucketName': VPCFlowLogsBucketName,
        'VPCFlowLogsLogFormat': VPCFlowLogsLogFormat,
        'VPCFlowLogsMaxAggregationInterval': VPCFlowLogsMaxAggregationInterval,
        'VPCFlowLogsTrafficType': VPCFlowLogsTrafficType,
        'VPCID': VPCID,
    }
    condition = 'VPCFlowLogsToS3Condition'


class VPCFlowLogsCloudWatchStack(cloudformation.Stack):
    resource: cloudformation.Stack
    template_url = Sub('https://${TemplatesS3BucketName}.s3.${TemplatesS3BucketRegion}.${AWS::URLSuffix}/templates/VPCFlowLogsCloudWatch.cfn.yaml')
    parameters = {
        'VPCFlowLogsCloudWatchKMSKey': VPCFlowLogsCloudWatchKMSKey,
        'VPCFlowLogsLogFormat': VPCFlowLogsLogFormat,
        'VPCFlowLogsLogGroupRetention': VPCFlowLogsLogGroupRetention,
        'VPCFlowLogsMaxAggregationInterval': VPCFlowLogsMaxAggregationInterval,
        'VPCFlowLogsTrafficType': VPCFlowLogsTrafficType,
        'VPCID': VPCID,
    }
    condition = 'VPCFlowLogsToCloudWatchCondition'
