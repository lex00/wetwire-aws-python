"""PropertyTypes for AWS::QuickSight::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmazonElasticsearchParameters(PropertyType):
    domain: DslValue[str] | None = None


@dataclass
class AmazonOpenSearchParameters(PropertyType):
    domain: DslValue[str] | None = None


@dataclass
class AthenaParameters(PropertyType):
    identity_center_configuration: DslValue[IdentityCenterConfiguration] | None = None
    role_arn: DslValue[str] | None = None
    work_group: DslValue[str] | None = None


@dataclass
class AuroraParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class AuroraPostgreSqlParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class CredentialPair(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None
    alternate_data_source_parameters: list[DslValue[DataSourceParameters]] = field(
        default_factory=list
    )


@dataclass
class DataSourceCredentials(PropertyType):
    copy_source_arn: DslValue[str] | None = None
    credential_pair: DslValue[CredentialPair] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class DataSourceErrorInfo(PropertyType):
    message: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DataSourceParameters(PropertyType):
    amazon_elasticsearch_parameters: DslValue[AmazonElasticsearchParameters] | None = (
        None
    )
    amazon_open_search_parameters: DslValue[AmazonOpenSearchParameters] | None = None
    athena_parameters: DslValue[AthenaParameters] | None = None
    aurora_parameters: DslValue[AuroraParameters] | None = None
    aurora_postgre_sql_parameters: DslValue[AuroraPostgreSqlParameters] | None = None
    databricks_parameters: DslValue[DatabricksParameters] | None = None
    maria_db_parameters: DslValue[MariaDbParameters] | None = None
    my_sql_parameters: DslValue[MySqlParameters] | None = None
    oracle_parameters: DslValue[OracleParameters] | None = None
    postgre_sql_parameters: DslValue[PostgreSqlParameters] | None = None
    presto_parameters: DslValue[PrestoParameters] | None = None
    rds_parameters: DslValue[RdsParameters] | None = None
    redshift_parameters: DslValue[RedshiftParameters] | None = None
    s3_parameters: DslValue[S3Parameters] | None = None
    snowflake_parameters: DslValue[SnowflakeParameters] | None = None
    spark_parameters: DslValue[SparkParameters] | None = None
    sql_server_parameters: DslValue[SqlServerParameters] | None = None
    starburst_parameters: DslValue[StarburstParameters] | None = None
    teradata_parameters: DslValue[TeradataParameters] | None = None
    trino_parameters: DslValue[TrinoParameters] | None = None


@dataclass
class DatabricksParameters(PropertyType):
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None
    sql_endpoint_path: DslValue[str] | None = None


@dataclass
class IdentityCenterConfiguration(PropertyType):
    enable_identity_propagation: DslValue[bool] | None = None


@dataclass
class ManifestFileLocation(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class MariaDbParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class MySqlParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class OAuthParameters(PropertyType):
    token_provider_url: DslValue[str] | None = None
    identity_provider_resource_uri: DslValue[str] | None = None
    identity_provider_vpc_connection_properties: (
        DslValue[VpcConnectionProperties] | None
    ) = None
    o_auth_scope: DslValue[str] | None = None


@dataclass
class OracleParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None
    use_service_name: DslValue[bool] | None = None


@dataclass
class PostgreSqlParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class PrestoParameters(PropertyType):
    catalog: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class RdsParameters(PropertyType):
    database: DslValue[str] | None = None
    instance_id: DslValue[str] | None = None


@dataclass
class RedshiftIAMParameters(PropertyType):
    role_arn: DslValue[str] | None = None
    auto_create_database_user: DslValue[bool] | None = None
    database_groups: list[DslValue[str]] = field(default_factory=list)
    database_user: DslValue[str] | None = None


@dataclass
class RedshiftParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_parameters": "IAMParameters",
    }

    database: DslValue[str] | None = None
    cluster_id: DslValue[str] | None = None
    host: DslValue[str] | None = None
    iam_parameters: DslValue[RedshiftIAMParameters] | None = None
    identity_center_configuration: DslValue[IdentityCenterConfiguration] | None = None
    port: DslValue[float] | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[str] | None = None
    resource: DslValue[str] | None = None


@dataclass
class S3Parameters(PropertyType):
    manifest_file_location: DslValue[ManifestFileLocation] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class SnowflakeParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    warehouse: DslValue[str] | None = None
    authentication_type: DslValue[str] | None = None
    database_access_control_role: DslValue[str] | None = None
    o_auth_parameters: DslValue[OAuthParameters] | None = None


@dataclass
class SparkParameters(PropertyType):
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class SqlServerParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class SslProperties(PropertyType):
    disable_ssl: DslValue[bool] | None = None


@dataclass
class StarburstParameters(PropertyType):
    catalog: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None
    authentication_type: DslValue[str] | None = None
    database_access_control_role: DslValue[str] | None = None
    o_auth_parameters: DslValue[OAuthParameters] | None = None
    product_type: DslValue[str] | None = None


@dataclass
class TeradataParameters(PropertyType):
    database: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class TrinoParameters(PropertyType):
    catalog: DslValue[str] | None = None
    host: DslValue[str] | None = None
    port: DslValue[float] | None = None


@dataclass
class VpcConnectionProperties(PropertyType):
    vpc_connection_arn: DslValue[str] | None = None
