"""PropertyTypes for AWS::DataBrew::Recipe."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    operation: str | None = None
    parameters: RecipeParameters | None = None


@dataclass
class ConditionExpression(PropertyType):
    condition: str | None = None
    target_column: str | None = None
    value: str | None = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    table_name: str | None = None
    temp_directory: S3Location | None = None


@dataclass
class Input(PropertyType):
    data_catalog_input_definition: DataCatalogInputDefinition | None = None
    s3_input_definition: S3Location | None = None


@dataclass
class RecipeParameters(PropertyType):
    aggregate_function: str | None = None
    base: str | None = None
    case_statement: str | None = None
    category_map: str | None = None
    chars_to_remove: str | None = None
    collapse_consecutive_whitespace: str | None = None
    column_data_type: str | None = None
    column_range: str | None = None
    count: str | None = None
    custom_characters: str | None = None
    custom_stop_words: str | None = None
    custom_value: str | None = None
    datasets_columns: str | None = None
    date_add_value: str | None = None
    date_time_format: str | None = None
    date_time_parameters: str | None = None
    delete_other_rows: str | None = None
    delimiter: str | None = None
    end_pattern: str | None = None
    end_position: str | None = None
    end_value: str | None = None
    expand_contractions: str | None = None
    exponent: str | None = None
    false_string: str | None = None
    group_by_agg_function_options: str | None = None
    group_by_columns: str | None = None
    hidden_columns: str | None = None
    ignore_case: str | None = None
    include_in_split: str | None = None
    input: Input | None = None
    interval: str | None = None
    is_text: str | None = None
    join_keys: str | None = None
    join_type: str | None = None
    left_columns: str | None = None
    limit: str | None = None
    lower_bound: str | None = None
    map_type: str | None = None
    mode_type: str | None = None
    multi_line: bool | None = None
    num_rows: str | None = None
    num_rows_after: str | None = None
    num_rows_before: str | None = None
    order_by_column: str | None = None
    order_by_columns: str | None = None
    other: str | None = None
    pattern: str | None = None
    pattern_option1: str | None = None
    pattern_option2: str | None = None
    pattern_options: str | None = None
    period: str | None = None
    position: str | None = None
    remove_all_punctuation: str | None = None
    remove_all_quotes: str | None = None
    remove_all_whitespace: str | None = None
    remove_custom_characters: str | None = None
    remove_custom_value: str | None = None
    remove_leading_and_trailing_punctuation: str | None = None
    remove_leading_and_trailing_quotes: str | None = None
    remove_leading_and_trailing_whitespace: str | None = None
    remove_letters: str | None = None
    remove_numbers: str | None = None
    remove_source_column: str | None = None
    remove_special_characters: str | None = None
    right_columns: str | None = None
    sample_size: str | None = None
    sample_type: str | None = None
    second_input: str | None = None
    secondary_inputs: list[SecondaryInput] = field(default_factory=list)
    sheet_indexes: list[Integer] = field(default_factory=list)
    sheet_names: list[String] = field(default_factory=list)
    source_column: str | None = None
    source_column1: str | None = None
    source_column2: str | None = None
    source_columns: str | None = None
    start_column_index: str | None = None
    start_pattern: str | None = None
    start_position: str | None = None
    start_value: str | None = None
    stemming_mode: str | None = None
    step_count: str | None = None
    step_index: str | None = None
    stop_words_mode: str | None = None
    strategy: str | None = None
    target_column: str | None = None
    target_column_names: str | None = None
    target_date_format: str | None = None
    target_index: str | None = None
    time_zone: str | None = None
    tokenizer_pattern: str | None = None
    true_string: str | None = None
    udf_lang: str | None = None
    units: str | None = None
    unpivot_column: str | None = None
    upper_bound: str | None = None
    use_new_data_frame: str | None = None
    value: str | None = None
    value1: str | None = None
    value2: str | None = None
    value_column: str | None = None
    view_frame: str | None = None


@dataclass
class RecipeStep(PropertyType):
    action: Action | None = None
    condition_expressions: list[ConditionExpression] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None


@dataclass
class SecondaryInput(PropertyType):
    data_catalog_input_definition: DataCatalogInputDefinition | None = None
    s3_input_definition: S3Location | None = None
