"""PropertyTypes for AWS::Glue::Crawler."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CatalogTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    dlq_event_queue_arn: DslValue[str] | None = None
    event_queue_arn: DslValue[str] | None = None
    tables: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DeltaTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    create_native_delta_table: DslValue[bool] | None = None
    delta_tables: list[DslValue[str]] = field(default_factory=list)
    write_manifest: DslValue[bool] | None = None


@dataclass
class DynamoDBTarget(PropertyType):
    path: DslValue[str] | None = None
    scan_all: DslValue[bool] | None = None
    scan_rate: DslValue[float] | None = None


@dataclass
class HudiTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    exclusions: list[DslValue[str]] = field(default_factory=list)
    maximum_traversal_depth: DslValue[int] | None = None
    paths: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IcebergTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    exclusions: list[DslValue[str]] = field(default_factory=list)
    maximum_traversal_depth: DslValue[int] | None = None
    paths: list[DslValue[str]] = field(default_factory=list)


@dataclass
class JdbcTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    enable_additional_metadata: list[DslValue[str]] = field(default_factory=list)
    exclusions: list[DslValue[str]] = field(default_factory=list)
    path: DslValue[str] | None = None


@dataclass
class LakeFormationConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    use_lake_formation_credentials: DslValue[bool] | None = None


@dataclass
class MongoDBTarget(PropertyType):
    connection_name: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class RecrawlPolicy(PropertyType):
    recrawl_behavior: DslValue[str] | None = None


@dataclass
class S3Target(PropertyType):
    connection_name: DslValue[str] | None = None
    dlq_event_queue_arn: DslValue[str] | None = None
    event_queue_arn: DslValue[str] | None = None
    exclusions: list[DslValue[str]] = field(default_factory=list)
    path: DslValue[str] | None = None
    sample_size: DslValue[int] | None = None


@dataclass
class Schedule(PropertyType):
    schedule_expression: DslValue[str] | None = None


@dataclass
class SchemaChangePolicy(PropertyType):
    delete_behavior: DslValue[str] | None = None
    update_behavior: DslValue[str] | None = None


@dataclass
class Targets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db_targets": "DynamoDBTargets",
        "mongo_db_targets": "MongoDBTargets",
    }

    catalog_targets: list[DslValue[CatalogTarget]] = field(default_factory=list)
    delta_targets: list[DslValue[DeltaTarget]] = field(default_factory=list)
    dynamo_db_targets: list[DslValue[DynamoDBTarget]] = field(default_factory=list)
    hudi_targets: list[DslValue[HudiTarget]] = field(default_factory=list)
    iceberg_targets: list[DslValue[IcebergTarget]] = field(default_factory=list)
    jdbc_targets: list[DslValue[JdbcTarget]] = field(default_factory=list)
    mongo_db_targets: list[DslValue[MongoDBTarget]] = field(default_factory=list)
    s3_targets: list[DslValue[S3Target]] = field(default_factory=list)
