"""Infra resources: ConfigRecorder, AggragateAccountAuth, DeliveryChannel, AggregateCollection."""

from . import *  # noqa: F403


class ConfigRecorderRecordingGroup(config.ConfigurationRecorder.RecordingGroup):
    include_global_resource_types = If("IsMainRegion", True, False)
    all_supported = True


class ConfigRecorder(config.ConfigurationRecorder):
    name = Sub('${AWS::Region}-Config-Recorder')
    recording_group = ConfigRecorderRecordingGroup
    role_arn = ConfigRole.Arn


class AggragateAccountAuth(config.AggregationAuthorization):
    authorized_account_id = AggregateAccount
    authorized_aws_region = MainRegion


class DeliveryChannel(config.DeliveryChannel):
    s3_bucket_name = DataBucket
    sns_topic_arn = NotificationTopic


class AggregateCollectionAccountAggregationSource(config.ConfigurationAggregator.AccountAggregationSource):
    account_ids = SubAccountList
    all_aws_regions = True


class AggregateCollection(config.ConfigurationAggregator):
    account_aggregation_sources = [AggregateCollectionAccountAggregationSource]
    configuration_aggregator_name = 'ConfigAggregateCollector'
    condition = 'IsAggregateAccount'
