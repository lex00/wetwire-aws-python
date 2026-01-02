"""PropertyTypes for AWS::AppSync::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthorizationConfig(PropertyType):
    authorization_type: str | None = None
    aws_iam_config: AwsIamConfig | None = None


@dataclass
class AwsIamConfig(PropertyType):
    signing_region: str | None = None
    signing_service_name: str | None = None


@dataclass
class DeltaSyncConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base_table_ttl": "BaseTableTTL",
        "delta_sync_table_ttl": "DeltaSyncTableTTL",
    }

    base_table_ttl: str | None = None
    delta_sync_table_name: str | None = None
    delta_sync_table_ttl: str | None = None


@dataclass
class DynamoDBConfig(PropertyType):
    aws_region: str | None = None
    table_name: str | None = None
    delta_sync_config: DeltaSyncConfig | None = None
    use_caller_credentials: bool | None = None
    versioned: bool | None = None


@dataclass
class EventBridgeConfig(PropertyType):
    event_bus_arn: str | None = None


@dataclass
class HttpConfig(PropertyType):
    endpoint: str | None = None
    authorization_config: AuthorizationConfig | None = None


@dataclass
class LambdaConfig(PropertyType):
    lambda_function_arn: str | None = None


@dataclass
class OpenSearchServiceConfig(PropertyType):
    aws_region: str | None = None
    endpoint: str | None = None


@dataclass
class RdsHttpEndpointConfig(PropertyType):
    aws_region: str | None = None
    aws_secret_store_arn: str | None = None
    db_cluster_identifier: str | None = None
    database_name: str | None = None
    schema: str | None = None


@dataclass
class RelationalDatabaseConfig(PropertyType):
    relational_database_source_type: str | None = None
    rds_http_endpoint_config: RdsHttpEndpointConfig | None = None
