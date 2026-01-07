"""PropertyTypes for AWS::AppSync::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthorizationConfig(PropertyType):
    authorization_type: DslValue[str] | None = None
    aws_iam_config: DslValue[AwsIamConfig] | None = None


@dataclass
class AwsIamConfig(PropertyType):
    signing_region: DslValue[str] | None = None
    signing_service_name: DslValue[str] | None = None


@dataclass
class DeltaSyncConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base_table_ttl": "BaseTableTTL",
        "delta_sync_table_ttl": "DeltaSyncTableTTL",
    }

    base_table_ttl: DslValue[str] | None = None
    delta_sync_table_name: DslValue[str] | None = None
    delta_sync_table_ttl: DslValue[str] | None = None


@dataclass
class DynamoDBConfig(PropertyType):
    aws_region: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    delta_sync_config: DslValue[DeltaSyncConfig] | None = None
    use_caller_credentials: DslValue[bool] | None = None
    versioned: DslValue[bool] | None = None


@dataclass
class EventBridgeConfig(PropertyType):
    event_bus_arn: DslValue[str] | None = None


@dataclass
class HttpConfig(PropertyType):
    endpoint: DslValue[str] | None = None
    authorization_config: DslValue[AuthorizationConfig] | None = None


@dataclass
class LambdaConfig(PropertyType):
    lambda_function_arn: DslValue[str] | None = None


@dataclass
class OpenSearchServiceConfig(PropertyType):
    aws_region: DslValue[str] | None = None
    endpoint: DslValue[str] | None = None


@dataclass
class RdsHttpEndpointConfig(PropertyType):
    aws_region: DslValue[str] | None = None
    aws_secret_store_arn: DslValue[str] | None = None
    db_cluster_identifier: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    schema: DslValue[str] | None = None


@dataclass
class RelationalDatabaseConfig(PropertyType):
    relational_database_source_type: DslValue[str] | None = None
    rds_http_endpoint_config: DslValue[RdsHttpEndpointConfig] | None = None
