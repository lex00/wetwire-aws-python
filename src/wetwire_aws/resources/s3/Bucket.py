"""PropertyTypes for AWS::S3::Bucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: int | None = None


@dataclass
class AccelerateConfiguration(PropertyType):
    acceleration_status: str | None = None


@dataclass
class AccessControlTranslation(PropertyType):
    owner: str | None = None


@dataclass
class AnalyticsConfiguration(PropertyType):
    id: str | None = None
    storage_class_analysis: StorageClassAnalysis | None = None
    prefix: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class BlockedEncryptionTypes(PropertyType):
    encryption_type: list[String] = field(default_factory=list)


@dataclass
class BucketEncryption(PropertyType):
    server_side_encryption_configuration: list[ServerSideEncryptionRule] = field(
        default_factory=list
    )


@dataclass
class CorsConfiguration(PropertyType):
    cors_rules: list[CorsRule] = field(default_factory=list)


@dataclass
class CorsRule(PropertyType):
    allowed_methods: list[String] = field(default_factory=list)
    allowed_origins: list[String] = field(default_factory=list)
    allowed_headers: list[String] = field(default_factory=list)
    exposed_headers: list[String] = field(default_factory=list)
    id: str | None = None
    max_age: int | None = None


@dataclass
class DataExport(PropertyType):
    destination: Destination | None = None
    output_schema_version: str | None = None


@dataclass
class DefaultRetention(PropertyType):
    days: int | None = None
    mode: str | None = None
    years: int | None = None


@dataclass
class DeleteMarkerReplication(PropertyType):
    status: str | None = None


@dataclass
class Destination(PropertyType):
    bucket_arn: str | None = None
    format: str | None = None
    bucket_account_id: str | None = None
    prefix: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_kms_key_id": "ReplicaKmsKeyID",
    }

    replica_kms_key_id: str | None = None


@dataclass
class EventBridgeConfiguration(PropertyType):
    event_bridge_enabled: bool | None = None


@dataclass
class FilterRule(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class IntelligentTieringConfiguration(PropertyType):
    id: str | None = None
    status: str | None = None
    tierings: list[Tiering] = field(default_factory=list)
    prefix: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class InventoryConfiguration(PropertyType):
    destination: Destination | None = None
    enabled: bool | None = None
    id: str | None = None
    included_object_versions: str | None = None
    schedule_frequency: str | None = None
    optional_fields: list[String] = field(default_factory=list)
    prefix: str | None = None


@dataclass
class InventoryTableConfiguration(PropertyType):
    configuration_state: str | None = None
    encryption_configuration: MetadataTableEncryptionConfiguration | None = None
    table_arn: str | None = None
    table_name: str | None = None


@dataclass
class JournalTableConfiguration(PropertyType):
    record_expiration: RecordExpiration | None = None
    encryption_configuration: MetadataTableEncryptionConfiguration | None = None
    table_arn: str | None = None
    table_name: str | None = None


@dataclass
class LambdaConfiguration(PropertyType):
    event: str | None = None
    function: str | None = None
    filter: NotificationFilter | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[Rule] = field(default_factory=list)
    transition_default_minimum_object_size: str | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destination_bucket_name: str | None = None
    log_file_prefix: str | None = None
    target_object_key_format: TargetObjectKeyFormat | None = None


@dataclass
class MetadataConfiguration(PropertyType):
    journal_table_configuration: JournalTableConfiguration | None = None
    destination: MetadataDestination | None = None
    inventory_table_configuration: InventoryTableConfiguration | None = None


@dataclass
class MetadataDestination(PropertyType):
    table_bucket_type: str | None = None
    table_bucket_arn: str | None = None
    table_namespace: str | None = None


@dataclass
class MetadataTableConfiguration(PropertyType):
    s3_tables_destination: S3TablesDestination | None = None


@dataclass
class MetadataTableEncryptionConfiguration(PropertyType):
    sse_algorithm: str | None = None
    kms_key_arn: str | None = None


@dataclass
class Metrics(PropertyType):
    status: str | None = None
    event_threshold: ReplicationTimeValue | None = None


@dataclass
class MetricsConfiguration(PropertyType):
    id: str | None = None
    access_point_arn: str | None = None
    prefix: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class NoncurrentVersionExpiration(PropertyType):
    noncurrent_days: int | None = None
    newer_noncurrent_versions: int | None = None


@dataclass
class NoncurrentVersionTransition(PropertyType):
    storage_class: str | None = None
    transition_in_days: int | None = None
    newer_noncurrent_versions: int | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    event_bridge_configuration: EventBridgeConfiguration | None = None
    lambda_configurations: list[LambdaConfiguration] = field(default_factory=list)
    queue_configurations: list[QueueConfiguration] = field(default_factory=list)
    topic_configurations: list[TopicConfiguration] = field(default_factory=list)


@dataclass
class NotificationFilter(PropertyType):
    s3_key: S3KeyFilter | None = None


@dataclass
class ObjectLockConfiguration(PropertyType):
    object_lock_enabled: str | None = None
    rule: ObjectLockRule | None = None


@dataclass
class ObjectLockRule(PropertyType):
    default_retention: DefaultRetention | None = None


@dataclass
class OwnershipControls(PropertyType):
    rules: list[OwnershipControlsRule] = field(default_factory=list)


@dataclass
class OwnershipControlsRule(PropertyType):
    object_ownership: str | None = None


@dataclass
class PartitionedPrefix(PropertyType):
    partition_date_source: str | None = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: bool | None = None
    block_public_policy: bool | None = None
    ignore_public_acls: bool | None = None
    restrict_public_buckets: bool | None = None


@dataclass
class QueueConfiguration(PropertyType):
    event: str | None = None
    queue: str | None = None
    filter: NotificationFilter | None = None


@dataclass
class RecordExpiration(PropertyType):
    expiration: str | None = None
    days: int | None = None


@dataclass
class RedirectAllRequestsTo(PropertyType):
    host_name: str | None = None
    protocol: str | None = None


@dataclass
class RedirectRule(PropertyType):
    host_name: str | None = None
    http_redirect_code: str | None = None
    protocol: str | None = None
    replace_key_prefix_with: str | None = None
    replace_key_with: str | None = None


@dataclass
class ReplicaModifications(PropertyType):
    status: str | None = None


@dataclass
class ReplicationConfiguration(PropertyType):
    role: str | None = None
    rules: list[ReplicationRule] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    bucket: str | None = None
    access_control_translation: AccessControlTranslation | None = None
    account: str | None = None
    encryption_configuration: EncryptionConfiguration | None = None
    metrics: Metrics | None = None
    replication_time: ReplicationTime | None = None
    storage_class: str | None = None


@dataclass
class ReplicationRule(PropertyType):
    destination: ReplicationDestination | None = None
    status: str | None = None
    delete_marker_replication: DeleteMarkerReplication | None = None
    filter: ReplicationRuleFilter | None = None
    id: str | None = None
    prefix: str | None = None
    priority: int | None = None
    source_selection_criteria: SourceSelectionCriteria | None = None


@dataclass
class ReplicationRuleAndOperator(PropertyType):
    prefix: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class ReplicationRuleFilter(PropertyType):
    and_: ReplicationRuleAndOperator | None = None
    prefix: str | None = None
    tag_filter: TagFilter | None = None


@dataclass
class ReplicationTime(PropertyType):
    status: str | None = None
    time: ReplicationTimeValue | None = None


@dataclass
class ReplicationTimeValue(PropertyType):
    minutes: int | None = None


@dataclass
class RoutingRule(PropertyType):
    redirect_rule: RedirectRule | None = None
    routing_rule_condition: RoutingRuleCondition | None = None


@dataclass
class RoutingRuleCondition(PropertyType):
    http_error_code_returned_equals: str | None = None
    key_prefix_equals: str | None = None


@dataclass
class Rule(PropertyType):
    status: str | None = None
    abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = None
    expiration_date: str | None = None
    expiration_in_days: int | None = None
    expired_object_delete_marker: bool | None = None
    id: str | None = None
    noncurrent_version_expiration: NoncurrentVersionExpiration | None = None
    noncurrent_version_expiration_in_days: int | None = None
    noncurrent_version_transition: NoncurrentVersionTransition | None = None
    noncurrent_version_transitions: list[NoncurrentVersionTransition] = field(
        default_factory=list
    )
    object_size_greater_than: str | None = None
    object_size_less_than: str | None = None
    prefix: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)
    transition: Transition | None = None
    transitions: list[Transition] = field(default_factory=list)


@dataclass
class S3KeyFilter(PropertyType):
    rules: list[FilterRule] = field(default_factory=list)


@dataclass
class S3TablesDestination(PropertyType):
    table_bucket_arn: str | None = None
    table_name: str | None = None
    table_arn: str | None = None
    table_namespace: str | None = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyID",
        "sse_algorithm": "SSEAlgorithm",
    }

    sse_algorithm: str | None = None
    kms_master_key_id: str | None = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    blocked_encryption_types: BlockedEncryptionTypes | None = None
    bucket_key_enabled: bool | None = None
    server_side_encryption_by_default: ServerSideEncryptionByDefault | None = None


@dataclass
class SourceSelectionCriteria(PropertyType):
    replica_modifications: ReplicaModifications | None = None
    sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = None


@dataclass
class SseKmsEncryptedObjects(PropertyType):
    status: str | None = None


@dataclass
class StorageClassAnalysis(PropertyType):
    data_export: DataExport | None = None


@dataclass
class TagFilter(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class TargetObjectKeyFormat(PropertyType):
    partitioned_prefix: PartitionedPrefix | None = None
    simple_prefix: dict[str, Any] | None = None


@dataclass
class Tiering(PropertyType):
    access_tier: str | None = None
    days: int | None = None


@dataclass
class TopicConfiguration(PropertyType):
    event: str | None = None
    topic: str | None = None
    filter: NotificationFilter | None = None


@dataclass
class Transition(PropertyType):
    storage_class: str | None = None
    transition_date: str | None = None
    transition_in_days: int | None = None


@dataclass
class VersioningConfiguration(PropertyType):
    status: str | None = None


@dataclass
class WebsiteConfiguration(PropertyType):
    error_document: str | None = None
    index_document: str | None = None
    redirect_all_requests_to: RedirectAllRequestsTo | None = None
    routing_rules: list[RoutingRule] = field(default_factory=list)
