"""PropertyTypes for AWS::QuickSight::Topic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CellValueSynonym(PropertyType):
    cell_value: str | None = None
    synonyms: list[String] = field(default_factory=list)


@dataclass
class CollectiveConstant(PropertyType):
    value_list: list[String] = field(default_factory=list)


@dataclass
class ComparativeOrder(PropertyType):
    specifed_order: list[String] = field(default_factory=list)
    treat_undefined_specified_values: str | None = None
    use_ordering: str | None = None


@dataclass
class CustomInstructions(PropertyType):
    custom_instructions_string: str | None = None


@dataclass
class DataAggregation(PropertyType):
    dataset_row_date_granularity: str | None = None
    default_date_column_name: str | None = None


@dataclass
class DatasetMetadata(PropertyType):
    dataset_arn: str | None = None
    calculated_fields: list[TopicCalculatedField] = field(default_factory=list)
    columns: list[TopicColumn] = field(default_factory=list)
    data_aggregation: DataAggregation | None = None
    dataset_description: str | None = None
    dataset_name: str | None = None
    filters: list[TopicFilter] = field(default_factory=list)
    named_entities: list[TopicNamedEntity] = field(default_factory=list)


@dataclass
class DefaultFormatting(PropertyType):
    display_format: str | None = None
    display_format_options: DisplayFormatOptions | None = None


@dataclass
class DisplayFormatOptions(PropertyType):
    blank_cell_format: str | None = None
    currency_symbol: str | None = None
    date_format: str | None = None
    decimal_separator: str | None = None
    fraction_digits: float | None = None
    grouping_separator: str | None = None
    negative_format: NegativeFormat | None = None
    prefix: str | None = None
    suffix: str | None = None
    unit_scaler: str | None = None
    use_blank_cell_format: bool | None = None
    use_grouping: bool | None = None


@dataclass
class NamedEntityDefinition(PropertyType):
    field_name: str | None = None
    metric: NamedEntityDefinitionMetric | None = None
    property_name: str | None = None
    property_role: str | None = None
    property_usage: str | None = None


@dataclass
class NamedEntityDefinitionMetric(PropertyType):
    aggregation: str | None = None
    aggregation_function_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class NegativeFormat(PropertyType):
    prefix: str | None = None
    suffix: str | None = None


@dataclass
class RangeConstant(PropertyType):
    maximum: str | None = None
    minimum: str | None = None


@dataclass
class SemanticEntityType(PropertyType):
    sub_type_name: str | None = None
    type_name: str | None = None
    type_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class SemanticType(PropertyType):
    falsey_cell_value: str | None = None
    falsey_cell_value_synonyms: list[String] = field(default_factory=list)
    sub_type_name: str | None = None
    truthy_cell_value: str | None = None
    truthy_cell_value_synonyms: list[String] = field(default_factory=list)
    type_name: str | None = None
    type_parameters: dict[str, String] = field(default_factory=dict)


@dataclass
class TopicCalculatedField(PropertyType):
    calculated_field_name: str | None = None
    expression: str | None = None
    aggregation: str | None = None
    allowed_aggregations: list[String] = field(default_factory=list)
    calculated_field_description: str | None = None
    calculated_field_synonyms: list[String] = field(default_factory=list)
    cell_value_synonyms: list[CellValueSynonym] = field(default_factory=list)
    column_data_role: str | None = None
    comparative_order: ComparativeOrder | None = None
    default_formatting: DefaultFormatting | None = None
    disable_indexing: bool | None = None
    is_included_in_topic: bool | None = None
    never_aggregate_in_filter: bool | None = None
    non_additive: bool | None = None
    not_allowed_aggregations: list[String] = field(default_factory=list)
    semantic_type: SemanticType | None = None
    time_granularity: str | None = None


@dataclass
class TopicCategoryFilter(PropertyType):
    category_filter_function: str | None = None
    category_filter_type: str | None = None
    constant: TopicCategoryFilterConstant | None = None
    inverse: bool | None = None


@dataclass
class TopicCategoryFilterConstant(PropertyType):
    collective_constant: CollectiveConstant | None = None
    constant_type: str | None = None
    singular_constant: str | None = None


@dataclass
class TopicColumn(PropertyType):
    column_name: str | None = None
    aggregation: str | None = None
    allowed_aggregations: list[String] = field(default_factory=list)
    cell_value_synonyms: list[CellValueSynonym] = field(default_factory=list)
    column_data_role: str | None = None
    column_description: str | None = None
    column_friendly_name: str | None = None
    column_synonyms: list[String] = field(default_factory=list)
    comparative_order: ComparativeOrder | None = None
    default_formatting: DefaultFormatting | None = None
    disable_indexing: bool | None = None
    is_included_in_topic: bool | None = None
    never_aggregate_in_filter: bool | None = None
    non_additive: bool | None = None
    not_allowed_aggregations: list[String] = field(default_factory=list)
    semantic_type: SemanticType | None = None
    time_granularity: str | None = None


@dataclass
class TopicConfigOptions(PropertyType):
    q_business_insights_enabled: bool | None = None


@dataclass
class TopicDateRangeFilter(PropertyType):
    constant: TopicRangeFilterConstant | None = None
    inclusive: bool | None = None


@dataclass
class TopicFilter(PropertyType):
    filter_name: str | None = None
    operand_field_name: str | None = None
    category_filter: TopicCategoryFilter | None = None
    date_range_filter: TopicDateRangeFilter | None = None
    filter_class: str | None = None
    filter_description: str | None = None
    filter_synonyms: list[String] = field(default_factory=list)
    filter_type: str | None = None
    numeric_equality_filter: TopicNumericEqualityFilter | None = None
    numeric_range_filter: TopicNumericRangeFilter | None = None
    relative_date_filter: TopicRelativeDateFilter | None = None


@dataclass
class TopicNamedEntity(PropertyType):
    entity_name: str | None = None
    definition: list[NamedEntityDefinition] = field(default_factory=list)
    entity_description: str | None = None
    entity_synonyms: list[String] = field(default_factory=list)
    semantic_entity_type: SemanticEntityType | None = None


@dataclass
class TopicNumericEqualityFilter(PropertyType):
    aggregation: str | None = None
    constant: TopicSingularFilterConstant | None = None


@dataclass
class TopicNumericRangeFilter(PropertyType):
    aggregation: str | None = None
    constant: TopicRangeFilterConstant | None = None
    inclusive: bool | None = None


@dataclass
class TopicRangeFilterConstant(PropertyType):
    constant_type: str | None = None
    range_constant: RangeConstant | None = None


@dataclass
class TopicRelativeDateFilter(PropertyType):
    constant: TopicSingularFilterConstant | None = None
    relative_date_filter_function: str | None = None
    time_granularity: str | None = None


@dataclass
class TopicSingularFilterConstant(PropertyType):
    constant_type: str | None = None
    singular_constant: str | None = None
