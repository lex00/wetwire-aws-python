"""Stack resources."""

from . import *  # noqa: F403


class Channel(iotanalytics.Channel):
    channel_name = Sub('${ProjectName}_channel')
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]


class Datastore(iotanalytics.Datastore):
    datastore_name = Sub('${ProjectName}_datastore')
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]


class SqlDatasetQueryAction(iotanalytics.Dataset.QueryAction):
    sql_query = SqlQuery


class SqlDatasetAction(iotanalytics.Dataset.Action):
    action_name = 'SqlAction'
    query_action = SqlDatasetQueryAction


class SqlDatasetSchedule(iotanalytics.Dataset.Schedule):
    schedule_expression = ScheduleExpression


class SqlDatasetTrigger(iotanalytics.Dataset.Trigger):
    schedule = SqlDatasetSchedule


class SqlDatasetRetentionPeriod(iotanalytics.Channel.RetentionPeriod):
    unlimited = False
    number_of_days = 30


class SqlDataset(iotanalytics.Dataset):
    dataset_name = Sub('${ProjectName}_dataset')
    actions = [SqlDatasetAction]
    triggers = [SqlDatasetTrigger]
    retention_period = SqlDatasetRetentionPeriod
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]
    depends_on = [Datastore]


class PipelineChannel(iotanalytics.Pipeline.Channel):
    name = 'ChannelActivity'
    channel_name = Sub('${ProjectName}_channel')
    next = 'DatastoreActivity'


class PipelineDatastore(iotanalytics.Pipeline.Datastore):
    name = 'DatastoreActivity'
    datastore_name = Sub('${ProjectName}_datastore')


class PipelineActivity(iotanalytics.Pipeline.Activity):
    channel = PipelineChannel
    datastore = PipelineDatastore


class Pipeline(iotanalytics.Pipeline):
    pipeline_name = Sub('${ProjectName}_pipeline')
    pipeline_activities = [PipelineActivity]
    tags = [{
        'Key': 'Project',
        'Value': ProjectName,
    }]
    depends_on = [Channel, Datastore]
