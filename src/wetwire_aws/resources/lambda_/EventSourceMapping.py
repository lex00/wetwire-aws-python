"""PropertyTypes for AWS::Lambda::EventSourceMapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmazonManagedKafkaEventSourceConfig(PropertyType):
    consumer_group_id: str | None = None
    schema_registry_config: SchemaRegistryConfig | None = None


@dataclass
class DestinationConfig(PropertyType):
    on_failure: OnFailure | None = None


@dataclass
class DocumentDBEventSourceConfig(PropertyType):
    collection_name: str | None = None
    database_name: str | None = None
    full_document: str | None = None


@dataclass
class Endpoints(PropertyType):
    kafka_bootstrap_servers: list[String] = field(default_factory=list)


@dataclass
class Filter(PropertyType):
    pattern: str | None = None


@dataclass
class FilterCriteria(PropertyType):
    filters: list[Filter] = field(default_factory=list)


@dataclass
class LoggingConfig(PropertyType):
    system_log_level: str | None = None


@dataclass
class MetricsConfig(PropertyType):
    metrics: list[String] = field(default_factory=list)


@dataclass
class OnFailure(PropertyType):
    destination: str | None = None


@dataclass
class ProvisionedPollerConfig(PropertyType):
    maximum_pollers: int | None = None
    minimum_pollers: int | None = None
    poller_group_name: str | None = None


@dataclass
class ScalingConfig(PropertyType):
    maximum_concurrency: int | None = None


@dataclass
class SchemaRegistryAccessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    type_: str | None = None
    uri: str | None = None


@dataclass
class SchemaRegistryConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_registry_uri": "SchemaRegistryURI",
    }

    access_configs: list[SchemaRegistryAccessConfig] = field(default_factory=list)
    event_record_format: str | None = None
    schema_registry_uri: str | None = None
    schema_validation_configs: list[SchemaValidationConfig] = field(
        default_factory=list
    )


@dataclass
class SchemaValidationConfig(PropertyType):
    attribute: str | None = None


@dataclass
class SelfManagedEventSource(PropertyType):
    endpoints: Endpoints | None = None


@dataclass
class SelfManagedKafkaEventSourceConfig(PropertyType):
    consumer_group_id: str | None = None
    schema_registry_config: SchemaRegistryConfig | None = None


@dataclass
class SourceAccessConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    type_: str | None = None
    uri: str | None = None
