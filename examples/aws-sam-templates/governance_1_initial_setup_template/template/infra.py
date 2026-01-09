"""Infra resources: DeliveryChannel, ConfigRecorder."""

from . import *  # noqa: F403


class DeliveryChannel(config.DeliveryChannel):
    s3_bucket_name = DataBucket
    sns_topic_arn = NotificationTopic


class ConfigRecorderRecordingGroup(config.ConfigurationRecorder.RecordingGroup):
    include_global_resource_types = If("IsMainRegion", True, False)
    all_supported = True


class ConfigRecorder(config.ConfigurationRecorder):
    name = Sub('${AWS::Region}-Config-Recorder')
    recording_group = ConfigRecorderRecordingGroup
    role_arn = ConfigRole.Arn
