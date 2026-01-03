"""Infra resources: ConfigRecorder, ConfigRuleForVolumeTags, ConfigRuleForVolumeAutoEnableIO, DeliveryChannel."""

from . import *  # noqa: F403


class ConfigRecorderExclusionByResourceTypes:
    resource: config.ConfigurationRecorder.ExclusionByResourceTypes
    resource_types = ['AWS::EC2::Volume']


class ConfigRecorder:
    resource: config.ConfigurationRecorder
    name = 'default'
    recording_group = ConfigRecorderExclusionByResourceTypes
    role_arn = ConfigRole.Arn


class ConfigRuleForVolumeTagsScope:
    resource: config.ConfigRule.Scope
    compliance_resource_types = ['AWS::EC2::Volume']


class ConfigRuleForVolumeTagsSource:
    resource: config.ConfigRule.Source
    owner = 'AWS'
    source_identifier = 'REQUIRED_TAGS'


class ConfigRuleForVolumeTags:
    resource: config.ConfigRule
    input_parameters = {
        'tag1Key': 'CostCenter',
    }
    scope = ConfigRuleForVolumeTagsScope
    source = ConfigRuleForVolumeTagsSource
    depends_on = [ConfigRecorder]


class ConfigRuleForVolumeAutoEnableIOScope:
    resource: config.ConfigRule.Scope
    compliance_resource_id = Ec2Volume
    compliance_resource_types = ['AWS::EC2::Volume']


class ConfigRuleForVolumeAutoEnableIOSourceDetail:
    resource: config.ConfigRule.SourceDetail
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


class ConfigRuleForVolumeAutoEnableIOSource:
    resource: config.ConfigRule.Source
    owner = 'CUSTOM_LAMBDA'
    source_details = [ConfigRuleForVolumeAutoEnableIOSourceDetail]
    source_identifier = VolumeAutoEnableIOComplianceCheck.Arn


class ConfigRuleForVolumeAutoEnableIO:
    resource: config.ConfigRule
    config_rule_name = 'ConfigRuleForVolumeAutoEnableIO'
    scope = ConfigRuleForVolumeAutoEnableIOScope
    source = ConfigRuleForVolumeAutoEnableIOSource
    depends_on = [ConfigPermissionToCallLambda, ConfigRecorder]


class DeliveryChannelConfigSnapshotDeliveryProperties:
    resource: config.DeliveryChannel.ConfigSnapshotDeliveryProperties
    delivery_frequency = 'Six_Hours'


class DeliveryChannel:
    resource: config.DeliveryChannel
    config_snapshot_delivery_properties = DeliveryChannelConfigSnapshotDeliveryProperties
    s3_bucket_name = ConfigBucket
    sns_topic_arn = ConfigTopic
    condition = 'CreateDeliveryChannel'
