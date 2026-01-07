"""Stack resources."""

from . import *  # noqa: F403


class DeliveryStreamDeliveryStreamEncryptionConfigurationInput(kinesisfirehose.DeliveryStream.DeliveryStreamEncryptionConfigurationInput):
    key_type = 'AWS_OWNED_CMK'


class DeliveryStreamCloudWatchLoggingOptions(kinesisfirehose.DeliveryStream.CloudWatchLoggingOptions):
    enabled = True
    log_group_name = FirehoseLogGroup
    log_stream_name = FirehoseLogStream


class DeliveryStreamProcessorParameter(kinesisfirehose.DeliveryStream.ProcessorParameter):
    parameter_name = 'Delimiter'
    parameter_value = '\\n'


class DeliveryStreamProcessor(kinesisfirehose.DeliveryStream.Processor):
    type_ = 'AppendDelimiterToRecord'
    parameters = [DeliveryStreamProcessorParameter]


class DeliveryStreamProcessingConfiguration(kinesisfirehose.DeliveryStream.ProcessingConfiguration):
    enabled = True
    processors = [DeliveryStreamProcessor]


class DeliveryStreamExtendedS3DestinationConfiguration(kinesisfirehose.DeliveryStream.ExtendedS3DestinationConfiguration):
    cloud_watch_logging_options = DeliveryStreamCloudWatchLoggingOptions
    role_arn = DeliveryRole.Arn
    bucket_arn = Join('', [
    'arn:aws:s3:::',
    DestinationBucketName,
])
    error_output_prefix = 'errors/'
    processing_configuration = DeliveryStreamProcessingConfiguration


class DeliveryStream(kinesisfirehose.DeliveryStream):
    delivery_stream_name = DeliveryStreamName
    delivery_stream_type = 'DirectPut'
    delivery_stream_encryption_configuration_input = DeliveryStreamDeliveryStreamEncryptionConfigurationInput
    extended_s3_destination_configuration = DeliveryStreamExtendedS3DestinationConfiguration
