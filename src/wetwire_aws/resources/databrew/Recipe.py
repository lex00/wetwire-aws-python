"""PropertyTypes for AWS::DataBrew::Recipe."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    operation: DslValue[str] | None = None
    parameters: DslValue[RecipeParameters] | None = None


@dataclass
class ConditionExpression(PropertyType):
    condition: DslValue[str] | None = None
    target_column: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    temp_directory: DslValue[S3Location] | None = None


@dataclass
class Input(PropertyType):
    data_catalog_input_definition: DslValue[DataCatalogInputDefinition] | None = None
    s3_input_definition: DslValue[S3Location] | None = None


@dataclass
class RecipeParameters(PropertyType):
    aggregate_function: DslValue[str] | None = None
    base: DslValue[str] | None = None
    case_statement: DslValue[str] | None = None
    category_map: DslValue[str] | None = None
    chars_to_remove: DslValue[str] | None = None
    collapse_consecutive_whitespace: DslValue[str] | None = None
    column_data_type: DslValue[str] | None = None
    column_range: DslValue[str] | None = None
    count: DslValue[str] | None = None
    custom_characters: DslValue[str] | None = None
    custom_stop_words: DslValue[str] | None = None
    custom_value: DslValue[str] | None = None
    datasets_columns: DslValue[str] | None = None
    date_add_value: DslValue[str] | None = None
    date_time_format: DslValue[str] | None = None
    date_time_parameters: DslValue[str] | None = None
    delete_other_rows: DslValue[str] | None = None
    delimiter: DslValue[str] | None = None
    end_pattern: DslValue[str] | None = None
    end_position: DslValue[str] | None = None
    end_value: DslValue[str] | None = None
    expand_contractions: DslValue[str] | None = None
    exponent: DslValue[str] | None = None
    false_string: DslValue[str] | None = None
    group_by_agg_function_options: DslValue[str] | None = None
    group_by_columns: DslValue[str] | None = None
    hidden_columns: DslValue[str] | None = None
    ignore_case: DslValue[str] | None = None
    include_in_split: DslValue[str] | None = None
    input: DslValue[Input] | None = None
    interval: DslValue[str] | None = None
    is_text: DslValue[str] | None = None
    join_keys: DslValue[str] | None = None
    join_type: DslValue[str] | None = None
    left_columns: DslValue[str] | None = None
    limit: DslValue[str] | None = None
    lower_bound: DslValue[str] | None = None
    map_type: DslValue[str] | None = None
    mode_type: DslValue[str] | None = None
    multi_line: DslValue[bool] | None = None
    num_rows: DslValue[str] | None = None
    num_rows_after: DslValue[str] | None = None
    num_rows_before: DslValue[str] | None = None
    order_by_column: DslValue[str] | None = None
    order_by_columns: DslValue[str] | None = None
    other: DslValue[str] | None = None
    pattern: DslValue[str] | None = None
    pattern_option1: DslValue[str] | None = None
    pattern_option2: DslValue[str] | None = None
    pattern_options: DslValue[str] | None = None
    period: DslValue[str] | None = None
    position: DslValue[str] | None = None
    remove_all_punctuation: DslValue[str] | None = None
    remove_all_quotes: DslValue[str] | None = None
    remove_all_whitespace: DslValue[str] | None = None
    remove_custom_characters: DslValue[str] | None = None
    remove_custom_value: DslValue[str] | None = None
    remove_leading_and_trailing_punctuation: DslValue[str] | None = None
    remove_leading_and_trailing_quotes: DslValue[str] | None = None
    remove_leading_and_trailing_whitespace: DslValue[str] | None = None
    remove_letters: DslValue[str] | None = None
    remove_numbers: DslValue[str] | None = None
    remove_source_column: DslValue[str] | None = None
    remove_special_characters: DslValue[str] | None = None
    right_columns: DslValue[str] | None = None
    sample_size: DslValue[str] | None = None
    sample_type: DslValue[str] | None = None
    second_input: DslValue[str] | None = None
    secondary_inputs: list[DslValue[SecondaryInput]] = field(default_factory=list)
    sheet_indexes: list[DslValue[int]] = field(default_factory=list)
    sheet_names: list[DslValue[str]] = field(default_factory=list)
    source_column: DslValue[str] | None = None
    source_column1: DslValue[str] | None = None
    source_column2: DslValue[str] | None = None
    source_columns: DslValue[str] | None = None
    start_column_index: DslValue[str] | None = None
    start_pattern: DslValue[str] | None = None
    start_position: DslValue[str] | None = None
    start_value: DslValue[str] | None = None
    stemming_mode: DslValue[str] | None = None
    step_count: DslValue[str] | None = None
    step_index: DslValue[str] | None = None
    stop_words_mode: DslValue[str] | None = None
    strategy: DslValue[str] | None = None
    target_column: DslValue[str] | None = None
    target_column_names: DslValue[str] | None = None
    target_date_format: DslValue[str] | None = None
    target_index: DslValue[str] | None = None
    time_zone: DslValue[str] | None = None
    tokenizer_pattern: DslValue[str] | None = None
    true_string: DslValue[str] | None = None
    udf_lang: DslValue[str] | None = None
    units: DslValue[str] | None = None
    unpivot_column: DslValue[str] | None = None
    upper_bound: DslValue[str] | None = None
    use_new_data_frame: DslValue[str] | None = None
    value: DslValue[str] | None = None
    value1: DslValue[str] | None = None
    value2: DslValue[str] | None = None
    value_column: DslValue[str] | None = None
    view_frame: DslValue[str] | None = None


@dataclass
class RecipeStep(PropertyType):
    action: DslValue[Action] | None = None
    condition_expressions: list[DslValue[ConditionExpression]] = field(
        default_factory=list
    )


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class SecondaryInput(PropertyType):
    data_catalog_input_definition: DslValue[DataCatalogInputDefinition] | None = None
    s3_input_definition: DslValue[S3Location] | None = None
