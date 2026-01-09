"""Stack resources."""

from . import *  # noqa: F403


class AnalyticsTablePrimaryKey(serverless.SimpleTable.PrimaryKey):
    name = 'Id'
    type_ = 'String'


class AnalyticsTableProvisionedThroughput(serverless.SimpleTable.ProvisionedThroughput):
    read_capacity_units = 1
    write_capacity_units = 1


class AnalyticsTable(serverless.SimpleTable):
    primary_key = AnalyticsTablePrimaryKey
    provisioned_throughput = AnalyticsTableProvisionedThroughput


class GatherStackOverflowMetrics(serverless.StateMachine):
    definition_uri = 'statemachine/stackoverflow.asl.json'
    definition_substitutions = {
        'DDBPutItem': Sub('arn:${AWS::Partition}:states:::dynamodb:putItem'),
        'DDBTable': AnalyticsTable,
    }
    type_ = 'EXPRESS'
    policies = [{
        'DynamoDBWritePolicy': {
            'TableName': AnalyticsTable,
        },
    }]


class GatherTwitchMetrics(serverless.StateMachine):
    definition_uri = 'statemachine/twitch.asl.json'
    definition_substitutions = {
        'DDBPutItem': Sub('arn:${AWS::Partition}:states:::dynamodb:putItem'),
        'DDBTable': AnalyticsTable,
    }
    type_ = 'EXPRESS'
    policies = [{
        'DynamoDBWritePolicy': {
            'TableName': AnalyticsTable,
        },
    }]


class AnalyticsStateMachine(serverless.StateMachine):
    definition_uri = 'statemachine/analytics.asl.json'
    definition_substitutions = {
        'SNSTopicArn': AnalyticsTopic,
        'StackOverflowWorkflowArn': GatherStackOverflowMetrics,
        'TwitchWorkflowArn': GatherTwitchMetrics,
    }
    events = {
        'DailySchedule': {
            'Type': 'Schedule',
            'Properties': {
                'Description': 'Schedule to run the analytics state machine every day',
                'Enabled': True,
                'Schedule': 'rate(1 day)',
            },
        },
    }
    role = AnalyticsWorkflowRole.Arn
