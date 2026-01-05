"""PropertyTypes for AWS::DMS::DataProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DocDbSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    certificate_arn: str | None = None
    ssl_mode: str | None = None


@dataclass
class IbmDb2LuwSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class IbmDb2zOsSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class MariaDbSettings(PropertyType):
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class MongoDbSettings(PropertyType):
    port: int | None = None
    server_name: str | None = None
    auth_mechanism: str | None = None
    auth_source: str | None = None
    auth_type: str | None = None
    certificate_arn: str | None = None
    database_name: str | None = None
    ssl_mode: str | None = None


@dataclass
class MySqlSettings(PropertyType):
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class OracleSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    asm_server: str | None = None
    certificate_arn: str | None = None
    secrets_manager_oracle_asm_access_role_arn: str | None = None
    secrets_manager_oracle_asm_secret_id: str | None = None
    secrets_manager_security_db_encryption_access_role_arn: str | None = None
    secrets_manager_security_db_encryption_secret_id: str | None = None


@dataclass
class PostgreSqlSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None


@dataclass
class RedshiftSettings(PropertyType):
    database_name: str | None = None
    port: int | None = None
    server_name: str | None = None


@dataclass
class Settings(PropertyType):
    doc_db_settings: DocDbSettings | None = None
    ibm_db2_luw_settings: IbmDb2LuwSettings | None = None
    ibm_db2z_os_settings: IbmDb2zOsSettings | None = None
    maria_db_settings: MariaDbSettings | None = None
    microsoft_sql_server_settings: MicrosoftSqlServerSettings | None = None
    mongo_db_settings: MongoDbSettings | None = None
    my_sql_settings: MySqlSettings | None = None
    oracle_settings: OracleSettings | None = None
    postgre_sql_settings: PostgreSqlSettings | None = None
    redshift_settings: RedshiftSettings | None = None
    sybase_ase_settings: SybaseAseSettings | None = None


@dataclass
class SybaseAseSettings(PropertyType):
    port: int | None = None
    server_name: str | None = None
    ssl_mode: str | None = None
    certificate_arn: str | None = None
    database_name: str | None = None
    encrypt_password: bool | None = None
