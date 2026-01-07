"""PropertyTypes for AWS::DMS::DataProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DocDbSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None


@dataclass
class IbmDb2LuwSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class IbmDb2zOsSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class MariaDbSettings(PropertyType):
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class MongoDbSettings(PropertyType):
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    auth_mechanism: DslValue[str] | None = None
    auth_source: DslValue[str] | None = None
    auth_type: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None


@dataclass
class MySqlSettings(PropertyType):
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class OracleSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    asm_server: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None
    secrets_manager_oracle_asm_access_role_arn: DslValue[str] | None = None
    secrets_manager_oracle_asm_secret_id: DslValue[str] | None = None
    secrets_manager_security_db_encryption_access_role_arn: DslValue[str] | None = None
    secrets_manager_security_db_encryption_secret_id: DslValue[str] | None = None


@dataclass
class PostgreSqlSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None


@dataclass
class RedshiftSettings(PropertyType):
    database_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None


@dataclass
class Settings(PropertyType):
    doc_db_settings: DslValue[DocDbSettings] | None = None
    ibm_db2_luw_settings: DslValue[IbmDb2LuwSettings] | None = None
    ibm_db2z_os_settings: DslValue[IbmDb2zOsSettings] | None = None
    maria_db_settings: DslValue[MariaDbSettings] | None = None
    microsoft_sql_server_settings: DslValue[MicrosoftSqlServerSettings] | None = None
    mongo_db_settings: DslValue[MongoDbSettings] | None = None
    my_sql_settings: DslValue[MySqlSettings] | None = None
    oracle_settings: DslValue[OracleSettings] | None = None
    postgre_sql_settings: DslValue[PostgreSqlSettings] | None = None
    redshift_settings: DslValue[RedshiftSettings] | None = None
    sybase_ase_settings: DslValue[SybaseAseSettings] | None = None


@dataclass
class SybaseAseSettings(PropertyType):
    port: DslValue[int] | None = None
    server_name: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    encrypt_password: DslValue[bool] | None = None
