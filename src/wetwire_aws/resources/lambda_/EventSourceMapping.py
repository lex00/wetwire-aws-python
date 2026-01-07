"""PropertyTypes for AWS::Lambda::EventSourceMapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmazonManagedKafkaEventSourceConfig(PropertyType):
    consumer_group_id: DslValue[str] | None = None
    schema_registry_config: DslValue[SchemaRegistryConfig] | None = None


@dataclass
class DestinationConfig(PropertyType):
    on_failure: DslValue[OnFailure] | None = None


@dataclass
class DocumentDBEventSourceConfig(PropertyType):
    collection_name: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    full_document: DslValue[str] | None = None


@dataclass
class Endpoints(PropertyType):
    kafka_bootstrap_servers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Filter(PropertyType):
    pattern: DslValue[str] | None = None


@dataclass
class FilterCriteria(PropertyType):
    filters: list[DslValue[Filter]] = field(default_factory=list)


@dataclass
class LoggingConfig(PropertyType):
    system_log_level: DslValue[str] | None = None


@dataclass
class MetricsConfig(PropertyType):
    metrics: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OnFailure(PropertyType):
    destination: DslValue[str] | None = None


@dataclass
class ProvisionedPollerConfig(PropertyType):
    maximum_pollers: DslValue[int] | None = None
    minimum_pollers: DslValue[int] | None = None
    poller_group_name: DslValue[str] | None = None


@dataclass
class ScalingConfig(PropertyType):
    maximum_concurrency: DslValue[int] | None = None


@dataclass
class SchemaRegistryAccessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    type_: DslValue[str] | None = None
    uri: DslValue[str] | None = None


@dataclass
class SchemaRegistryConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_registry_uri": "SchemaRegistryURI",
    }

    access_configs: list[DslValue[SchemaRegistryAccessConfig]] = field(
        default_factory=list
    )
    event_record_format: DslValue[str] | None = None
    schema_registry_uri: DslValue[str] | None = None
    schema_validation_configs: list[DslValue[SchemaValidationConfig]] = field(
        default_factory=list
    )


@dataclass
class SchemaValidationConfig(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class SelfManagedEventSource(PropertyType):
    endpoints: DslValue[Endpoints] | None = None


@dataclass
class SelfManagedKafkaEventSourceConfig(PropertyType):
    consumer_group_id: DslValue[str] | None = None
    schema_registry_config: DslValue[SchemaRegistryConfig] | None = None


@dataclass
class SourceAccessConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    type_: DslValue[str] | None = None
    uri: DslValue[str] | None = None
