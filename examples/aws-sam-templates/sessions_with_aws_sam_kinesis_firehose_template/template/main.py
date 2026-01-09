"""Stack resources."""

from . import *  # noqa: F403


class ProcessFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'TABLE_NAME': ProcessedDataTable,
    }


class ProcessFunction(serverless.Function):
    timeout = 180
    code_uri = 'src/'
    handler = 'process.handler'
    runtime = 'nodejs16.x'
    policies = [{
        'DynamoDBCrudPolicy': {
            'TableName': ProcessedDataTable,
        },
    }]
    environment = ProcessFunctionEnvironment


class CountTable(serverless.SimpleTable):
    pass


class CountFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'TABLE_NAME': CountTable,
    }


class CountFunction(serverless.Function):
    timeout = 180
    code_uri = 'src/'
    handler = 'count.handler'
    runtime = 'nodejs16.x'
    policies = [{
        'DynamoDBCrudPolicy': {
            'TableName': CountTable,
        },
    }]
    environment = CountFunctionEnvironment


class FirehoseProcessorParameter(kinesisfirehose.DeliveryStream.ProcessorParameter):
    parameter_name = 'LambdaArn'
    parameter_value = ProcessFunction.Arn


class FirehoseProcessor(kinesisfirehose.DeliveryStream.Processor):
    type_ = 'Lambda'
    parameters = [FirehoseProcessorParameter]


class FirehoseProcessingConfiguration(kinesisfirehose.DeliveryStream.ProcessingConfiguration):
    enabled = True
    processors = [FirehoseProcessor]


class FirehoseAmazonOpenSearchServerlessBufferingHints(kinesisfirehose.DeliveryStream.AmazonOpenSearchServerlessBufferingHints):
    interval_in_seconds = 60
    size_in_m_bs = 1


class FirehoseAmazonOpenSearchServerlessBufferingHints1(kinesisfirehose.DeliveryStream.AmazonOpenSearchServerlessBufferingHints):
    interval_in_seconds = 60
    size_in_m_bs = 1


class FirehoseS3DestinationConfiguration(kinesisfirehose.DeliveryStream.S3DestinationConfiguration):
    bucket_arn = RawDataBucket.Arn
    compression_format = 'GZIP'
    role_arn = FirehoseAccessRole.Arn
    buffering_hints = FirehoseAmazonOpenSearchServerlessBufferingHints1


class FirehoseExtendedS3DestinationConfiguration(kinesisfirehose.DeliveryStream.ExtendedS3DestinationConfiguration):
    bucket_arn = ProcessedDataBucket.Arn
    compression_format = 'GZIP'
    role_arn = FirehoseAccessRole.Arn
    processing_configuration = FirehoseProcessingConfiguration
    buffering_hints = FirehoseAmazonOpenSearchServerlessBufferingHints
    s3_backup_mode = 'Enabled'
    s3_backup_configuration = FirehoseS3DestinationConfiguration


class Firehose(kinesisfirehose.DeliveryStream):
    delivery_stream_type = 'DirectPut'
    extended_s3_destination_configuration = FirehoseExtendedS3DestinationConfiguration


class KinesisAnalyticsAppRecordColumn(kinesisanalyticsv2.Application.RecordColumn):
    name = 'requestId'
    mapping = '$.requestId'
    sql_type = 'bigint'


class KinesisAnalyticsAppRecordColumn1(kinesisanalyticsv2.Application.RecordColumn):
    name = 'ip'
    mapping = '$.ip'
    sql_type = 'varchar(16)'


class KinesisAnalyticsAppRecordColumn2(kinesisanalyticsv2.Application.RecordColumn):
    name = 'status'
    mapping = '$.status'
    sql_type = 'varchar(8)'


class KinesisAnalyticsAppRecordColumn3(kinesisanalyticsv2.Application.RecordColumn):
    name = 'resourcePath'
    mapping = '$.resourcePath'
    sql_type = 'varchar(16)'


class KinesisAnalyticsAppDestinationSchema(kinesisanalyticsv2.ApplicationOutput.DestinationSchema):
    record_format_type = 'JSON'


class KinesisAnalyticsAppInputSchema(kinesisanalyticsv2.Application.InputSchema):
    record_columns = [KinesisAnalyticsAppRecordColumn, KinesisAnalyticsAppRecordColumn1, KinesisAnalyticsAppRecordColumn2, KinesisAnalyticsAppRecordColumn3]
    record_format = KinesisAnalyticsAppDestinationSchema


class KinesisAnalyticsAppInput(kinesisanalyticsv2.Application.Input):
    input_schema = KinesisAnalyticsAppInputSchema
    kinesis_firehose_input = {
        'ResourceARN': Firehose.Arn,
        'RoleARN': KinesisAnalyticsAccessRole.Arn,
    }
    name_prefix = 'SESSIONS_STREAM'


class KinesisAnalyticsApp(kinesisanalytics.Application):
    application_code = """CREATE OR REPLACE STREAM "LINK_STREAM" ("resourcePath" varchar(16), link_count INTEGER); CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "LINK_STREAM" SELECT STREAM "resourcePath", COUNT(*) AS link_count
    FROM "SESSIONS_STREAM_001"
    GROUP BY "resourcePath", STEP("SESSIONS_STREAM_001".ROWTIME BY INTERVAL '10' SECOND);
"""
    inputs = [KinesisAnalyticsAppInput]


class KinesisAnalyticsOutputDestinationSchema(kinesisanalyticsv2.ApplicationOutput.DestinationSchema):
    record_format_type = 'JSON'


class KinesisAnalyticsOutputOutput(kinesisanalyticsv2.ApplicationOutput.Output):
    destination_schema = KinesisAnalyticsOutputDestinationSchema
    lambda_output = {
        'ResourceARN': CountFunction.Arn,
        'RoleARN': KinesisAnalyticsAccessRole.Arn,
    }
    name = 'LINK_STREAM'


class KinesisAnalyticsOutput(kinesisanalytics.ApplicationOutput):
    application_name = KinesisAnalyticsApp
    output = KinesisAnalyticsOutputOutput
