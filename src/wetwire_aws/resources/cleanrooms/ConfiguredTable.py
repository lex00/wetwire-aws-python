"""PropertyTypes for AWS::CleanRooms::ConfiguredTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AggregateColumn(PropertyType):
    column_names: list[DslValue[str]] = field(default_factory=list)
    function: DslValue[str] | None = None


@dataclass
class AggregationConstraint(PropertyType):
    column_name: DslValue[str] | None = None
    minimum: DslValue[float] | None = None
    type_: DslValue[str] | None = None


@dataclass
class AnalysisRule(PropertyType):
    policy: DslValue[ConfiguredTableAnalysisRulePolicy] | None = None
    type_: DslValue[str] | None = None


@dataclass
class AnalysisRuleAggregation(PropertyType):
    aggregate_columns: list[DslValue[AggregateColumn]] = field(default_factory=list)
    dimension_columns: list[DslValue[str]] = field(default_factory=list)
    join_columns: list[DslValue[str]] = field(default_factory=list)
    output_constraints: list[DslValue[AggregationConstraint]] = field(
        default_factory=list
    )
    scalar_functions: list[DslValue[str]] = field(default_factory=list)
    additional_analyses: DslValue[str] | None = None
    allowed_join_operators: list[DslValue[str]] = field(default_factory=list)
    join_required: DslValue[str] | None = None


@dataclass
class AnalysisRuleCustom(PropertyType):
    allowed_analyses: list[DslValue[str]] = field(default_factory=list)
    additional_analyses: DslValue[str] | None = None
    allowed_analysis_providers: list[DslValue[str]] = field(default_factory=list)
    differential_privacy: DslValue[DifferentialPrivacy] | None = None
    disallowed_output_columns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AnalysisRuleList(PropertyType):
    join_columns: list[DslValue[str]] = field(default_factory=list)
    list_columns: list[DslValue[str]] = field(default_factory=list)
    additional_analyses: DslValue[str] | None = None
    allowed_join_operators: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AthenaTableReference(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    work_group: DslValue[str] | None = None
    output_location: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class ConfiguredTableAnalysisRulePolicy(PropertyType):
    v1: DslValue[ConfiguredTableAnalysisRulePolicyV1] | None = None


@dataclass
class ConfiguredTableAnalysisRulePolicyV1(PropertyType):
    aggregation: DslValue[AnalysisRuleAggregation] | None = None
    custom: DslValue[AnalysisRuleCustom] | None = None
    list: DslValue[AnalysisRuleList] | None = None


@dataclass
class DifferentialPrivacy(PropertyType):
    columns: list[DslValue[DifferentialPrivacyColumn]] = field(default_factory=list)


@dataclass
class DifferentialPrivacyColumn(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class GlueTableReference(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class SnowflakeTableReference(PropertyType):
    account_identifier: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    schema_name: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    table_schema: DslValue[SnowflakeTableSchema] | None = None


@dataclass
class SnowflakeTableSchema(PropertyType):
    v1: list[DslValue[SnowflakeTableSchemaV1]] = field(default_factory=list)


@dataclass
class SnowflakeTableSchemaV1(PropertyType):
    column_name: DslValue[str] | None = None
    column_type: DslValue[str] | None = None


@dataclass
class TableReference(PropertyType):
    athena: DslValue[AthenaTableReference] | None = None
    glue: DslValue[GlueTableReference] | None = None
    snowflake: DslValue[SnowflakeTableReference] | None = None
