"""Monitoring resources: FirehoseLogGroup, FirehoseLogStream."""

from . import *  # noqa: F403


class FirehoseLogGroup:
    resource: logs.LogGroup
    log_group_name = Join('', [
    '/aws/kinesisfirehose/',
    LogGroupName,
])
    retention_in_days = CloudWatchLogGroupRetention
    kms_key_id = If("CloudWatchLogsKMSKeyCondition", CloudWatchLogsKMSKey, AWS_NO_VALUE)


class FirehoseLogStream:
    resource: logs.LogStream
    log_group_name = FirehoseLogGroup
    log_stream_name = LogStreamName
