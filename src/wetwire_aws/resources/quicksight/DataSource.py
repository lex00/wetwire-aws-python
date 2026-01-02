"""PropertyTypes for AWS::QuickSight::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmazonElasticsearchParameters(PropertyType):
    domain: str | None = None


@dataclass
class AmazonOpenSearchParameters(PropertyType):
    domain: str | None = None


@dataclass
class AthenaParameters(PropertyType):
    identity_center_configuration: IdentityCenterConfiguration | None = None
    role_arn: str | None = None
    work_group: str | None = None


@dataclass
class AuroraParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class AuroraPostgreSqlParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class CredentialPair(PropertyType):
    password: str | None = None
    username: str | None = None
    alternate_data_source_parameters: list[DataSourceParameters] = field(
        default_factory=list
    )


@dataclass
class DataSourceCredentials(PropertyType):
    copy_source_arn: str | None = None
    credential_pair: CredentialPair | None = None
    secret_arn: str | None = None


@dataclass
class DataSourceErrorInfo(PropertyType):
    message: str | None = None
    type_: str | None = None


@dataclass
class DataSourceParameters(PropertyType):
    amazon_elasticsearch_parameters: AmazonElasticsearchParameters | None = None
    amazon_open_search_parameters: AmazonOpenSearchParameters | None = None
    athena_parameters: AthenaParameters | None = None
    aurora_parameters: AuroraParameters | None = None
    aurora_postgre_sql_parameters: AuroraPostgreSqlParameters | None = None
    databricks_parameters: DatabricksParameters | None = None
    maria_db_parameters: MariaDbParameters | None = None
    my_sql_parameters: MySqlParameters | None = None
    oracle_parameters: OracleParameters | None = None
    postgre_sql_parameters: PostgreSqlParameters | None = None
    presto_parameters: PrestoParameters | None = None
    rds_parameters: RdsParameters | None = None
    redshift_parameters: RedshiftParameters | None = None
    s3_parameters: S3Parameters | None = None
    snowflake_parameters: SnowflakeParameters | None = None
    spark_parameters: SparkParameters | None = None
    sql_server_parameters: SqlServerParameters | None = None
    starburst_parameters: StarburstParameters | None = None
    teradata_parameters: TeradataParameters | None = None
    trino_parameters: TrinoParameters | None = None


@dataclass
class DatabricksParameters(PropertyType):
    host: str | None = None
    port: float | None = None
    sql_endpoint_path: str | None = None


@dataclass
class IdentityCenterConfiguration(PropertyType):
    enable_identity_propagation: bool | None = None


@dataclass
class ManifestFileLocation(PropertyType):
    bucket: str | None = None
    key: str | None = None


@dataclass
class MariaDbParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class MySqlParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class OAuthParameters(PropertyType):
    token_provider_url: str | None = None
    identity_provider_resource_uri: str | None = None
    identity_provider_vpc_connection_properties: VpcConnectionProperties | None = None
    o_auth_scope: str | None = None


@dataclass
class OracleParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None
    use_service_name: bool | None = None


@dataclass
class PostgreSqlParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class PrestoParameters(PropertyType):
    catalog: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class RdsParameters(PropertyType):
    database: str | None = None
    instance_id: str | None = None


@dataclass
class RedshiftIAMParameters(PropertyType):
    role_arn: str | None = None
    auto_create_database_user: bool | None = None
    database_groups: list[String] = field(default_factory=list)
    database_user: str | None = None


@dataclass
class RedshiftParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_parameters": "IAMParameters",
    }

    database: str | None = None
    cluster_id: str | None = None
    host: str | None = None
    iam_parameters: RedshiftIAMParameters | None = None
    identity_center_configuration: IdentityCenterConfiguration | None = None
    port: float | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[String] = field(default_factory=list)
    principal: str | None = None
    resource: str | None = None


@dataclass
class S3Parameters(PropertyType):
    manifest_file_location: ManifestFileLocation | None = None
    role_arn: str | None = None


@dataclass
class SnowflakeParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    warehouse: str | None = None
    authentication_type: str | None = None
    database_access_control_role: str | None = None
    o_auth_parameters: OAuthParameters | None = None


@dataclass
class SparkParameters(PropertyType):
    host: str | None = None
    port: float | None = None


@dataclass
class SqlServerParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class SslProperties(PropertyType):
    disable_ssl: bool | None = None


@dataclass
class StarburstParameters(PropertyType):
    catalog: str | None = None
    host: str | None = None
    port: float | None = None
    authentication_type: str | None = None
    database_access_control_role: str | None = None
    o_auth_parameters: OAuthParameters | None = None
    product_type: str | None = None


@dataclass
class TeradataParameters(PropertyType):
    database: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class TrinoParameters(PropertyType):
    catalog: str | None = None
    host: str | None = None
    port: float | None = None


@dataclass
class VpcConnectionProperties(PropertyType):
    vpc_connection_arn: str | None = None
