"""PropertyTypes for AWS::Glue::Crawler."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CatalogTarget(PropertyType):
    connection_name: str | None = None
    database_name: str | None = None
    dlq_event_queue_arn: str | None = None
    event_queue_arn: str | None = None
    tables: list[String] = field(default_factory=list)


@dataclass
class DeltaTarget(PropertyType):
    connection_name: str | None = None
    create_native_delta_table: bool | None = None
    delta_tables: list[String] = field(default_factory=list)
    write_manifest: bool | None = None


@dataclass
class DynamoDBTarget(PropertyType):
    path: str | None = None
    scan_all: bool | None = None
    scan_rate: float | None = None


@dataclass
class HudiTarget(PropertyType):
    connection_name: str | None = None
    exclusions: list[String] = field(default_factory=list)
    maximum_traversal_depth: int | None = None
    paths: list[String] = field(default_factory=list)


@dataclass
class IcebergTarget(PropertyType):
    connection_name: str | None = None
    exclusions: list[String] = field(default_factory=list)
    maximum_traversal_depth: int | None = None
    paths: list[String] = field(default_factory=list)


@dataclass
class JdbcTarget(PropertyType):
    connection_name: str | None = None
    enable_additional_metadata: list[String] = field(default_factory=list)
    exclusions: list[String] = field(default_factory=list)
    path: str | None = None


@dataclass
class LakeFormationConfiguration(PropertyType):
    account_id: str | None = None
    use_lake_formation_credentials: bool | None = None


@dataclass
class MongoDBTarget(PropertyType):
    connection_name: str | None = None
    path: str | None = None


@dataclass
class RecrawlPolicy(PropertyType):
    recrawl_behavior: str | None = None


@dataclass
class S3Target(PropertyType):
    connection_name: str | None = None
    dlq_event_queue_arn: str | None = None
    event_queue_arn: str | None = None
    exclusions: list[String] = field(default_factory=list)
    path: str | None = None
    sample_size: int | None = None


@dataclass
class Schedule(PropertyType):
    schedule_expression: str | None = None


@dataclass
class SchemaChangePolicy(PropertyType):
    delete_behavior: str | None = None
    update_behavior: str | None = None


@dataclass
class Targets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db_targets": "DynamoDBTargets",
        "mongo_db_targets": "MongoDBTargets",
    }

    catalog_targets: list[CatalogTarget] = field(default_factory=list)
    delta_targets: list[DeltaTarget] = field(default_factory=list)
    dynamo_db_targets: list[DynamoDBTarget] = field(default_factory=list)
    hudi_targets: list[HudiTarget] = field(default_factory=list)
    iceberg_targets: list[IcebergTarget] = field(default_factory=list)
    jdbc_targets: list[JdbcTarget] = field(default_factory=list)
    mongo_db_targets: list[MongoDBTarget] = field(default_factory=list)
    s3_targets: list[S3Target] = field(default_factory=list)
