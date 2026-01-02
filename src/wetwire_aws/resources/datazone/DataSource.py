"""PropertyTypes for AWS::DataZone::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataSourceConfigurationInput(PropertyType):
    glue_run_configuration: GlueRunConfigurationInput | None = None
    redshift_run_configuration: RedshiftRunConfigurationInput | None = None
    sage_maker_run_configuration: SageMakerRunConfigurationInput | None = None


@dataclass
class FilterExpression(PropertyType):
    expression: str | None = None
    type_: str | None = None


@dataclass
class FormInput(PropertyType):
    form_name: str | None = None
    content: str | None = None
    type_identifier: str | None = None
    type_revision: str | None = None


@dataclass
class GlueRunConfigurationInput(PropertyType):
    relational_filter_configurations: list[RelationalFilterConfiguration] = field(
        default_factory=list
    )
    auto_import_data_quality_result: bool | None = None
    catalog_name: str | None = None
    data_access_role: str | None = None


@dataclass
class RecommendationConfiguration(PropertyType):
    enable_business_name_generation: bool | None = None


@dataclass
class RedshiftClusterStorage(PropertyType):
    cluster_name: str | None = None


@dataclass
class RedshiftCredentialConfiguration(PropertyType):
    secret_manager_arn: str | None = None


@dataclass
class RedshiftRunConfigurationInput(PropertyType):
    relational_filter_configurations: list[RelationalFilterConfiguration] = field(
        default_factory=list
    )
    data_access_role: str | None = None
    redshift_credential_configuration: RedshiftCredentialConfiguration | None = None
    redshift_storage: RedshiftStorage | None = None


@dataclass
class RedshiftServerlessStorage(PropertyType):
    workgroup_name: str | None = None


@dataclass
class RedshiftStorage(PropertyType):
    redshift_cluster_source: RedshiftClusterStorage | None = None
    redshift_serverless_source: RedshiftServerlessStorage | None = None


@dataclass
class RelationalFilterConfiguration(PropertyType):
    database_name: str | None = None
    filter_expressions: list[FilterExpression] = field(default_factory=list)
    schema_name: str | None = None


@dataclass
class SageMakerRunConfigurationInput(PropertyType):
    tracking_assets: dict[str, Any] | None = None


@dataclass
class ScheduleConfiguration(PropertyType):
    schedule: str | None = None
    timezone: str | None = None
