"""PropertyTypes for AWS::DataZone::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataSourceConfigurationInput(PropertyType):
    glue_run_configuration: DslValue[GlueRunConfigurationInput] | None = None
    redshift_run_configuration: DslValue[RedshiftRunConfigurationInput] | None = None
    sage_maker_run_configuration: DslValue[SageMakerRunConfigurationInput] | None = None


@dataclass
class FilterExpression(PropertyType):
    expression: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FormInput(PropertyType):
    form_name: DslValue[str] | None = None
    content: DslValue[str] | None = None
    type_identifier: DslValue[str] | None = None
    type_revision: DslValue[str] | None = None


@dataclass
class GlueRunConfigurationInput(PropertyType):
    relational_filter_configurations: list[DslValue[RelationalFilterConfiguration]] = (
        field(default_factory=list)
    )
    auto_import_data_quality_result: DslValue[bool] | None = None
    catalog_name: DslValue[str] | None = None
    data_access_role: DslValue[str] | None = None


@dataclass
class RecommendationConfiguration(PropertyType):
    enable_business_name_generation: DslValue[bool] | None = None


@dataclass
class RedshiftClusterStorage(PropertyType):
    cluster_name: DslValue[str] | None = None


@dataclass
class RedshiftCredentialConfiguration(PropertyType):
    secret_manager_arn: DslValue[str] | None = None


@dataclass
class RedshiftRunConfigurationInput(PropertyType):
    relational_filter_configurations: list[DslValue[RelationalFilterConfiguration]] = (
        field(default_factory=list)
    )
    data_access_role: DslValue[str] | None = None
    redshift_credential_configuration: (
        DslValue[RedshiftCredentialConfiguration] | None
    ) = None
    redshift_storage: DslValue[RedshiftStorage] | None = None


@dataclass
class RedshiftServerlessStorage(PropertyType):
    workgroup_name: DslValue[str] | None = None


@dataclass
class RedshiftStorage(PropertyType):
    redshift_cluster_source: DslValue[RedshiftClusterStorage] | None = None
    redshift_serverless_source: DslValue[RedshiftServerlessStorage] | None = None


@dataclass
class RelationalFilterConfiguration(PropertyType):
    database_name: DslValue[str] | None = None
    filter_expressions: list[DslValue[FilterExpression]] = field(default_factory=list)
    schema_name: DslValue[str] | None = None


@dataclass
class SageMakerRunConfigurationInput(PropertyType):
    tracking_assets: DslValue[dict[str, Any]] | None = None


@dataclass
class ScheduleConfiguration(PropertyType):
    schedule: DslValue[str] | None = None
    timezone: DslValue[str] | None = None
