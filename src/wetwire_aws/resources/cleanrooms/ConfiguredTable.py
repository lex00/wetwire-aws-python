"""PropertyTypes for AWS::CleanRooms::ConfiguredTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AggregateColumn(PropertyType):
    column_names: list[String] = field(default_factory=list)
    function: str | None = None


@dataclass
class AggregationConstraint(PropertyType):
    column_name: str | None = None
    minimum: float | None = None
    type_: str | None = None


@dataclass
class AnalysisRule(PropertyType):
    policy: ConfiguredTableAnalysisRulePolicy | None = None
    type_: str | None = None


@dataclass
class AnalysisRuleAggregation(PropertyType):
    aggregate_columns: list[AggregateColumn] = field(default_factory=list)
    dimension_columns: list[String] = field(default_factory=list)
    join_columns: list[String] = field(default_factory=list)
    output_constraints: list[AggregationConstraint] = field(default_factory=list)
    scalar_functions: list[String] = field(default_factory=list)
    additional_analyses: str | None = None
    allowed_join_operators: list[String] = field(default_factory=list)
    join_required: str | None = None


@dataclass
class AnalysisRuleCustom(PropertyType):
    allowed_analyses: list[String] = field(default_factory=list)
    additional_analyses: str | None = None
    allowed_analysis_providers: list[String] = field(default_factory=list)
    differential_privacy: DifferentialPrivacy | None = None
    disallowed_output_columns: list[String] = field(default_factory=list)


@dataclass
class AnalysisRuleList(PropertyType):
    join_columns: list[String] = field(default_factory=list)
    list_columns: list[String] = field(default_factory=list)
    additional_analyses: str | None = None
    allowed_join_operators: list[String] = field(default_factory=list)


@dataclass
class AthenaTableReference(PropertyType):
    database_name: str | None = None
    table_name: str | None = None
    work_group: str | None = None
    output_location: str | None = None
    region: str | None = None


@dataclass
class ConfiguredTableAnalysisRulePolicy(PropertyType):
    v1: ConfiguredTableAnalysisRulePolicyV1 | None = None


@dataclass
class ConfiguredTableAnalysisRulePolicyV1(PropertyType):
    aggregation: AnalysisRuleAggregation | None = None
    custom: AnalysisRuleCustom | None = None
    list: AnalysisRuleList | None = None


@dataclass
class DifferentialPrivacy(PropertyType):
    columns: list[DifferentialPrivacyColumn] = field(default_factory=list)


@dataclass
class DifferentialPrivacyColumn(PropertyType):
    name: str | None = None


@dataclass
class GlueTableReference(PropertyType):
    database_name: str | None = None
    table_name: str | None = None
    region: str | None = None


@dataclass
class SnowflakeTableReference(PropertyType):
    account_identifier: str | None = None
    database_name: str | None = None
    schema_name: str | None = None
    secret_arn: str | None = None
    table_name: str | None = None
    table_schema: SnowflakeTableSchema | None = None


@dataclass
class SnowflakeTableSchema(PropertyType):
    v1: list[SnowflakeTableSchemaV1] = field(default_factory=list)


@dataclass
class SnowflakeTableSchemaV1(PropertyType):
    column_name: str | None = None
    column_type: str | None = None


@dataclass
class TableReference(PropertyType):
    athena: AthenaTableReference | None = None
    glue: GlueTableReference | None = None
    snowflake: SnowflakeTableReference | None = None
