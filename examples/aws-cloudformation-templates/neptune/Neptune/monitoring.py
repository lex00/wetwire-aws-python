"""Monitoring resources: NeptunePrimaryGremlinRequestsPerSecAlarm, NeptunePrimarySparqlRequestsPerSecAlarm, NeptunePrimaryCpuAlarm, NeptunePrimaryMemoryAlarm."""

from . import *  # noqa: F403


class NeptunePrimaryGremlinRequestsPerSecAlarmDimension(cloudwatch.Alarm.Dimension):
    name = 'DBClusterIdentifier'
    value = 'gremlin-cluster'


class NeptunePrimaryGremlinRequestsPerSecAlarm(cloudwatch.Alarm):
    alarm_description = Sub('${Env}-${AppName} primary DB Gremlin Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'GremlinRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = GremlinRequestsPerSecThreshold
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryGremlinRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]
    insufficient_data_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]


class NeptunePrimarySparqlRequestsPerSecAlarmDimension(cloudwatch.Alarm.Dimension):
    name = 'DBClusterIdentifier'
    value = NeptuneDBCluster


class NeptunePrimarySparqlRequestsPerSecAlarm(cloudwatch.Alarm):
    alarm_description = Sub('${Env}-${AppName} primary DB Sparql Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'SparqlRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = SparqlRequestsPerSecThreshold
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimarySparqlRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]
    insufficient_data_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]


class NeptunePrimaryCpuAlarmDimension(cloudwatch.Alarm.Dimension):
    name = 'DBClusterIdentifier'
    value = NeptuneDBCluster


class NeptunePrimaryCpuAlarm(cloudwatch.Alarm):
    alarm_description = Sub('${Env}-${AppName} primary DB CPU over ${HighCpuAlarmThreshold}%')
    namespace = 'AWS/Neptune'
    metric_name = 'CPUUtilization'
    unit = 'Percent'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = HighCpuAlarmThreshold
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryCpuAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]
    insufficient_data_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]


class NeptunePrimaryMemoryAlarmDimension(cloudwatch.Alarm.Dimension):
    name = 'DBClusterIdentifier'
    value = NeptuneDBCluster


class NeptunePrimaryMemoryAlarm(cloudwatch.Alarm):
    alarm_description = Sub('${Env}-${AppName} primary DB memory under ${LowMemoryAlarmThreshold} bytes')
    namespace = 'AWS/Neptune'
    metric_name = 'FreeableMemory'
    unit = 'Bytes'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = LowMemoryAlarmThreshold
    comparison_operator = 'LessThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryMemoryAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]
    insufficient_data_actions = [If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)]
