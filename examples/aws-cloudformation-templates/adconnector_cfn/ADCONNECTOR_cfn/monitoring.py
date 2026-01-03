"""Monitoring resources: ADConnectorLambdaLogsLogGroup."""

from . import *  # noqa: F403


class ADConnectorLambdaLogsLogGroup:
    resource: logs.LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = LambdaLogsLogGroupRetention
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", LambdaLogsCloudWatchKMSKey, AWS_NO_VALUE)
    deletion_policy = 'Retain'
