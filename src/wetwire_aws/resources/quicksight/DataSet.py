"""PropertyTypes for AWS::QuickSight::DataSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AggregateOperation(PropertyType):
    aggregations: list[Aggregation] = field(default_factory=list)
    alias: str | None = None
    source: TransformOperationSource | None = None
    group_by_column_names: list[String] = field(default_factory=list)


@dataclass
class Aggregation(PropertyType):
    aggregation_function: DataPrepAggregationFunction | None = None
    new_column_id: str | None = None
    new_column_name: str | None = None


@dataclass
class AppendOperation(PropertyType):
    alias: str | None = None
    appended_columns: list[AppendedColumn] = field(default_factory=list)
    first_source: TransformOperationSource | None = None
    second_source: TransformOperationSource | None = None


@dataclass
class AppendedColumn(PropertyType):
    column_name: str | None = None
    new_column_id: str | None = None


@dataclass
class CalculatedColumn(PropertyType):
    column_id: str | None = None
    column_name: str | None = None
    expression: str | None = None


@dataclass
class CastColumnTypeOperation(PropertyType):
    column_name: str | None = None
    new_column_type: str | None = None
    format: str | None = None
    sub_type: str | None = None


@dataclass
class CastColumnTypesOperation(PropertyType):
    alias: str | None = None
    cast_column_type_operations: list[CastColumnTypeOperation] = field(
        default_factory=list
    )
    source: TransformOperationSource | None = None


@dataclass
class ColumnGroup(PropertyType):
    geo_spatial_column_group: GeoSpatialColumnGroup | None = None


@dataclass
class ColumnLevelPermissionRule(PropertyType):
    column_names: list[String] = field(default_factory=list)
    principals: list[String] = field(default_factory=list)


@dataclass
class ColumnToUnpivot(PropertyType):
    column_name: str | None = None
    new_value: str | None = None


@dataclass
class CreateColumnsOperation(PropertyType):
    columns: list[CalculatedColumn] = field(default_factory=list)
    alias: str | None = None
    source: TransformOperationSource | None = None


@dataclass
class CustomSql(PropertyType):
    columns: list[InputColumn] = field(default_factory=list)
    data_source_arn: str | None = None
    name: str | None = None
    sql_query: str | None = None


@dataclass
class DataPrepAggregationFunction(PropertyType):
    list_aggregation: DataPrepListAggregationFunction | None = None
    percentile_aggregation: DataPrepPercentileAggregationFunction | None = None
    simple_aggregation: DataPrepSimpleAggregationFunction | None = None


@dataclass
class DataPrepConfiguration(PropertyType):
    destination_table_map: dict[str, DestinationTable] = field(default_factory=dict)
    source_table_map: dict[str, SourceTable] = field(default_factory=dict)
    transform_step_map: dict[str, TransformStep] = field(default_factory=dict)


@dataclass
class DataPrepListAggregationFunction(PropertyType):
    distinct: bool | None = None
    separator: str | None = None
    input_column_name: str | None = None


@dataclass
class DataPrepPercentileAggregationFunction(PropertyType):
    percentile_value: float | None = None
    input_column_name: str | None = None


@dataclass
class DataPrepSimpleAggregationFunction(PropertyType):
    function_type: str | None = None
    input_column_name: str | None = None


@dataclass
class DataSetColumnIdMapping(PropertyType):
    source_column_id: str | None = None
    target_column_id: str | None = None


@dataclass
class DataSetDateComparisonFilterCondition(PropertyType):
    operator: str | None = None
    value: DataSetDateFilterValue | None = None


@dataclass
class DataSetDateFilterCondition(PropertyType):
    column_name: str | None = None
    comparison_filter_condition: DataSetDateComparisonFilterCondition | None = None
    range_filter_condition: DataSetDateRangeFilterCondition | None = None


@dataclass
class DataSetDateFilterValue(PropertyType):
    static_value: str | None = None


@dataclass
class DataSetDateRangeFilterCondition(PropertyType):
    include_maximum: bool | None = None
    include_minimum: bool | None = None
    range_maximum: DataSetDateFilterValue | None = None
    range_minimum: DataSetDateFilterValue | None = None


@dataclass
class DataSetNumericComparisonFilterCondition(PropertyType):
    operator: str | None = None
    value: DataSetNumericFilterValue | None = None


@dataclass
class DataSetNumericFilterCondition(PropertyType):
    column_name: str | None = None
    comparison_filter_condition: DataSetNumericComparisonFilterCondition | None = None
    range_filter_condition: DataSetNumericRangeFilterCondition | None = None


@dataclass
class DataSetNumericFilterValue(PropertyType):
    static_value: float | None = None


@dataclass
class DataSetNumericRangeFilterCondition(PropertyType):
    include_maximum: bool | None = None
    include_minimum: bool | None = None
    range_maximum: DataSetNumericFilterValue | None = None
    range_minimum: DataSetNumericFilterValue | None = None


@dataclass
class DataSetRefreshProperties(PropertyType):
    failure_configuration: RefreshFailureConfiguration | None = None
    refresh_configuration: RefreshConfiguration | None = None


@dataclass
class DataSetStringComparisonFilterCondition(PropertyType):
    operator: str | None = None
    value: DataSetStringFilterValue | None = None


@dataclass
class DataSetStringFilterCondition(PropertyType):
    column_name: str | None = None
    comparison_filter_condition: DataSetStringComparisonFilterCondition | None = None
    list_filter_condition: DataSetStringListFilterCondition | None = None


@dataclass
class DataSetStringFilterValue(PropertyType):
    static_value: str | None = None


@dataclass
class DataSetStringListFilterCondition(PropertyType):
    operator: str | None = None
    values: DataSetStringListFilterValue | None = None


@dataclass
class DataSetStringListFilterValue(PropertyType):
    static_values: list[String] = field(default_factory=list)


@dataclass
class DataSetUsageConfiguration(PropertyType):
    disable_use_as_direct_query_source: bool | None = None
    disable_use_as_imported_source: bool | None = None


@dataclass
class DatasetParameter(PropertyType):
    date_time_dataset_parameter: DateTimeDatasetParameter | None = None
    decimal_dataset_parameter: DecimalDatasetParameter | None = None
    integer_dataset_parameter: IntegerDatasetParameter | None = None
    string_dataset_parameter: StringDatasetParameter | None = None


@dataclass
class DateTimeDatasetParameter(PropertyType):
    id: str | None = None
    name: str | None = None
    value_type: str | None = None
    default_values: DateTimeDatasetParameterDefaultValues | None = None
    time_granularity: str | None = None


@dataclass
class DateTimeDatasetParameterDefaultValues(PropertyType):
    static_values: list[String] = field(default_factory=list)


@dataclass
class DecimalDatasetParameter(PropertyType):
    id: str | None = None
    name: str | None = None
    value_type: str | None = None
    default_values: DecimalDatasetParameterDefaultValues | None = None


@dataclass
class DecimalDatasetParameterDefaultValues(PropertyType):
    static_values: list[Double] = field(default_factory=list)


@dataclass
class DestinationTable(PropertyType):
    alias: str | None = None
    source: DestinationTableSource | None = None


@dataclass
class DestinationTableSource(PropertyType):
    transform_operation_id: str | None = None


@dataclass
class FieldFolder(PropertyType):
    columns: list[String] = field(default_factory=list)
    description: str | None = None


@dataclass
class FilterOperation(PropertyType):
    condition_expression: str | None = None
    date_filter_condition: DataSetDateFilterCondition | None = None
    numeric_filter_condition: DataSetNumericFilterCondition | None = None
    string_filter_condition: DataSetStringFilterCondition | None = None


@dataclass
class FiltersOperation(PropertyType):
    alias: str | None = None
    filter_operations: list[FilterOperation] = field(default_factory=list)
    source: TransformOperationSource | None = None


@dataclass
class GeoSpatialColumnGroup(PropertyType):
    columns: list[String] = field(default_factory=list)
    name: str | None = None
    country_code: str | None = None


@dataclass
class ImportTableOperation(PropertyType):
    alias: str | None = None
    source: ImportTableOperationSource | None = None


@dataclass
class ImportTableOperationSource(PropertyType):
    source_table_id: str | None = None
    column_id_mappings: list[DataSetColumnIdMapping] = field(default_factory=list)


@dataclass
class IncrementalRefresh(PropertyType):
    lookback_window: LookbackWindow | None = None


@dataclass
class IngestionWaitPolicy(PropertyType):
    ingestion_wait_time_in_hours: float | None = None
    wait_for_spice_ingestion: bool | None = None


@dataclass
class InputColumn(PropertyType):
    name: str | None = None
    type_: str | None = None
    id: str | None = None
    sub_type: str | None = None


@dataclass
class IntegerDatasetParameter(PropertyType):
    id: str | None = None
    name: str | None = None
    value_type: str | None = None
    default_values: IntegerDatasetParameterDefaultValues | None = None


@dataclass
class IntegerDatasetParameterDefaultValues(PropertyType):
    static_values: list[Long] = field(default_factory=list)


@dataclass
class JoinOperandProperties(PropertyType):
    output_column_name_overrides: list[OutputColumnNameOverride] = field(
        default_factory=list
    )


@dataclass
class JoinOperation(PropertyType):
    alias: str | None = None
    left_operand: TransformOperationSource | None = None
    on_clause: str | None = None
    right_operand: TransformOperationSource | None = None
    type_: str | None = None
    left_operand_properties: JoinOperandProperties | None = None
    right_operand_properties: JoinOperandProperties | None = None


@dataclass
class LookbackWindow(PropertyType):
    column_name: str | None = None
    size: float | None = None
    size_unit: str | None = None


@dataclass
class OutputColumn(PropertyType):
    description: str | None = None
    id: str | None = None
    name: str | None = None
    sub_type: str | None = None
    type_: str | None = None


@dataclass
class OutputColumnNameOverride(PropertyType):
    output_column_name: str | None = None
    source_column_name: str | None = None


@dataclass
class ParentDataSet(PropertyType):
    data_set_arn: str | None = None
    input_columns: list[InputColumn] = field(default_factory=list)


@dataclass
class PerformanceConfiguration(PropertyType):
    unique_keys: list[UniqueKey] = field(default_factory=list)


@dataclass
class PhysicalTable(PropertyType):
    custom_sql: CustomSql | None = None
    relational_table: RelationalTable | None = None
    s3_source: S3Source | None = None
    saa_s_table: SaaSTable | None = None


@dataclass
class PivotConfiguration(PropertyType):
    pivoted_labels: list[PivotedLabel] = field(default_factory=list)
    label_column_name: str | None = None


@dataclass
class PivotOperation(PropertyType):
    alias: str | None = None
    pivot_configuration: PivotConfiguration | None = None
    source: TransformOperationSource | None = None
    value_column_configuration: ValueColumnConfiguration | None = None
    group_by_column_names: list[String] = field(default_factory=list)


@dataclass
class PivotedLabel(PropertyType):
    label_name: str | None = None
    new_column_id: str | None = None
    new_column_name: str | None = None


@dataclass
class ProjectOperation(PropertyType):
    alias: str | None = None
    projected_columns: list[String] = field(default_factory=list)
    source: TransformOperationSource | None = None


@dataclass
class RefreshConfiguration(PropertyType):
    incremental_refresh: IncrementalRefresh | None = None


@dataclass
class RefreshFailureConfiguration(PropertyType):
    email_alert: RefreshFailureEmailAlert | None = None


@dataclass
class RefreshFailureEmailAlert(PropertyType):
    alert_status: str | None = None


@dataclass
class RelationalTable(PropertyType):
    data_source_arn: str | None = None
    input_columns: list[InputColumn] = field(default_factory=list)
    name: str | None = None
    catalog: str | None = None
    schema: str | None = None


@dataclass
class RenameColumnOperation(PropertyType):
    column_name: str | None = None
    new_column_name: str | None = None


@dataclass
class RenameColumnsOperation(PropertyType):
    alias: str | None = None
    rename_column_operations: list[RenameColumnOperation] = field(default_factory=list)
    source: TransformOperationSource | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[String] = field(default_factory=list)
    principal: str | None = None


@dataclass
class RowLevelPermissionConfiguration(PropertyType):
    row_level_permission_data_set: RowLevelPermissionDataSet | None = None
    tag_configuration: RowLevelPermissionTagConfiguration | None = None


@dataclass
class RowLevelPermissionDataSet(PropertyType):
    arn: str | None = None
    permission_policy: str | None = None
    format_version: str | None = None
    namespace: str | None = None
    status: str | None = None


@dataclass
class RowLevelPermissionTagConfiguration(PropertyType):
    tag_rules: list[RowLevelPermissionTagRule] = field(default_factory=list)
    status: str | None = None
    tag_rule_configurations: dict[str, Any] | None = None


@dataclass
class RowLevelPermissionTagRule(PropertyType):
    column_name: str | None = None
    tag_key: str | None = None
    match_all_value: str | None = None
    tag_multi_value_delimiter: str | None = None


@dataclass
class S3Source(PropertyType):
    data_source_arn: str | None = None
    input_columns: list[InputColumn] = field(default_factory=list)
    upload_settings: UploadSettings | None = None


@dataclass
class SaaSTable(PropertyType):
    data_source_arn: str | None = None
    input_columns: list[InputColumn] = field(default_factory=list)
    table_path: list[TablePathElement] = field(default_factory=list)


@dataclass
class SemanticModelConfiguration(PropertyType):
    table_map: dict[str, SemanticTable] = field(default_factory=dict)


@dataclass
class SemanticTable(PropertyType):
    alias: str | None = None
    destination_table_id: str | None = None
    row_level_permission_configuration: RowLevelPermissionConfiguration | None = None


@dataclass
class SourceTable(PropertyType):
    data_set: ParentDataSet | None = None
    physical_table_id: str | None = None


@dataclass
class StringDatasetParameter(PropertyType):
    id: str | None = None
    name: str | None = None
    value_type: str | None = None
    default_values: StringDatasetParameterDefaultValues | None = None


@dataclass
class StringDatasetParameterDefaultValues(PropertyType):
    static_values: list[String] = field(default_factory=list)


@dataclass
class TablePathElement(PropertyType):
    id: str | None = None
    name: str | None = None


@dataclass
class TransformOperationSource(PropertyType):
    transform_operation_id: str | None = None
    column_id_mappings: list[DataSetColumnIdMapping] = field(default_factory=list)


@dataclass
class TransformStep(PropertyType):
    aggregate_step: AggregateOperation | None = None
    append_step: AppendOperation | None = None
    cast_column_types_step: CastColumnTypesOperation | None = None
    create_columns_step: CreateColumnsOperation | None = None
    filters_step: FiltersOperation | None = None
    import_table_step: ImportTableOperation | None = None
    join_step: JoinOperation | None = None
    pivot_step: PivotOperation | None = None
    project_step: ProjectOperation | None = None
    rename_columns_step: RenameColumnsOperation | None = None
    unpivot_step: UnpivotOperation | None = None


@dataclass
class UniqueKey(PropertyType):
    column_names: list[String] = field(default_factory=list)


@dataclass
class UnpivotOperation(PropertyType):
    alias: str | None = None
    columns_to_unpivot: list[ColumnToUnpivot] = field(default_factory=list)
    source: TransformOperationSource | None = None
    unpivoted_label_column_id: str | None = None
    unpivoted_label_column_name: str | None = None
    unpivoted_value_column_id: str | None = None
    unpivoted_value_column_name: str | None = None


@dataclass
class UploadSettings(PropertyType):
    contains_header: bool | None = None
    delimiter: str | None = None
    format: str | None = None
    start_from_row: float | None = None
    text_qualifier: str | None = None


@dataclass
class ValueColumnConfiguration(PropertyType):
    aggregation_function: DataPrepAggregationFunction | None = None
