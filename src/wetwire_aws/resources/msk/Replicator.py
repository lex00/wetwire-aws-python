"""PropertyTypes for AWS::MSK::Replicator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmazonMskCluster(PropertyType):
    msk_cluster_arn: str | None = None


@dataclass
class ConsumerGroupReplication(PropertyType):
    consumer_groups_to_replicate: list[String] = field(default_factory=list)
    consumer_groups_to_exclude: list[String] = field(default_factory=list)
    detect_and_copy_new_consumer_groups: bool | None = None
    synchronise_consumer_group_offsets: bool | None = None


@dataclass
class KafkaCluster(PropertyType):
    amazon_msk_cluster: AmazonMskCluster | None = None
    vpc_config: KafkaClusterClientVpcConfig | None = None


@dataclass
class KafkaClusterClientVpcConfig(PropertyType):
    subnet_ids: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)


@dataclass
class ReplicationInfo(PropertyType):
    consumer_group_replication: ConsumerGroupReplication | None = None
    source_kafka_cluster_arn: str | None = None
    target_compression_type: str | None = None
    target_kafka_cluster_arn: str | None = None
    topic_replication: TopicReplication | None = None


@dataclass
class ReplicationStartingPosition(PropertyType):
    type_: str | None = None


@dataclass
class ReplicationTopicNameConfiguration(PropertyType):
    type_: str | None = None


@dataclass
class TopicReplication(PropertyType):
    topics_to_replicate: list[String] = field(default_factory=list)
    copy_access_control_lists_for_topics: bool | None = None
    copy_topic_configurations: bool | None = None
    detect_and_copy_new_topics: bool | None = None
    starting_position: ReplicationStartingPosition | None = None
    topic_name_configuration: ReplicationTopicNameConfiguration | None = None
    topics_to_exclude: list[String] = field(default_factory=list)
