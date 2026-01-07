"""PropertyTypes for AWS::QuickSight::Topic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CellValueSynonym(PropertyType):
    cell_value: DslValue[str] | None = None
    synonyms: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CollectiveConstant(PropertyType):
    value_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ComparativeOrder(PropertyType):
    specifed_order: list[DslValue[str]] = field(default_factory=list)
    treat_undefined_specified_values: DslValue[str] | None = None
    use_ordering: DslValue[str] | None = None


@dataclass
class CustomInstructions(PropertyType):
    custom_instructions_string: DslValue[str] | None = None


@dataclass
class DataAggregation(PropertyType):
    dataset_row_date_granularity: DslValue[str] | None = None
    default_date_column_name: DslValue[str] | None = None


@dataclass
class DatasetMetadata(PropertyType):
    dataset_arn: DslValue[str] | None = None
    calculated_fields: list[DslValue[TopicCalculatedField]] = field(
        default_factory=list
    )
    columns: list[DslValue[TopicColumn]] = field(default_factory=list)
    data_aggregation: DslValue[DataAggregation] | None = None
    dataset_description: DslValue[str] | None = None
    dataset_name: DslValue[str] | None = None
    filters: list[DslValue[TopicFilter]] = field(default_factory=list)
    named_entities: list[DslValue[TopicNamedEntity]] = field(default_factory=list)


@dataclass
class DefaultFormatting(PropertyType):
    display_format: DslValue[str] | None = None
    display_format_options: DslValue[DisplayFormatOptions] | None = None


@dataclass
class DisplayFormatOptions(PropertyType):
    blank_cell_format: DslValue[str] | None = None
    currency_symbol: DslValue[str] | None = None
    date_format: DslValue[str] | None = None
    decimal_separator: DslValue[str] | None = None
    fraction_digits: DslValue[float] | None = None
    grouping_separator: DslValue[str] | None = None
    negative_format: DslValue[NegativeFormat] | None = None
    prefix: DslValue[str] | None = None
    suffix: DslValue[str] | None = None
    unit_scaler: DslValue[str] | None = None
    use_blank_cell_format: DslValue[bool] | None = None
    use_grouping: DslValue[bool] | None = None


@dataclass
class NamedEntityDefinition(PropertyType):
    field_name: DslValue[str] | None = None
    metric: DslValue[NamedEntityDefinitionMetric] | None = None
    property_name: DslValue[str] | None = None
    property_role: DslValue[str] | None = None
    property_usage: DslValue[str] | None = None


@dataclass
class NamedEntityDefinitionMetric(PropertyType):
    aggregation: DslValue[str] | None = None
    aggregation_function_parameters: dict[str, DslValue[str]] = field(
        default_factory=dict
    )


@dataclass
class NegativeFormat(PropertyType):
    prefix: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class RangeConstant(PropertyType):
    maximum: DslValue[str] | None = None
    minimum: DslValue[str] | None = None


@dataclass
class SemanticEntityType(PropertyType):
    sub_type_name: DslValue[str] | None = None
    type_name: DslValue[str] | None = None
    type_parameters: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class SemanticType(PropertyType):
    falsey_cell_value: DslValue[str] | None = None
    falsey_cell_value_synonyms: list[DslValue[str]] = field(default_factory=list)
    sub_type_name: DslValue[str] | None = None
    truthy_cell_value: DslValue[str] | None = None
    truthy_cell_value_synonyms: list[DslValue[str]] = field(default_factory=list)
    type_name: DslValue[str] | None = None
    type_parameters: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class TopicCalculatedField(PropertyType):
    calculated_field_name: DslValue[str] | None = None
    expression: DslValue[str] | None = None
    aggregation: DslValue[str] | None = None
    allowed_aggregations: list[DslValue[str]] = field(default_factory=list)
    calculated_field_description: DslValue[str] | None = None
    calculated_field_synonyms: list[DslValue[str]] = field(default_factory=list)
    cell_value_synonyms: list[DslValue[CellValueSynonym]] = field(default_factory=list)
    column_data_role: DslValue[str] | None = None
    comparative_order: DslValue[ComparativeOrder] | None = None
    default_formatting: DslValue[DefaultFormatting] | None = None
    disable_indexing: DslValue[bool] | None = None
    is_included_in_topic: DslValue[bool] | None = None
    never_aggregate_in_filter: DslValue[bool] | None = None
    non_additive: DslValue[bool] | None = None
    not_allowed_aggregations: list[DslValue[str]] = field(default_factory=list)
    semantic_type: DslValue[SemanticType] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TopicCategoryFilter(PropertyType):
    category_filter_function: DslValue[str] | None = None
    category_filter_type: DslValue[str] | None = None
    constant: DslValue[TopicCategoryFilterConstant] | None = None
    inverse: DslValue[bool] | None = None


@dataclass
class TopicCategoryFilterConstant(PropertyType):
    collective_constant: DslValue[CollectiveConstant] | None = None
    constant_type: DslValue[str] | None = None
    singular_constant: DslValue[str] | None = None


@dataclass
class TopicColumn(PropertyType):
    column_name: DslValue[str] | None = None
    aggregation: DslValue[str] | None = None
    allowed_aggregations: list[DslValue[str]] = field(default_factory=list)
    cell_value_synonyms: list[DslValue[CellValueSynonym]] = field(default_factory=list)
    column_data_role: DslValue[str] | None = None
    column_description: DslValue[str] | None = None
    column_friendly_name: DslValue[str] | None = None
    column_synonyms: list[DslValue[str]] = field(default_factory=list)
    comparative_order: DslValue[ComparativeOrder] | None = None
    default_formatting: DslValue[DefaultFormatting] | None = None
    disable_indexing: DslValue[bool] | None = None
    is_included_in_topic: DslValue[bool] | None = None
    never_aggregate_in_filter: DslValue[bool] | None = None
    non_additive: DslValue[bool] | None = None
    not_allowed_aggregations: list[DslValue[str]] = field(default_factory=list)
    semantic_type: DslValue[SemanticType] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TopicConfigOptions(PropertyType):
    q_business_insights_enabled: DslValue[bool] | None = None


@dataclass
class TopicDateRangeFilter(PropertyType):
    constant: DslValue[TopicRangeFilterConstant] | None = None
    inclusive: DslValue[bool] | None = None


@dataclass
class TopicFilter(PropertyType):
    filter_name: DslValue[str] | None = None
    operand_field_name: DslValue[str] | None = None
    category_filter: DslValue[TopicCategoryFilter] | None = None
    date_range_filter: DslValue[TopicDateRangeFilter] | None = None
    filter_class: DslValue[str] | None = None
    filter_description: DslValue[str] | None = None
    filter_synonyms: list[DslValue[str]] = field(default_factory=list)
    filter_type: DslValue[str] | None = None
    numeric_equality_filter: DslValue[TopicNumericEqualityFilter] | None = None
    numeric_range_filter: DslValue[TopicNumericRangeFilter] | None = None
    relative_date_filter: DslValue[TopicRelativeDateFilter] | None = None


@dataclass
class TopicNamedEntity(PropertyType):
    entity_name: DslValue[str] | None = None
    definition: list[DslValue[NamedEntityDefinition]] = field(default_factory=list)
    entity_description: DslValue[str] | None = None
    entity_synonyms: list[DslValue[str]] = field(default_factory=list)
    semantic_entity_type: DslValue[SemanticEntityType] | None = None


@dataclass
class TopicNumericEqualityFilter(PropertyType):
    aggregation: DslValue[str] | None = None
    constant: DslValue[TopicSingularFilterConstant] | None = None


@dataclass
class TopicNumericRangeFilter(PropertyType):
    aggregation: DslValue[str] | None = None
    constant: DslValue[TopicRangeFilterConstant] | None = None
    inclusive: DslValue[bool] | None = None


@dataclass
class TopicRangeFilterConstant(PropertyType):
    constant_type: DslValue[str] | None = None
    range_constant: DslValue[RangeConstant] | None = None


@dataclass
class TopicRelativeDateFilter(PropertyType):
    constant: DslValue[TopicSingularFilterConstant] | None = None
    relative_date_filter_function: DslValue[str] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TopicSingularFilterConstant(PropertyType):
    constant_type: DslValue[str] | None = None
    singular_constant: DslValue[str] | None = None
