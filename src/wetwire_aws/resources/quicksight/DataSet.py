"""PropertyTypes for AWS::QuickSight::DataSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AggregateOperation(PropertyType):
    aggregations: list[DslValue[Aggregation]] = field(default_factory=list)
    alias: DslValue[str] | None = None
    source: DslValue[TransformOperationSource] | None = None
    group_by_column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Aggregation(PropertyType):
    aggregation_function: DslValue[DataPrepAggregationFunction] | None = None
    new_column_id: DslValue[str] | None = None
    new_column_name: DslValue[str] | None = None


@dataclass
class AppendOperation(PropertyType):
    alias: DslValue[str] | None = None
    appended_columns: list[DslValue[AppendedColumn]] = field(default_factory=list)
    first_source: DslValue[TransformOperationSource] | None = None
    second_source: DslValue[TransformOperationSource] | None = None


@dataclass
class AppendedColumn(PropertyType):
    column_name: DslValue[str] | None = None
    new_column_id: DslValue[str] | None = None


@dataclass
class CalculatedColumn(PropertyType):
    column_id: DslValue[str] | None = None
    column_name: DslValue[str] | None = None
    expression: DslValue[str] | None = None


@dataclass
class CastColumnTypeOperation(PropertyType):
    column_name: DslValue[str] | None = None
    new_column_type: DslValue[str] | None = None
    format: DslValue[str] | None = None
    sub_type: DslValue[str] | None = None


@dataclass
class CastColumnTypesOperation(PropertyType):
    alias: DslValue[str] | None = None
    cast_column_type_operations: list[DslValue[CastColumnTypeOperation]] = field(
        default_factory=list
    )
    source: DslValue[TransformOperationSource] | None = None


@dataclass
class ColumnGroup(PropertyType):
    geo_spatial_column_group: DslValue[GeoSpatialColumnGroup] | None = None


@dataclass
class ColumnLevelPermissionRule(PropertyType):
    column_names: list[DslValue[str]] = field(default_factory=list)
    principals: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ColumnToUnpivot(PropertyType):
    column_name: DslValue[str] | None = None
    new_value: DslValue[str] | None = None


@dataclass
class CreateColumnsOperation(PropertyType):
    columns: list[DslValue[CalculatedColumn]] = field(default_factory=list)
    alias: DslValue[str] | None = None
    source: DslValue[TransformOperationSource] | None = None


@dataclass
class CustomSql(PropertyType):
    columns: list[DslValue[InputColumn]] = field(default_factory=list)
    data_source_arn: DslValue[str] | None = None
    name: DslValue[str] | None = None
    sql_query: DslValue[str] | None = None


@dataclass
class DataPrepAggregationFunction(PropertyType):
    list_aggregation: DslValue[DataPrepListAggregationFunction] | None = None
    percentile_aggregation: DslValue[DataPrepPercentileAggregationFunction] | None = (
        None
    )
    simple_aggregation: DslValue[DataPrepSimpleAggregationFunction] | None = None


@dataclass
class DataPrepConfiguration(PropertyType):
    destination_table_map: dict[str, DslValue[DestinationTable]] = field(
        default_factory=dict
    )
    source_table_map: dict[str, DslValue[SourceTable]] = field(default_factory=dict)
    transform_step_map: dict[str, DslValue[TransformStep]] = field(default_factory=dict)


@dataclass
class DataPrepListAggregationFunction(PropertyType):
    distinct: DslValue[bool] | None = None
    separator: DslValue[str] | None = None
    input_column_name: DslValue[str] | None = None


@dataclass
class DataPrepPercentileAggregationFunction(PropertyType):
    percentile_value: DslValue[float] | None = None
    input_column_name: DslValue[str] | None = None


@dataclass
class DataPrepSimpleAggregationFunction(PropertyType):
    function_type: DslValue[str] | None = None
    input_column_name: DslValue[str] | None = None


@dataclass
class DataSetColumnIdMapping(PropertyType):
    source_column_id: DslValue[str] | None = None
    target_column_id: DslValue[str] | None = None


@dataclass
class DataSetDateComparisonFilterCondition(PropertyType):
    operator: DslValue[str] | None = None
    value: DslValue[DataSetDateFilterValue] | None = None


@dataclass
class DataSetDateFilterCondition(PropertyType):
    column_name: DslValue[str] | None = None
    comparison_filter_condition: (
        DslValue[DataSetDateComparisonFilterCondition] | None
    ) = None
    range_filter_condition: DslValue[DataSetDateRangeFilterCondition] | None = None


@dataclass
class DataSetDateFilterValue(PropertyType):
    static_value: DslValue[str] | None = None


@dataclass
class DataSetDateRangeFilterCondition(PropertyType):
    include_maximum: DslValue[bool] | None = None
    include_minimum: DslValue[bool] | None = None
    range_maximum: DslValue[DataSetDateFilterValue] | None = None
    range_minimum: DslValue[DataSetDateFilterValue] | None = None


@dataclass
class DataSetNumericComparisonFilterCondition(PropertyType):
    operator: DslValue[str] | None = None
    value: DslValue[DataSetNumericFilterValue] | None = None


@dataclass
class DataSetNumericFilterCondition(PropertyType):
    column_name: DslValue[str] | None = None
    comparison_filter_condition: (
        DslValue[DataSetNumericComparisonFilterCondition] | None
    ) = None
    range_filter_condition: DslValue[DataSetNumericRangeFilterCondition] | None = None


@dataclass
class DataSetNumericFilterValue(PropertyType):
    static_value: DslValue[float] | None = None


@dataclass
class DataSetNumericRangeFilterCondition(PropertyType):
    include_maximum: DslValue[bool] | None = None
    include_minimum: DslValue[bool] | None = None
    range_maximum: DslValue[DataSetNumericFilterValue] | None = None
    range_minimum: DslValue[DataSetNumericFilterValue] | None = None


@dataclass
class DataSetRefreshProperties(PropertyType):
    failure_configuration: DslValue[RefreshFailureConfiguration] | None = None
    refresh_configuration: DslValue[RefreshConfiguration] | None = None


@dataclass
class DataSetStringComparisonFilterCondition(PropertyType):
    operator: DslValue[str] | None = None
    value: DslValue[DataSetStringFilterValue] | None = None


@dataclass
class DataSetStringFilterCondition(PropertyType):
    column_name: DslValue[str] | None = None
    comparison_filter_condition: (
        DslValue[DataSetStringComparisonFilterCondition] | None
    ) = None
    list_filter_condition: DslValue[DataSetStringListFilterCondition] | None = None


@dataclass
class DataSetStringFilterValue(PropertyType):
    static_value: DslValue[str] | None = None


@dataclass
class DataSetStringListFilterCondition(PropertyType):
    operator: DslValue[str] | None = None
    values: DslValue[DataSetStringListFilterValue] | None = None


@dataclass
class DataSetStringListFilterValue(PropertyType):
    static_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataSetUsageConfiguration(PropertyType):
    disable_use_as_direct_query_source: DslValue[bool] | None = None
    disable_use_as_imported_source: DslValue[bool] | None = None


@dataclass
class DatasetParameter(PropertyType):
    date_time_dataset_parameter: DslValue[DateTimeDatasetParameter] | None = None
    decimal_dataset_parameter: DslValue[DecimalDatasetParameter] | None = None
    integer_dataset_parameter: DslValue[IntegerDatasetParameter] | None = None
    string_dataset_parameter: DslValue[StringDatasetParameter] | None = None


@dataclass
class DateTimeDatasetParameter(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    value_type: DslValue[str] | None = None
    default_values: DslValue[DateTimeDatasetParameterDefaultValues] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class DateTimeDatasetParameterDefaultValues(PropertyType):
    static_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DecimalDatasetParameter(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    value_type: DslValue[str] | None = None
    default_values: DslValue[DecimalDatasetParameterDefaultValues] | None = None


@dataclass
class DecimalDatasetParameterDefaultValues(PropertyType):
    static_values: list[DslValue[float]] = field(default_factory=list)


@dataclass
class DestinationTable(PropertyType):
    alias: DslValue[str] | None = None
    source: DslValue[DestinationTableSource] | None = None


@dataclass
class DestinationTableSource(PropertyType):
    transform_operation_id: DslValue[str] | None = None


@dataclass
class FieldFolder(PropertyType):
    columns: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None


@dataclass
class FilterOperation(PropertyType):
    condition_expression: DslValue[str] | None = None
    date_filter_condition: DslValue[DataSetDateFilterCondition] | None = None
    numeric_filter_condition: DslValue[DataSetNumericFilterCondition] | None = None
    string_filter_condition: DslValue[DataSetStringFilterCondition] | None = None


@dataclass
class FiltersOperation(PropertyType):
    alias: DslValue[str] | None = None
    filter_operations: list[DslValue[FilterOperation]] = field(default_factory=list)
    source: DslValue[TransformOperationSource] | None = None


@dataclass
class GeoSpatialColumnGroup(PropertyType):
    columns: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    country_code: DslValue[str] | None = None


@dataclass
class ImportTableOperation(PropertyType):
    alias: DslValue[str] | None = None
    source: DslValue[ImportTableOperationSource] | None = None


@dataclass
class ImportTableOperationSource(PropertyType):
    source_table_id: DslValue[str] | None = None
    column_id_mappings: list[DslValue[DataSetColumnIdMapping]] = field(
        default_factory=list
    )


@dataclass
class IncrementalRefresh(PropertyType):
    lookback_window: DslValue[LookbackWindow] | None = None


@dataclass
class IngestionWaitPolicy(PropertyType):
    ingestion_wait_time_in_hours: DslValue[float] | None = None
    wait_for_spice_ingestion: DslValue[bool] | None = None


@dataclass
class InputColumn(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    id: DslValue[str] | None = None
    sub_type: DslValue[str] | None = None


@dataclass
class IntegerDatasetParameter(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    value_type: DslValue[str] | None = None
    default_values: DslValue[IntegerDatasetParameterDefaultValues] | None = None


@dataclass
class IntegerDatasetParameterDefaultValues(PropertyType):
    static_values: list[DslValue[int]] = field(default_factory=list)


@dataclass
class JoinOperandProperties(PropertyType):
    output_column_name_overrides: list[DslValue[OutputColumnNameOverride]] = field(
        default_factory=list
    )


@dataclass
class JoinOperation(PropertyType):
    alias: DslValue[str] | None = None
    left_operand: DslValue[TransformOperationSource] | None = None
    on_clause: DslValue[str] | None = None
    right_operand: DslValue[TransformOperationSource] | None = None
    type_: DslValue[str] | None = None
    left_operand_properties: DslValue[JoinOperandProperties] | None = None
    right_operand_properties: DslValue[JoinOperandProperties] | None = None


@dataclass
class LookbackWindow(PropertyType):
    column_name: DslValue[str] | None = None
    size: DslValue[float] | None = None
    size_unit: DslValue[str] | None = None


@dataclass
class OutputColumn(PropertyType):
    description: DslValue[str] | None = None
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    sub_type: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class OutputColumnNameOverride(PropertyType):
    output_column_name: DslValue[str] | None = None
    source_column_name: DslValue[str] | None = None


@dataclass
class ParentDataSet(PropertyType):
    data_set_arn: DslValue[str] | None = None
    input_columns: list[DslValue[InputColumn]] = field(default_factory=list)


@dataclass
class PerformanceConfiguration(PropertyType):
    unique_keys: list[DslValue[UniqueKey]] = field(default_factory=list)


@dataclass
class PhysicalTable(PropertyType):
    custom_sql: DslValue[CustomSql] | None = None
    relational_table: DslValue[RelationalTable] | None = None
    s3_source: DslValue[S3Source] | None = None
    saa_s_table: DslValue[SaaSTable] | None = None


@dataclass
class PivotConfiguration(PropertyType):
    pivoted_labels: list[DslValue[PivotedLabel]] = field(default_factory=list)
    label_column_name: DslValue[str] | None = None


@dataclass
class PivotOperation(PropertyType):
    alias: DslValue[str] | None = None
    pivot_configuration: DslValue[PivotConfiguration] | None = None
    source: DslValue[TransformOperationSource] | None = None
    value_column_configuration: DslValue[ValueColumnConfiguration] | None = None
    group_by_column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PivotedLabel(PropertyType):
    label_name: DslValue[str] | None = None
    new_column_id: DslValue[str] | None = None
    new_column_name: DslValue[str] | None = None


@dataclass
class ProjectOperation(PropertyType):
    alias: DslValue[str] | None = None
    projected_columns: list[DslValue[str]] = field(default_factory=list)
    source: DslValue[TransformOperationSource] | None = None


@dataclass
class RefreshConfiguration(PropertyType):
    incremental_refresh: DslValue[IncrementalRefresh] | None = None


@dataclass
class RefreshFailureConfiguration(PropertyType):
    email_alert: DslValue[RefreshFailureEmailAlert] | None = None


@dataclass
class RefreshFailureEmailAlert(PropertyType):
    alert_status: DslValue[str] | None = None


@dataclass
class RelationalTable(PropertyType):
    data_source_arn: DslValue[str] | None = None
    input_columns: list[DslValue[InputColumn]] = field(default_factory=list)
    name: DslValue[str] | None = None
    catalog: DslValue[str] | None = None
    schema: DslValue[str] | None = None


@dataclass
class RenameColumnOperation(PropertyType):
    column_name: DslValue[str] | None = None
    new_column_name: DslValue[str] | None = None


@dataclass
class RenameColumnsOperation(PropertyType):
    alias: DslValue[str] | None = None
    rename_column_operations: list[DslValue[RenameColumnOperation]] = field(
        default_factory=list
    )
    source: DslValue[TransformOperationSource] | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[str] | None = None


@dataclass
class RowLevelPermissionConfiguration(PropertyType):
    row_level_permission_data_set: DslValue[RowLevelPermissionDataSet] | None = None
    tag_configuration: DslValue[RowLevelPermissionTagConfiguration] | None = None


@dataclass
class RowLevelPermissionDataSet(PropertyType):
    arn: DslValue[str] | None = None
    permission_policy: DslValue[str] | None = None
    format_version: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class RowLevelPermissionTagConfiguration(PropertyType):
    tag_rules: list[DslValue[RowLevelPermissionTagRule]] = field(default_factory=list)
    status: DslValue[str] | None = None
    tag_rule_configurations: DslValue[dict[str, Any]] | None = None


@dataclass
class RowLevelPermissionTagRule(PropertyType):
    column_name: DslValue[str] | None = None
    tag_key: DslValue[str] | None = None
    match_all_value: DslValue[str] | None = None
    tag_multi_value_delimiter: DslValue[str] | None = None


@dataclass
class S3Source(PropertyType):
    data_source_arn: DslValue[str] | None = None
    input_columns: list[DslValue[InputColumn]] = field(default_factory=list)
    upload_settings: DslValue[UploadSettings] | None = None


@dataclass
class SaaSTable(PropertyType):
    data_source_arn: DslValue[str] | None = None
    input_columns: list[DslValue[InputColumn]] = field(default_factory=list)
    table_path: list[DslValue[TablePathElement]] = field(default_factory=list)


@dataclass
class SemanticModelConfiguration(PropertyType):
    table_map: dict[str, DslValue[SemanticTable]] = field(default_factory=dict)


@dataclass
class SemanticTable(PropertyType):
    alias: DslValue[str] | None = None
    destination_table_id: DslValue[str] | None = None
    row_level_permission_configuration: (
        DslValue[RowLevelPermissionConfiguration] | None
    ) = None


@dataclass
class SourceTable(PropertyType):
    data_set: DslValue[ParentDataSet] | None = None
    physical_table_id: DslValue[str] | None = None


@dataclass
class StringDatasetParameter(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    value_type: DslValue[str] | None = None
    default_values: DslValue[StringDatasetParameterDefaultValues] | None = None


@dataclass
class StringDatasetParameterDefaultValues(PropertyType):
    static_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TablePathElement(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class TransformOperationSource(PropertyType):
    transform_operation_id: DslValue[str] | None = None
    column_id_mappings: list[DslValue[DataSetColumnIdMapping]] = field(
        default_factory=list
    )


@dataclass
class TransformStep(PropertyType):
    aggregate_step: DslValue[AggregateOperation] | None = None
    append_step: DslValue[AppendOperation] | None = None
    cast_column_types_step: DslValue[CastColumnTypesOperation] | None = None
    create_columns_step: DslValue[CreateColumnsOperation] | None = None
    filters_step: DslValue[FiltersOperation] | None = None
    import_table_step: DslValue[ImportTableOperation] | None = None
    join_step: DslValue[JoinOperation] | None = None
    pivot_step: DslValue[PivotOperation] | None = None
    project_step: DslValue[ProjectOperation] | None = None
    rename_columns_step: DslValue[RenameColumnsOperation] | None = None
    unpivot_step: DslValue[UnpivotOperation] | None = None


@dataclass
class UniqueKey(PropertyType):
    column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class UnpivotOperation(PropertyType):
    alias: DslValue[str] | None = None
    columns_to_unpivot: list[DslValue[ColumnToUnpivot]] = field(default_factory=list)
    source: DslValue[TransformOperationSource] | None = None
    unpivoted_label_column_id: DslValue[str] | None = None
    unpivoted_label_column_name: DslValue[str] | None = None
    unpivoted_value_column_id: DslValue[str] | None = None
    unpivoted_value_column_name: DslValue[str] | None = None


@dataclass
class UploadSettings(PropertyType):
    contains_header: DslValue[bool] | None = None
    delimiter: DslValue[str] | None = None
    format: DslValue[str] | None = None
    start_from_row: DslValue[float] | None = None
    text_qualifier: DslValue[str] | None = None


@dataclass
class ValueColumnConfiguration(PropertyType):
    aggregation_function: DslValue[DataPrepAggregationFunction] | None = None
