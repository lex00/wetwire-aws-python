"""PropertyTypes for AWS::MSK::Replicator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmazonMskCluster(PropertyType):
    msk_cluster_arn: DslValue[str] | None = None


@dataclass
class ConsumerGroupReplication(PropertyType):
    consumer_groups_to_replicate: list[DslValue[str]] = field(default_factory=list)
    consumer_groups_to_exclude: list[DslValue[str]] = field(default_factory=list)
    detect_and_copy_new_consumer_groups: DslValue[bool] | None = None
    synchronise_consumer_group_offsets: DslValue[bool] | None = None


@dataclass
class KafkaCluster(PropertyType):
    amazon_msk_cluster: DslValue[AmazonMskCluster] | None = None
    vpc_config: DslValue[KafkaClusterClientVpcConfig] | None = None


@dataclass
class KafkaClusterClientVpcConfig(PropertyType):
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ReplicationInfo(PropertyType):
    consumer_group_replication: DslValue[ConsumerGroupReplication] | None = None
    source_kafka_cluster_arn: DslValue[str] | None = None
    target_compression_type: DslValue[str] | None = None
    target_kafka_cluster_arn: DslValue[str] | None = None
    topic_replication: DslValue[TopicReplication] | None = None


@dataclass
class ReplicationStartingPosition(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class ReplicationTopicNameConfiguration(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class TopicReplication(PropertyType):
    topics_to_replicate: list[DslValue[str]] = field(default_factory=list)
    copy_access_control_lists_for_topics: DslValue[bool] | None = None
    copy_topic_configurations: DslValue[bool] | None = None
    detect_and_copy_new_topics: DslValue[bool] | None = None
    starting_position: DslValue[ReplicationStartingPosition] | None = None
    topic_name_configuration: DslValue[ReplicationTopicNameConfiguration] | None = None
    topics_to_exclude: list[DslValue[str]] = field(default_factory=list)
