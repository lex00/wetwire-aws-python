"""Stack resources."""

from . import *  # noqa: F403


class Datastore:
    resource: iotanalytics.Datastore
    datastore_name = Sub('${ProjectName}_datastore')
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]


class Channel:
    resource: iotanalytics.Channel
    channel_name = Sub('${ProjectName}_channel')
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]


class SqlDatasetQueryAction:
    resource: iotanalytics.Dataset.QueryAction
    sql_query = SqlQuery


class SqlDatasetAction:
    resource: iotanalytics.Dataset.Action
    action_name = 'SqlAction'
    query_action = SqlDatasetQueryAction


class SqlDatasetSchedule:
    resource: iotanalytics.Dataset.Schedule
    schedule_expression = ScheduleExpression


class SqlDatasetTrigger:
    resource: iotanalytics.Dataset.Trigger
    schedule = SqlDatasetSchedule


class SqlDatasetRetentionPeriod:
    resource: iotanalytics.Channel.RetentionPeriod
    unlimited = False
    number_of_days = 30


class SqlDataset:
    resource: iotanalytics.Dataset
    dataset_name = Sub('${ProjectName}_dataset')
    actions = [SqlDatasetAction]
    triggers = [SqlDatasetTrigger]
    retention_period = SqlDatasetRetentionPeriod
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]
    depends_on = [Datastore]


class PipelineChannel:
    resource: iotanalytics.Pipeline.Channel
    name = 'ChannelActivity'
    channel_name = Sub('${ProjectName}_channel')
    next = 'DatastoreActivity'


class PipelineDatastore:
    resource: iotanalytics.Pipeline.Datastore
    name = 'DatastoreActivity'
    datastore_name = Sub('${ProjectName}_datastore')


class PipelineActivity:
    resource: iotanalytics.Pipeline.Activity
    channel = PipelineChannel
    datastore = PipelineDatastore


class Pipeline:
    resource: iotanalytics.Pipeline
    pipeline_name = Sub('${ProjectName}_pipeline')
    pipeline_activities = [PipelineActivity]
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]
    depends_on = [Channel, Datastore]
