"""Monitoring resources: CPUAlarmHigh, CPUAlarmLow."""

from . import *  # noqa: F403


class CPUAlarmHighDimension(cloudwatch.Alarm.Dimension):
    name = 'AutoScalingGroupName'
    value = AutoScalingGroup


class CPUAlarmHigh(cloudwatch.Alarm):
    resource: cloudwatch.Alarm
    alarm_actions = [ScaleUpPolicy]
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    comparison_operator = 'GreaterThanThreshold'
    dimensions = [CPUAlarmHighDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '90'


class CPUAlarmLowDimension(cloudwatch.Alarm.Dimension):
    name = 'AutoScalingGroupName'
    value = AutoScalingGroup


class CPUAlarmLow(cloudwatch.Alarm):
    resource: cloudwatch.Alarm
    alarm_actions = [ScaleDownPolicy]
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    comparison_operator = 'LessThanThreshold'
    dimensions = [CPUAlarmLowDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '70'
