"""Monitoring resources: CloudwatchLogsGroup, ALB500sAlarmScaleUp."""

from . import *  # noqa: F403


class CloudwatchLogsGroup(logs.LogGroup):
    log_group_name = Join('-', [
    'ECSLogGroup',
    AWS_STACK_NAME,
])
    retention_in_days = 14
    kms_key_id = LogsKmsKey


class ALB500sAlarmScaleUpDimension:
    resource: cloudwatch.Alarm.Dimension
    name = 'ECSService'
    value = Service


class ALB500sAlarmScaleUp(cloudwatch.Alarm):
    evaluation_periods = '1'
    statistic = 'Average'
    threshold = '10'
    alarm_description = 'Alarm if our ALB generates too many HTTP 500s.'
    period = '60'
    alarm_actions = [ServiceScalingPolicy]
    namespace = 'AWS/ApplicationELB'
    dimensions = [ALB500sAlarmScaleUpDimension]
    comparison_operator = 'GreaterThanThreshold'
    metric_name = 'HTTPCode_ELB_5XX_Count'
