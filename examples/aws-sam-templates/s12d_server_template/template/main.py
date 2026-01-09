"""Stack resources."""

from . import *  # noqa: F403


class LoggingStream(kinesis.Stream):
    shard_count = 1


class SiteAPI(serverless.Api):
    stage_name = 'Prod'
    endpoint_configuration = 'REGIONAL'
    tracing_enabled = True
    method_settings = [{
        'HttpMethod': '*',
        'ResourcePath': '/*',
        'LoggingLevel': 'INFO',
        'DataTraceEnabled': True,
        'MetricsEnabled': True,
        'ThrottlingRateLimit': 2000,
        'ThrottlingBurstLimit': 1000,
    }, {
        'HttpMethod': 'GET',
        'ResourcePath': '/{linkId}',
        'ThrottlingRateLimit': 10000,
        'ThrottlingBurstLimit': 4000,
    }]
    definition_body = Transform(name='AWS::Include', parameters={
    'Location': './api.yaml',
})


class LoggingProcessorEnvironment(serverless.Function.Environment):
    variables = {
        'TABLE_NAME': LinkTable,
    }


class LoggingProcessor(serverless.Function):
    runtime = 'nodejs16.x'
    code_uri = 'src/analytics/'
    handler = 'app.handler'
    memory_size = 1024
    timeout = 45
    tracing = 'Active'
    policies = [{
        'DynamoDBWritePolicy': {
            'TableName': LinkTable,
        },
    }, {
        'SQSSendMessagePolicy': {
            'QueueName': LoggingDLQ.QueueName,
        },
    }]
    environment = LoggingProcessorEnvironment
    events = {
        'KinesisTrigger': {
            'Type': 'Kinesis',
            'Properties': {
                'StartingPosition': 'TRIM_HORIZON',
                'Stream': LoggingStream.Arn,
                'BisectBatchOnFunctionError': True,
                'MaximumBatchingWindowInSeconds': 15,
                'MaximumRetryAttempts': 3,
                'DestinationConfig': {
                    'OnFailure': {
                        'Destination': LoggingDLQ.Arn,
                    },
                },
            },
        },
    }
