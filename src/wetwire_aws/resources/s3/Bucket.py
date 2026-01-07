"""PropertyTypes for AWS::S3::Bucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: DslValue[int] | None = None


@dataclass
class AccelerateConfiguration(PropertyType):
    acceleration_status: DslValue[str] | None = None


@dataclass
class AccessControlTranslation(PropertyType):
    owner: DslValue[str] | None = None


@dataclass
class AnalyticsConfiguration(PropertyType):
    id: DslValue[str] | None = None
    storage_class_analysis: DslValue[StorageClassAnalysis] | None = None
    prefix: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class BlockedEncryptionTypes(PropertyType):
    encryption_type: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BucketEncryption(PropertyType):
    server_side_encryption_configuration: list[DslValue[ServerSideEncryptionRule]] = (
        field(default_factory=list)
    )


@dataclass
class CorsConfiguration(PropertyType):
    cors_rules: list[DslValue[CorsRule]] = field(default_factory=list)


@dataclass
class CorsRule(PropertyType):
    allowed_methods: list[DslValue[str]] = field(default_factory=list)
    allowed_origins: list[DslValue[str]] = field(default_factory=list)
    allowed_headers: list[DslValue[str]] = field(default_factory=list)
    exposed_headers: list[DslValue[str]] = field(default_factory=list)
    id: DslValue[str] | None = None
    max_age: DslValue[int] | None = None


@dataclass
class DataExport(PropertyType):
    destination: DslValue[Destination] | None = None
    output_schema_version: DslValue[str] | None = None


@dataclass
class DefaultRetention(PropertyType):
    days: DslValue[int] | None = None
    mode: DslValue[str] | None = None
    years: DslValue[int] | None = None


@dataclass
class DeleteMarkerReplication(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class Destination(PropertyType):
    bucket_arn: DslValue[str] | None = None
    format: DslValue[str] | None = None
    bucket_account_id: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_kms_key_id": "ReplicaKmsKeyID",
    }

    replica_kms_key_id: DslValue[str] | None = None


@dataclass
class EventBridgeConfiguration(PropertyType):
    event_bridge_enabled: DslValue[bool] | None = None


@dataclass
class FilterRule(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class IntelligentTieringConfiguration(PropertyType):
    id: DslValue[str] | None = None
    status: DslValue[str] | None = None
    tierings: list[DslValue[Tiering]] = field(default_factory=list)
    prefix: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class InventoryConfiguration(PropertyType):
    destination: DslValue[Destination] | None = None
    enabled: DslValue[bool] | None = None
    id: DslValue[str] | None = None
    included_object_versions: DslValue[str] | None = None
    schedule_frequency: DslValue[str] | None = None
    optional_fields: list[DslValue[str]] = field(default_factory=list)
    prefix: DslValue[str] | None = None


@dataclass
class InventoryTableConfiguration(PropertyType):
    configuration_state: DslValue[str] | None = None
    encryption_configuration: DslValue[MetadataTableEncryptionConfiguration] | None = (
        None
    )
    table_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class JournalTableConfiguration(PropertyType):
    record_expiration: DslValue[RecordExpiration] | None = None
    encryption_configuration: DslValue[MetadataTableEncryptionConfiguration] | None = (
        None
    )
    table_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class LambdaConfiguration(PropertyType):
    event: DslValue[str] | None = None
    function: DslValue[str] | None = None
    filter: DslValue[NotificationFilter] | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[DslValue[Rule]] = field(default_factory=list)
    transition_default_minimum_object_size: DslValue[str] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destination_bucket_name: DslValue[str] | None = None
    log_file_prefix: DslValue[str] | None = None
    target_object_key_format: DslValue[TargetObjectKeyFormat] | None = None


@dataclass
class MetadataConfiguration(PropertyType):
    journal_table_configuration: DslValue[JournalTableConfiguration] | None = None
    destination: DslValue[MetadataDestination] | None = None
    inventory_table_configuration: DslValue[InventoryTableConfiguration] | None = None


@dataclass
class MetadataDestination(PropertyType):
    table_bucket_type: DslValue[str] | None = None
    table_bucket_arn: DslValue[str] | None = None
    table_namespace: DslValue[str] | None = None


@dataclass
class MetadataTableConfiguration(PropertyType):
    s3_tables_destination: DslValue[S3TablesDestination] | None = None


@dataclass
class MetadataTableEncryptionConfiguration(PropertyType):
    sse_algorithm: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class Metrics(PropertyType):
    status: DslValue[str] | None = None
    event_threshold: DslValue[ReplicationTimeValue] | None = None


@dataclass
class MetricsConfiguration(PropertyType):
    id: DslValue[str] | None = None
    access_point_arn: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class NoncurrentVersionExpiration(PropertyType):
    noncurrent_days: DslValue[int] | None = None
    newer_noncurrent_versions: DslValue[int] | None = None


@dataclass
class NoncurrentVersionTransition(PropertyType):
    storage_class: DslValue[str] | None = None
    transition_in_days: DslValue[int] | None = None
    newer_noncurrent_versions: DslValue[int] | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    event_bridge_configuration: DslValue[EventBridgeConfiguration] | None = None
    lambda_configurations: list[DslValue[LambdaConfiguration]] = field(
        default_factory=list
    )
    queue_configurations: list[DslValue[QueueConfiguration]] = field(
        default_factory=list
    )
    topic_configurations: list[DslValue[TopicConfiguration]] = field(
        default_factory=list
    )


@dataclass
class NotificationFilter(PropertyType):
    s3_key: DslValue[S3KeyFilter] | None = None


@dataclass
class ObjectLockConfiguration(PropertyType):
    object_lock_enabled: DslValue[str] | None = None
    rule: DslValue[ObjectLockRule] | None = None


@dataclass
class ObjectLockRule(PropertyType):
    default_retention: DslValue[DefaultRetention] | None = None


@dataclass
class OwnershipControls(PropertyType):
    rules: list[DslValue[OwnershipControlsRule]] = field(default_factory=list)


@dataclass
class OwnershipControlsRule(PropertyType):
    object_ownership: DslValue[str] | None = None


@dataclass
class PartitionedPrefix(PropertyType):
    partition_date_source: DslValue[str] | None = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: DslValue[bool] | None = None
    block_public_policy: DslValue[bool] | None = None
    ignore_public_acls: DslValue[bool] | None = None
    restrict_public_buckets: DslValue[bool] | None = None


@dataclass
class QueueConfiguration(PropertyType):
    event: DslValue[str] | None = None
    queue: DslValue[str] | None = None
    filter: DslValue[NotificationFilter] | None = None


@dataclass
class RecordExpiration(PropertyType):
    expiration: DslValue[str] | None = None
    days: DslValue[int] | None = None


@dataclass
class RedirectAllRequestsTo(PropertyType):
    host_name: DslValue[str] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class RedirectRule(PropertyType):
    host_name: DslValue[str] | None = None
    http_redirect_code: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    replace_key_prefix_with: DslValue[str] | None = None
    replace_key_with: DslValue[str] | None = None


@dataclass
class ReplicaModifications(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class ReplicationConfiguration(PropertyType):
    role: DslValue[str] | None = None
    rules: list[DslValue[ReplicationRule]] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    bucket: DslValue[str] | None = None
    access_control_translation: DslValue[AccessControlTranslation] | None = None
    account: DslValue[str] | None = None
    encryption_configuration: DslValue[EncryptionConfiguration] | None = None
    metrics: DslValue[Metrics] | None = None
    replication_time: DslValue[ReplicationTime] | None = None
    storage_class: DslValue[str] | None = None


@dataclass
class ReplicationRule(PropertyType):
    destination: DslValue[ReplicationDestination] | None = None
    status: DslValue[str] | None = None
    delete_marker_replication: DslValue[DeleteMarkerReplication] | None = None
    filter: DslValue[ReplicationRuleFilter] | None = None
    id: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    priority: DslValue[int] | None = None
    source_selection_criteria: DslValue[SourceSelectionCriteria] | None = None


@dataclass
class ReplicationRuleAndOperator(PropertyType):
    prefix: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class ReplicationRuleFilter(PropertyType):
    and_: DslValue[ReplicationRuleAndOperator] | None = None
    prefix: DslValue[str] | None = None
    tag_filter: DslValue[TagFilter] | None = None


@dataclass
class ReplicationTime(PropertyType):
    status: DslValue[str] | None = None
    time: DslValue[ReplicationTimeValue] | None = None


@dataclass
class ReplicationTimeValue(PropertyType):
    minutes: DslValue[int] | None = None


@dataclass
class RoutingRule(PropertyType):
    redirect_rule: DslValue[RedirectRule] | None = None
    routing_rule_condition: DslValue[RoutingRuleCondition] | None = None


@dataclass
class RoutingRuleCondition(PropertyType):
    http_error_code_returned_equals: DslValue[str] | None = None
    key_prefix_equals: DslValue[str] | None = None


@dataclass
class Rule(PropertyType):
    status: DslValue[str] | None = None
    abort_incomplete_multipart_upload: (
        DslValue[AbortIncompleteMultipartUpload] | None
    ) = None
    expiration_date: DslValue[str] | None = None
    expiration_in_days: DslValue[int] | None = None
    expired_object_delete_marker: DslValue[bool] | None = None
    id: DslValue[str] | None = None
    noncurrent_version_expiration: DslValue[NoncurrentVersionExpiration] | None = None
    noncurrent_version_expiration_in_days: DslValue[int] | None = None
    noncurrent_version_transition: DslValue[NoncurrentVersionTransition] | None = None
    noncurrent_version_transitions: list[DslValue[NoncurrentVersionTransition]] = field(
        default_factory=list
    )
    object_size_greater_than: DslValue[str] | None = None
    object_size_less_than: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)
    transition: DslValue[Transition] | None = None
    transitions: list[DslValue[Transition]] = field(default_factory=list)


@dataclass
class S3KeyFilter(PropertyType):
    rules: list[DslValue[FilterRule]] = field(default_factory=list)


@dataclass
class S3TablesDestination(PropertyType):
    table_bucket_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    table_arn: DslValue[str] | None = None
    table_namespace: DslValue[str] | None = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyID",
        "sse_algorithm": "SSEAlgorithm",
    }

    sse_algorithm: DslValue[str] | None = None
    kms_master_key_id: DslValue[str] | None = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    blocked_encryption_types: DslValue[BlockedEncryptionTypes] | None = None
    bucket_key_enabled: DslValue[bool] | None = None
    server_side_encryption_by_default: (
        DslValue[ServerSideEncryptionByDefault] | None
    ) = None


@dataclass
class SourceSelectionCriteria(PropertyType):
    replica_modifications: DslValue[ReplicaModifications] | None = None
    sse_kms_encrypted_objects: DslValue[SseKmsEncryptedObjects] | None = None


@dataclass
class SseKmsEncryptedObjects(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class StorageClassAnalysis(PropertyType):
    data_export: DslValue[DataExport] | None = None


@dataclass
class TagFilter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TargetObjectKeyFormat(PropertyType):
    partitioned_prefix: DslValue[PartitionedPrefix] | None = None
    simple_prefix: DslValue[dict[str, Any]] | None = None


@dataclass
class Tiering(PropertyType):
    access_tier: DslValue[str] | None = None
    days: DslValue[int] | None = None


@dataclass
class TopicConfiguration(PropertyType):
    event: DslValue[str] | None = None
    topic: DslValue[str] | None = None
    filter: DslValue[NotificationFilter] | None = None


@dataclass
class Transition(PropertyType):
    storage_class: DslValue[str] | None = None
    transition_date: DslValue[str] | None = None
    transition_in_days: DslValue[int] | None = None


@dataclass
class VersioningConfiguration(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class WebsiteConfiguration(PropertyType):
    error_document: DslValue[str] | None = None
    index_document: DslValue[str] | None = None
    redirect_all_requests_to: DslValue[RedirectAllRequestsTo] | None = None
    routing_rules: list[DslValue[RoutingRule]] = field(default_factory=list)
