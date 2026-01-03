"""Monitoring resources: CPUAlarmHigh, CPUAlarmLow."""

from . import *  # noqa: F403


class CPUAlarmHighDimension:
    resource: cloudwatch.Alarm.Dimension
    name = 'AutoScalingGroupName'
    value = WebServerGroup


class CPUAlarmHigh:
    resource: cloudwatch.Alarm
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 90
    alarm_actions = [WebServerScaleUpPolicy]
    dimensions = [CPUAlarmHighDimension]
    comparison_operator = 'GreaterThanThreshold'


class CPUAlarmLowDimension:
    resource: cloudwatch.Alarm.Dimension
    name = 'AutoScalingGroupName'
    value = WebServerGroup


class CPUAlarmLow:
    resource: cloudwatch.Alarm
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 70
    alarm_actions = [WebServerScaleDownPolicy]
    dimensions = [CPUAlarmLowDimension]
    comparison_operator = 'LessThanThreshold'
