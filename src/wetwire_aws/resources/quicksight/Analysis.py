"""PropertyTypes for AWS::QuickSight::Analysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AggregationFunction(PropertyType):
    attribute_aggregation_function: AttributeAggregationFunction | None = None
    categorical_aggregation_function: str | None = None
    date_aggregation_function: str | None = None
    numerical_aggregation_function: NumericalAggregationFunction | None = None


@dataclass
class AggregationSortConfiguration(PropertyType):
    column: ColumnIdentifier | None = None
    sort_direction: str | None = None
    aggregation_function: AggregationFunction | None = None


@dataclass
class AnalysisDefaults(PropertyType):
    default_new_sheet_configuration: DefaultNewSheetConfiguration | None = None


@dataclass
class AnalysisDefinition(PropertyType):
    data_set_identifier_declarations: list[DataSetIdentifierDeclaration] = field(
        default_factory=list
    )
    analysis_defaults: AnalysisDefaults | None = None
    calculated_fields: list[CalculatedField] = field(default_factory=list)
    column_configurations: list[ColumnConfiguration] = field(default_factory=list)
    filter_groups: list[FilterGroup] = field(default_factory=list)
    options: AssetOptions | None = None
    parameter_declarations: list[ParameterDeclaration] = field(default_factory=list)
    query_execution_options: QueryExecutionOptions | None = None
    sheets: list[SheetDefinition] = field(default_factory=list)
    static_files: list[StaticFile] = field(default_factory=list)


@dataclass
class AnalysisError(PropertyType):
    message: str | None = None
    type_: str | None = None
    violated_entities: list[Entity] = field(default_factory=list)


@dataclass
class AnalysisSourceEntity(PropertyType):
    source_template: AnalysisSourceTemplate | None = None


@dataclass
class AnalysisSourceTemplate(PropertyType):
    arn: str | None = None
    data_set_references: list[DataSetReference] = field(default_factory=list)


@dataclass
class AnchorDateConfiguration(PropertyType):
    anchor_option: str | None = None
    parameter_name: str | None = None


@dataclass
class ArcAxisConfiguration(PropertyType):
    range: ArcAxisDisplayRange | None = None
    reserve_range: float | None = None


@dataclass
class ArcAxisDisplayRange(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class ArcConfiguration(PropertyType):
    arc_angle: float | None = None
    arc_thickness: str | None = None


@dataclass
class ArcOptions(PropertyType):
    arc_thickness: str | None = None


@dataclass
class AssetOptions(PropertyType):
    timezone: str | None = None
    week_start: str | None = None


@dataclass
class AttributeAggregationFunction(PropertyType):
    simple_attribute_aggregation: str | None = None
    value_for_multiple_values: str | None = None


@dataclass
class AxisDataOptions(PropertyType):
    date_axis_options: DateAxisOptions | None = None
    numeric_axis_options: NumericAxisOptions | None = None


@dataclass
class AxisDisplayMinMaxRange(PropertyType):
    maximum: float | None = None
    minimum: float | None = None


@dataclass
class AxisDisplayOptions(PropertyType):
    axis_line_visibility: str | None = None
    axis_offset: str | None = None
    data_options: AxisDataOptions | None = None
    grid_line_visibility: str | None = None
    scrollbar_options: ScrollBarOptions | None = None
    tick_label_options: AxisTickLabelOptions | None = None


@dataclass
class AxisDisplayRange(PropertyType):
    data_driven: dict[str, Any] | None = None
    min_max: AxisDisplayMinMaxRange | None = None


@dataclass
class AxisLabelOptions(PropertyType):
    apply_to: AxisLabelReferenceOptions | None = None
    custom_label: str | None = None
    font_configuration: FontConfiguration | None = None


@dataclass
class AxisLabelReferenceOptions(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None


@dataclass
class AxisLinearScale(PropertyType):
    step_count: float | None = None
    step_size: float | None = None


@dataclass
class AxisLogarithmicScale(PropertyType):
    base: float | None = None


@dataclass
class AxisScale(PropertyType):
    linear: AxisLinearScale | None = None
    logarithmic: AxisLogarithmicScale | None = None


@dataclass
class AxisTickLabelOptions(PropertyType):
    label_options: LabelOptions | None = None
    rotation_angle: float | None = None


@dataclass
class BarChartAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    colors: list[DimensionField] = field(default_factory=list)
    small_multiples: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class BarChartConfiguration(PropertyType):
    bars_arrangement: str | None = None
    category_axis: AxisDisplayOptions | None = None
    category_label_options: ChartAxisLabelOptions | None = None
    color_label_options: ChartAxisLabelOptions | None = None
    contribution_analysis_defaults: list[ContributionAnalysisDefault] = field(
        default_factory=list
    )
    data_labels: DataLabelOptions | None = None
    field_wells: BarChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    orientation: str | None = None
    reference_lines: list[ReferenceLine] = field(default_factory=list)
    small_multiples_options: SmallMultiplesOptions | None = None
    sort_configuration: BarChartSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    value_axis: AxisDisplayOptions | None = None
    value_label_options: ChartAxisLabelOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class BarChartFieldWells(PropertyType):
    bar_chart_aggregated_field_wells: BarChartAggregatedFieldWells | None = None


@dataclass
class BarChartSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    color_items_limit: ItemsLimitConfiguration | None = None
    color_sort: list[FieldSortOptions] = field(default_factory=list)
    small_multiples_limit_configuration: ItemsLimitConfiguration | None = None
    small_multiples_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class BarChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: BarChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class BinCountOptions(PropertyType):
    value: float | None = None


@dataclass
class BinWidthOptions(PropertyType):
    bin_count_limit: float | None = None
    value: float | None = None


@dataclass
class BodySectionConfiguration(PropertyType):
    content: BodySectionContent | None = None
    section_id: str | None = None
    page_break_configuration: SectionPageBreakConfiguration | None = None
    repeat_configuration: BodySectionRepeatConfiguration | None = None
    style: SectionStyle | None = None


@dataclass
class BodySectionContent(PropertyType):
    layout: SectionLayoutConfiguration | None = None


@dataclass
class BodySectionDynamicCategoryDimensionConfiguration(PropertyType):
    column: ColumnIdentifier | None = None
    limit: float | None = None
    sort_by_metrics: list[ColumnSort] = field(default_factory=list)


@dataclass
class BodySectionDynamicNumericDimensionConfiguration(PropertyType):
    column: ColumnIdentifier | None = None
    limit: float | None = None
    sort_by_metrics: list[ColumnSort] = field(default_factory=list)


@dataclass
class BodySectionRepeatConfiguration(PropertyType):
    dimension_configurations: list[BodySectionRepeatDimensionConfiguration] = field(
        default_factory=list
    )
    non_repeating_visuals: list[String] = field(default_factory=list)
    page_break_configuration: BodySectionRepeatPageBreakConfiguration | None = None


@dataclass
class BodySectionRepeatDimensionConfiguration(PropertyType):
    dynamic_category_dimension_configuration: (
        BodySectionDynamicCategoryDimensionConfiguration | None
    ) = None
    dynamic_numeric_dimension_configuration: (
        BodySectionDynamicNumericDimensionConfiguration | None
    ) = None


@dataclass
class BodySectionRepeatPageBreakConfiguration(PropertyType):
    after: SectionAfterPageBreak | None = None


@dataclass
class BoxPlotAggregatedFieldWells(PropertyType):
    group_by: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class BoxPlotChartConfiguration(PropertyType):
    box_plot_options: BoxPlotOptions | None = None
    category_axis: AxisDisplayOptions | None = None
    category_label_options: ChartAxisLabelOptions | None = None
    field_wells: BoxPlotFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    primary_y_axis_display_options: AxisDisplayOptions | None = None
    primary_y_axis_label_options: ChartAxisLabelOptions | None = None
    reference_lines: list[ReferenceLine] = field(default_factory=list)
    sort_configuration: BoxPlotSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class BoxPlotFieldWells(PropertyType):
    box_plot_aggregated_field_wells: BoxPlotAggregatedFieldWells | None = None


@dataclass
class BoxPlotOptions(PropertyType):
    all_data_points_visibility: str | None = None
    outlier_visibility: str | None = None
    style_options: BoxPlotStyleOptions | None = None


@dataclass
class BoxPlotSortConfiguration(PropertyType):
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    pagination_configuration: PaginationConfiguration | None = None


@dataclass
class BoxPlotStyleOptions(PropertyType):
    fill_style: str | None = None


@dataclass
class BoxPlotVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: BoxPlotChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class CalculatedField(PropertyType):
    data_set_identifier: str | None = None
    expression: str | None = None
    name: str | None = None


@dataclass
class CalculatedMeasureField(PropertyType):
    expression: str | None = None
    field_id: str | None = None


@dataclass
class CascadingControlConfiguration(PropertyType):
    source_controls: list[CascadingControlSource] = field(default_factory=list)


@dataclass
class CascadingControlSource(PropertyType):
    column_to_match: ColumnIdentifier | None = None
    source_sheet_control_id: str | None = None


@dataclass
class CategoricalDimensionField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    format_configuration: StringFormatConfiguration | None = None
    hierarchy_id: str | None = None


@dataclass
class CategoricalMeasureField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    aggregation_function: str | None = None
    format_configuration: StringFormatConfiguration | None = None


@dataclass
class CategoryDrillDownFilter(PropertyType):
    category_values: list[String] = field(default_factory=list)
    column: ColumnIdentifier | None = None


@dataclass
class CategoryFilter(PropertyType):
    column: ColumnIdentifier | None = None
    configuration: CategoryFilterConfiguration | None = None
    filter_id: str | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )


@dataclass
class CategoryFilterConfiguration(PropertyType):
    custom_filter_configuration: CustomFilterConfiguration | None = None
    custom_filter_list_configuration: CustomFilterListConfiguration | None = None
    filter_list_configuration: FilterListConfiguration | None = None


@dataclass
class CategoryInnerFilter(PropertyType):
    column: ColumnIdentifier | None = None
    configuration: CategoryFilterConfiguration | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )


@dataclass
class ChartAxisLabelOptions(PropertyType):
    axis_label_options: list[AxisLabelOptions] = field(default_factory=list)
    sort_icon_visibility: str | None = None
    visibility: str | None = None


@dataclass
class ClusterMarker(PropertyType):
    simple_cluster_marker: SimpleClusterMarker | None = None


@dataclass
class ClusterMarkerConfiguration(PropertyType):
    cluster_marker: ClusterMarker | None = None


@dataclass
class ColorScale(PropertyType):
    color_fill_type: str | None = None
    colors: list[DataColor] = field(default_factory=list)
    null_value_color: DataColor | None = None


@dataclass
class ColorsConfiguration(PropertyType):
    custom_colors: list[CustomColor] = field(default_factory=list)


@dataclass
class ColumnConfiguration(PropertyType):
    column: ColumnIdentifier | None = None
    colors_configuration: ColorsConfiguration | None = None
    format_configuration: FormatConfiguration | None = None
    role: str | None = None


@dataclass
class ColumnHierarchy(PropertyType):
    date_time_hierarchy: DateTimeHierarchy | None = None
    explicit_hierarchy: ExplicitHierarchy | None = None
    predefined_hierarchy: PredefinedHierarchy | None = None


@dataclass
class ColumnIdentifier(PropertyType):
    column_name: str | None = None
    data_set_identifier: str | None = None


@dataclass
class ColumnSort(PropertyType):
    direction: str | None = None
    sort_by: ColumnIdentifier | None = None
    aggregation_function: AggregationFunction | None = None


@dataclass
class ColumnTooltipItem(PropertyType):
    column: ColumnIdentifier | None = None
    aggregation: AggregationFunction | None = None
    label: str | None = None
    tooltip_target: str | None = None
    visibility: str | None = None


@dataclass
class ComboChartAggregatedFieldWells(PropertyType):
    bar_values: list[MeasureField] = field(default_factory=list)
    category: list[DimensionField] = field(default_factory=list)
    colors: list[DimensionField] = field(default_factory=list)
    line_values: list[MeasureField] = field(default_factory=list)


@dataclass
class ComboChartConfiguration(PropertyType):
    bar_data_labels: DataLabelOptions | None = None
    bars_arrangement: str | None = None
    category_axis: AxisDisplayOptions | None = None
    category_label_options: ChartAxisLabelOptions | None = None
    color_label_options: ChartAxisLabelOptions | None = None
    field_wells: ComboChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    line_data_labels: DataLabelOptions | None = None
    primary_y_axis_display_options: AxisDisplayOptions | None = None
    primary_y_axis_label_options: ChartAxisLabelOptions | None = None
    reference_lines: list[ReferenceLine] = field(default_factory=list)
    secondary_y_axis_display_options: AxisDisplayOptions | None = None
    secondary_y_axis_label_options: ChartAxisLabelOptions | None = None
    single_axis_options: SingleAxisOptions | None = None
    sort_configuration: ComboChartSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class ComboChartFieldWells(PropertyType):
    combo_chart_aggregated_field_wells: ComboChartAggregatedFieldWells | None = None


@dataclass
class ComboChartSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    color_items_limit: ItemsLimitConfiguration | None = None
    color_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class ComboChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: ComboChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class ComparisonConfiguration(PropertyType):
    comparison_format: ComparisonFormatConfiguration | None = None
    comparison_method: str | None = None


@dataclass
class ComparisonFormatConfiguration(PropertyType):
    number_display_format_configuration: NumberDisplayFormatConfiguration | None = None
    percentage_display_format_configuration: (
        PercentageDisplayFormatConfiguration | None
    ) = None


@dataclass
class Computation(PropertyType):
    forecast: ForecastComputation | None = None
    growth_rate: GrowthRateComputation | None = None
    maximum_minimum: MaximumMinimumComputation | None = None
    metric_comparison: MetricComparisonComputation | None = None
    period_over_period: PeriodOverPeriodComputation | None = None
    period_to_date: PeriodToDateComputation | None = None
    top_bottom_movers: TopBottomMoversComputation | None = None
    top_bottom_ranked: TopBottomRankedComputation | None = None
    total_aggregation: TotalAggregationComputation | None = None
    unique_values: UniqueValuesComputation | None = None


@dataclass
class ConditionalFormattingColor(PropertyType):
    gradient: ConditionalFormattingGradientColor | None = None
    solid: ConditionalFormattingSolidColor | None = None


@dataclass
class ConditionalFormattingCustomIconCondition(PropertyType):
    expression: str | None = None
    icon_options: ConditionalFormattingCustomIconOptions | None = None
    color: str | None = None
    display_configuration: ConditionalFormattingIconDisplayConfiguration | None = None


@dataclass
class ConditionalFormattingCustomIconOptions(PropertyType):
    icon: str | None = None
    unicode_icon: str | None = None


@dataclass
class ConditionalFormattingGradientColor(PropertyType):
    color: GradientColor | None = None
    expression: str | None = None


@dataclass
class ConditionalFormattingIcon(PropertyType):
    custom_condition: ConditionalFormattingCustomIconCondition | None = None
    icon_set: ConditionalFormattingIconSet | None = None


@dataclass
class ConditionalFormattingIconDisplayConfiguration(PropertyType):
    icon_display_option: str | None = None


@dataclass
class ConditionalFormattingIconSet(PropertyType):
    expression: str | None = None
    icon_set_type: str | None = None


@dataclass
class ConditionalFormattingSolidColor(PropertyType):
    expression: str | None = None
    color: str | None = None


@dataclass
class ContextMenuOption(PropertyType):
    availability_status: str | None = None


@dataclass
class ContributionAnalysisDefault(PropertyType):
    contributor_dimensions: list[ColumnIdentifier] = field(default_factory=list)
    measure_field_id: str | None = None


@dataclass
class CurrencyDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DecimalPlacesConfiguration | None = None
    negative_value_configuration: NegativeValueConfiguration | None = None
    null_value_format_configuration: NullValueFormatConfiguration | None = None
    number_scale: str | None = None
    prefix: str | None = None
    separator_configuration: NumericSeparatorConfiguration | None = None
    suffix: str | None = None
    symbol: str | None = None


@dataclass
class CustomActionFilterOperation(PropertyType):
    selected_fields_configuration: FilterOperationSelectedFieldsConfiguration | None = (
        None
    )
    target_visuals_configuration: FilterOperationTargetVisualsConfiguration | None = (
        None
    )


@dataclass
class CustomActionNavigationOperation(PropertyType):
    local_navigation_configuration: LocalNavigationConfiguration | None = None


@dataclass
class CustomActionSetParametersOperation(PropertyType):
    parameter_value_configurations: list[SetParameterValueConfiguration] = field(
        default_factory=list
    )


@dataclass
class CustomActionURLOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_target": "URLTarget",
        "url_template": "URLTemplate",
    }

    url_target: str | None = None
    url_template: str | None = None


@dataclass
class CustomColor(PropertyType):
    color: str | None = None
    field_value: str | None = None
    special_value: str | None = None


@dataclass
class CustomContentConfiguration(PropertyType):
    content_type: str | None = None
    content_url: str | None = None
    image_scaling: str | None = None
    interactions: VisualInteractionOptions | None = None


@dataclass
class CustomContentVisual(PropertyType):
    data_set_identifier: str | None = None
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: CustomContentConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class CustomFilterConfiguration(PropertyType):
    match_operator: str | None = None
    null_option: str | None = None
    category_value: str | None = None
    parameter_name: str | None = None
    select_all_options: str | None = None


@dataclass
class CustomFilterListConfiguration(PropertyType):
    match_operator: str | None = None
    null_option: str | None = None
    category_values: list[String] = field(default_factory=list)
    select_all_options: str | None = None


@dataclass
class CustomNarrativeOptions(PropertyType):
    narrative: str | None = None


@dataclass
class CustomParameterValues(PropertyType):
    date_time_values: list[String] = field(default_factory=list)
    decimal_values: list[Double] = field(default_factory=list)
    integer_values: list[Double] = field(default_factory=list)
    string_values: list[String] = field(default_factory=list)


@dataclass
class CustomValuesConfiguration(PropertyType):
    custom_values: CustomParameterValues | None = None
    include_null_value: bool | None = None


@dataclass
class DataBarsOptions(PropertyType):
    field_id: str | None = None
    negative_color: str | None = None
    positive_color: str | None = None


@dataclass
class DataColor(PropertyType):
    color: str | None = None
    data_value: float | None = None


@dataclass
class DataFieldSeriesItem(PropertyType):
    axis_binding: str | None = None
    field_id: str | None = None
    field_value: str | None = None
    settings: LineChartSeriesSettings | None = None


@dataclass
class DataLabelOptions(PropertyType):
    category_label_visibility: str | None = None
    data_label_types: list[DataLabelType] = field(default_factory=list)
    label_color: str | None = None
    label_content: str | None = None
    label_font_configuration: FontConfiguration | None = None
    measure_label_visibility: str | None = None
    overlap: str | None = None
    position: str | None = None
    totals_visibility: str | None = None
    visibility: str | None = None


@dataclass
class DataLabelType(PropertyType):
    data_path_label_type: DataPathLabelType | None = None
    field_label_type: FieldLabelType | None = None
    maximum_label_type: MaximumLabelType | None = None
    minimum_label_type: MinimumLabelType | None = None
    range_ends_label_type: RangeEndsLabelType | None = None


@dataclass
class DataPathColor(PropertyType):
    color: str | None = None
    element: DataPathValue | None = None
    time_granularity: str | None = None


@dataclass
class DataPathLabelType(PropertyType):
    field_id: str | None = None
    field_value: str | None = None
    visibility: str | None = None


@dataclass
class DataPathSort(PropertyType):
    direction: str | None = None
    sort_paths: list[DataPathValue] = field(default_factory=list)


@dataclass
class DataPathType(PropertyType):
    pivot_table_data_path_type: str | None = None


@dataclass
class DataPathValue(PropertyType):
    data_path_type: DataPathType | None = None
    field_id: str | None = None
    field_value: str | None = None


@dataclass
class DataSetIdentifierDeclaration(PropertyType):
    data_set_arn: str | None = None
    identifier: str | None = None


@dataclass
class DataSetReference(PropertyType):
    data_set_arn: str | None = None
    data_set_placeholder: str | None = None


@dataclass
class DateAxisOptions(PropertyType):
    missing_date_visibility: str | None = None


@dataclass
class DateDimensionField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    date_granularity: str | None = None
    format_configuration: DateTimeFormatConfiguration | None = None
    hierarchy_id: str | None = None


@dataclass
class DateMeasureField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    aggregation_function: str | None = None
    format_configuration: DateTimeFormatConfiguration | None = None


@dataclass
class DateTimeDefaultValues(PropertyType):
    dynamic_value: DynamicDefaultValue | None = None
    rolling_date: RollingDateConfiguration | None = None
    static_values: list[String] = field(default_factory=list)


@dataclass
class DateTimeFormatConfiguration(PropertyType):
    date_time_format: str | None = None
    null_value_format_configuration: NullValueFormatConfiguration | None = None
    numeric_format_configuration: NumericFormatConfiguration | None = None


@dataclass
class DateTimeHierarchy(PropertyType):
    hierarchy_id: str | None = None
    drill_down_filters: list[DrillDownFilter] = field(default_factory=list)


@dataclass
class DateTimeParameter(PropertyType):
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class DateTimeParameterDeclaration(PropertyType):
    name: str | None = None
    default_values: DateTimeDefaultValues | None = None
    mapped_data_set_parameters: list[MappedDataSetParameter] = field(
        default_factory=list
    )
    time_granularity: str | None = None
    value_when_unset: DateTimeValueWhenUnsetConfiguration | None = None


@dataclass
class DateTimePickerControlDisplayOptions(PropertyType):
    date_icon_visibility: str | None = None
    date_time_format: str | None = None
    helper_text_visibility: str | None = None
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class DateTimeValueWhenUnsetConfiguration(PropertyType):
    custom_value: str | None = None
    value_when_unset_option: str | None = None


@dataclass
class DecimalDefaultValues(PropertyType):
    dynamic_value: DynamicDefaultValue | None = None
    static_values: list[Double] = field(default_factory=list)


@dataclass
class DecimalParameter(PropertyType):
    name: str | None = None
    values: list[Double] = field(default_factory=list)


@dataclass
class DecimalParameterDeclaration(PropertyType):
    name: str | None = None
    parameter_value_type: str | None = None
    default_values: DecimalDefaultValues | None = None
    mapped_data_set_parameters: list[MappedDataSetParameter] = field(
        default_factory=list
    )
    value_when_unset: DecimalValueWhenUnsetConfiguration | None = None


@dataclass
class DecimalPlacesConfiguration(PropertyType):
    decimal_places: float | None = None


@dataclass
class DecimalValueWhenUnsetConfiguration(PropertyType):
    custom_value: float | None = None
    value_when_unset_option: str | None = None


@dataclass
class DefaultDateTimePickerControlOptions(PropertyType):
    commit_mode: str | None = None
    display_options: DateTimePickerControlDisplayOptions | None = None
    type_: str | None = None


@dataclass
class DefaultFilterControlConfiguration(PropertyType):
    control_options: DefaultFilterControlOptions | None = None
    title: str | None = None


@dataclass
class DefaultFilterControlOptions(PropertyType):
    default_date_time_picker_options: DefaultDateTimePickerControlOptions | None = None
    default_dropdown_options: DefaultFilterDropDownControlOptions | None = None
    default_list_options: DefaultFilterListControlOptions | None = None
    default_relative_date_time_options: DefaultRelativeDateTimeControlOptions | None = (
        None
    )
    default_slider_options: DefaultSliderControlOptions | None = None
    default_text_area_options: DefaultTextAreaControlOptions | None = None
    default_text_field_options: DefaultTextFieldControlOptions | None = None


@dataclass
class DefaultFilterDropDownControlOptions(PropertyType):
    commit_mode: str | None = None
    display_options: DropDownControlDisplayOptions | None = None
    selectable_values: FilterSelectableValues | None = None
    type_: str | None = None


@dataclass
class DefaultFilterListControlOptions(PropertyType):
    display_options: ListControlDisplayOptions | None = None
    selectable_values: FilterSelectableValues | None = None
    type_: str | None = None


@dataclass
class DefaultFreeFormLayoutConfiguration(PropertyType):
    canvas_size_options: FreeFormLayoutCanvasSizeOptions | None = None


@dataclass
class DefaultGridLayoutConfiguration(PropertyType):
    canvas_size_options: GridLayoutCanvasSizeOptions | None = None


@dataclass
class DefaultInteractiveLayoutConfiguration(PropertyType):
    free_form: DefaultFreeFormLayoutConfiguration | None = None
    grid: DefaultGridLayoutConfiguration | None = None


@dataclass
class DefaultNewSheetConfiguration(PropertyType):
    interactive_layout_configuration: DefaultInteractiveLayoutConfiguration | None = (
        None
    )
    paginated_layout_configuration: DefaultPaginatedLayoutConfiguration | None = None
    sheet_content_type: str | None = None


@dataclass
class DefaultPaginatedLayoutConfiguration(PropertyType):
    section_based: DefaultSectionBasedLayoutConfiguration | None = None


@dataclass
class DefaultRelativeDateTimeControlOptions(PropertyType):
    commit_mode: str | None = None
    display_options: RelativeDateTimeControlDisplayOptions | None = None


@dataclass
class DefaultSectionBasedLayoutConfiguration(PropertyType):
    canvas_size_options: SectionBasedLayoutCanvasSizeOptions | None = None


@dataclass
class DefaultSliderControlOptions(PropertyType):
    maximum_value: float | None = None
    minimum_value: float | None = None
    step_size: float | None = None
    display_options: SliderControlDisplayOptions | None = None
    type_: str | None = None


@dataclass
class DefaultTextAreaControlOptions(PropertyType):
    delimiter: str | None = None
    display_options: TextAreaControlDisplayOptions | None = None


@dataclass
class DefaultTextFieldControlOptions(PropertyType):
    display_options: TextFieldControlDisplayOptions | None = None


@dataclass
class DestinationParameterValueConfiguration(PropertyType):
    custom_values_configuration: CustomValuesConfiguration | None = None
    select_all_value_options: str | None = None
    source_column: ColumnIdentifier | None = None
    source_field: str | None = None
    source_parameter_name: str | None = None


@dataclass
class DimensionField(PropertyType):
    categorical_dimension_field: CategoricalDimensionField | None = None
    date_dimension_field: DateDimensionField | None = None
    numerical_dimension_field: NumericalDimensionField | None = None


@dataclass
class DonutCenterOptions(PropertyType):
    label_visibility: str | None = None


@dataclass
class DonutOptions(PropertyType):
    arc_options: ArcOptions | None = None
    donut_center_options: DonutCenterOptions | None = None


@dataclass
class DrillDownFilter(PropertyType):
    category_filter: CategoryDrillDownFilter | None = None
    numeric_equality_filter: NumericEqualityDrillDownFilter | None = None
    time_range_filter: TimeRangeDrillDownFilter | None = None


@dataclass
class DropDownControlDisplayOptions(PropertyType):
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    select_all_options: ListControlSelectAllOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class DynamicDefaultValue(PropertyType):
    default_value_column: ColumnIdentifier | None = None
    group_name_column: ColumnIdentifier | None = None
    user_name_column: ColumnIdentifier | None = None


@dataclass
class EmptyVisual(PropertyType):
    data_set_identifier: str | None = None
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)


@dataclass
class Entity(PropertyType):
    path: str | None = None


@dataclass
class ExcludePeriodConfiguration(PropertyType):
    amount: float | None = None
    granularity: str | None = None
    status: str | None = None


@dataclass
class ExplicitHierarchy(PropertyType):
    columns: list[ColumnIdentifier] = field(default_factory=list)
    hierarchy_id: str | None = None
    drill_down_filters: list[DrillDownFilter] = field(default_factory=list)


@dataclass
class FieldBasedTooltip(PropertyType):
    aggregation_visibility: str | None = None
    tooltip_fields: list[TooltipItem] = field(default_factory=list)
    tooltip_title_type: str | None = None


@dataclass
class FieldLabelType(PropertyType):
    field_id: str | None = None
    visibility: str | None = None


@dataclass
class FieldSeriesItem(PropertyType):
    axis_binding: str | None = None
    field_id: str | None = None
    settings: LineChartSeriesSettings | None = None


@dataclass
class FieldSort(PropertyType):
    direction: str | None = None
    field_id: str | None = None


@dataclass
class FieldSortOptions(PropertyType):
    column_sort: ColumnSort | None = None
    field_sort: FieldSort | None = None


@dataclass
class FieldTooltipItem(PropertyType):
    field_id: str | None = None
    label: str | None = None
    tooltip_target: str | None = None
    visibility: str | None = None


@dataclass
class FilledMapAggregatedFieldWells(PropertyType):
    geospatial: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class FilledMapConditionalFormatting(PropertyType):
    conditional_formatting_options: list[FilledMapConditionalFormattingOption] = field(
        default_factory=list
    )


@dataclass
class FilledMapConditionalFormattingOption(PropertyType):
    shape: FilledMapShapeConditionalFormatting | None = None


@dataclass
class FilledMapConfiguration(PropertyType):
    field_wells: FilledMapFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    map_style_options: GeospatialMapStyleOptions | None = None
    sort_configuration: FilledMapSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    window_options: GeospatialWindowOptions | None = None


@dataclass
class FilledMapFieldWells(PropertyType):
    filled_map_aggregated_field_wells: FilledMapAggregatedFieldWells | None = None


@dataclass
class FilledMapShapeConditionalFormatting(PropertyType):
    field_id: str | None = None
    format: ShapeConditionalFormat | None = None


@dataclass
class FilledMapSortConfiguration(PropertyType):
    category_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class FilledMapVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: FilledMapConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    conditional_formatting: FilledMapConditionalFormatting | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class Filter(PropertyType):
    category_filter: CategoryFilter | None = None
    nested_filter: NestedFilter | None = None
    numeric_equality_filter: NumericEqualityFilter | None = None
    numeric_range_filter: NumericRangeFilter | None = None
    relative_dates_filter: RelativeDatesFilter | None = None
    time_equality_filter: TimeEqualityFilter | None = None
    time_range_filter: TimeRangeFilter | None = None
    top_bottom_filter: TopBottomFilter | None = None


@dataclass
class FilterControl(PropertyType):
    cross_sheet: FilterCrossSheetControl | None = None
    date_time_picker: FilterDateTimePickerControl | None = None
    dropdown: FilterDropDownControl | None = None
    list: FilterListControl | None = None
    relative_date_time: FilterRelativeDateTimeControl | None = None
    slider: FilterSliderControl | None = None
    text_area: FilterTextAreaControl | None = None
    text_field: FilterTextFieldControl | None = None


@dataclass
class FilterCrossSheetControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    cascading_control_configuration: CascadingControlConfiguration | None = None


@dataclass
class FilterDateTimePickerControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    commit_mode: str | None = None
    display_options: DateTimePickerControlDisplayOptions | None = None
    type_: str | None = None


@dataclass
class FilterDropDownControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    cascading_control_configuration: CascadingControlConfiguration | None = None
    commit_mode: str | None = None
    display_options: DropDownControlDisplayOptions | None = None
    selectable_values: FilterSelectableValues | None = None
    type_: str | None = None


@dataclass
class FilterGroup(PropertyType):
    cross_dataset: str | None = None
    filter_group_id: str | None = None
    filters: list[Filter] = field(default_factory=list)
    scope_configuration: FilterScopeConfiguration | None = None
    status: str | None = None


@dataclass
class FilterListConfiguration(PropertyType):
    match_operator: str | None = None
    category_values: list[String] = field(default_factory=list)
    null_option: str | None = None
    select_all_options: str | None = None


@dataclass
class FilterListControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    cascading_control_configuration: CascadingControlConfiguration | None = None
    display_options: ListControlDisplayOptions | None = None
    selectable_values: FilterSelectableValues | None = None
    type_: str | None = None


@dataclass
class FilterOperationSelectedFieldsConfiguration(PropertyType):
    selected_columns: list[ColumnIdentifier] = field(default_factory=list)
    selected_field_options: str | None = None
    selected_fields: list[String] = field(default_factory=list)


@dataclass
class FilterOperationTargetVisualsConfiguration(PropertyType):
    same_sheet_target_visual_configuration: (
        SameSheetTargetVisualConfiguration | None
    ) = None


@dataclass
class FilterRelativeDateTimeControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    commit_mode: str | None = None
    display_options: RelativeDateTimeControlDisplayOptions | None = None


@dataclass
class FilterScopeConfiguration(PropertyType):
    all_sheets: dict[str, Any] | None = None
    selected_sheets: SelectedSheetsFilterScopeConfiguration | None = None


@dataclass
class FilterSelectableValues(PropertyType):
    values: list[String] = field(default_factory=list)


@dataclass
class FilterSliderControl(PropertyType):
    filter_control_id: str | None = None
    maximum_value: float | None = None
    minimum_value: float | None = None
    source_filter_id: str | None = None
    step_size: float | None = None
    title: str | None = None
    display_options: SliderControlDisplayOptions | None = None
    type_: str | None = None


@dataclass
class FilterTextAreaControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    delimiter: str | None = None
    display_options: TextAreaControlDisplayOptions | None = None


@dataclass
class FilterTextFieldControl(PropertyType):
    filter_control_id: str | None = None
    source_filter_id: str | None = None
    title: str | None = None
    display_options: TextFieldControlDisplayOptions | None = None


@dataclass
class FontConfiguration(PropertyType):
    font_color: str | None = None
    font_decoration: str | None = None
    font_family: str | None = None
    font_size: FontSize | None = None
    font_style: str | None = None
    font_weight: FontWeight | None = None


@dataclass
class FontSize(PropertyType):
    absolute: str | None = None
    relative: str | None = None


@dataclass
class FontWeight(PropertyType):
    name: str | None = None


@dataclass
class ForecastComputation(PropertyType):
    computation_id: str | None = None
    custom_seasonality_value: float | None = None
    lower_boundary: float | None = None
    name: str | None = None
    periods_backward: float | None = None
    periods_forward: float | None = None
    prediction_interval: float | None = None
    seasonality: str | None = None
    time: DimensionField | None = None
    upper_boundary: float | None = None
    value: MeasureField | None = None


@dataclass
class ForecastConfiguration(PropertyType):
    forecast_properties: TimeBasedForecastProperties | None = None
    scenario: ForecastScenario | None = None


@dataclass
class ForecastScenario(PropertyType):
    what_if_point_scenario: WhatIfPointScenario | None = None
    what_if_range_scenario: WhatIfRangeScenario | None = None


@dataclass
class FormatConfiguration(PropertyType):
    date_time_format_configuration: DateTimeFormatConfiguration | None = None
    number_format_configuration: NumberFormatConfiguration | None = None
    string_format_configuration: StringFormatConfiguration | None = None


@dataclass
class FreeFormLayoutCanvasSizeOptions(PropertyType):
    screen_canvas_size_options: FreeFormLayoutScreenCanvasSizeOptions | None = None


@dataclass
class FreeFormLayoutConfiguration(PropertyType):
    elements: list[FreeFormLayoutElement] = field(default_factory=list)
    canvas_size_options: FreeFormLayoutCanvasSizeOptions | None = None


@dataclass
class FreeFormLayoutElement(PropertyType):
    element_id: str | None = None
    element_type: str | None = None
    height: str | None = None
    width: str | None = None
    x_axis_location: str | None = None
    y_axis_location: str | None = None
    background_style: FreeFormLayoutElementBackgroundStyle | None = None
    border_style: FreeFormLayoutElementBorderStyle | None = None
    loading_animation: LoadingAnimation | None = None
    rendering_rules: list[SheetElementRenderingRule] = field(default_factory=list)
    selected_border_style: FreeFormLayoutElementBorderStyle | None = None
    visibility: str | None = None


@dataclass
class FreeFormLayoutElementBackgroundStyle(PropertyType):
    color: str | None = None
    visibility: str | None = None


@dataclass
class FreeFormLayoutElementBorderStyle(PropertyType):
    color: str | None = None
    visibility: str | None = None


@dataclass
class FreeFormLayoutScreenCanvasSizeOptions(PropertyType):
    optimized_view_port_width: str | None = None


@dataclass
class FreeFormSectionLayoutConfiguration(PropertyType):
    elements: list[FreeFormLayoutElement] = field(default_factory=list)


@dataclass
class FunnelChartAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class FunnelChartConfiguration(PropertyType):
    category_label_options: ChartAxisLabelOptions | None = None
    data_label_options: FunnelChartDataLabelOptions | None = None
    field_wells: FunnelChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    sort_configuration: FunnelChartSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    value_label_options: ChartAxisLabelOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class FunnelChartDataLabelOptions(PropertyType):
    category_label_visibility: str | None = None
    label_color: str | None = None
    label_font_configuration: FontConfiguration | None = None
    measure_data_label_style: str | None = None
    measure_label_visibility: str | None = None
    position: str | None = None
    visibility: str | None = None


@dataclass
class FunnelChartFieldWells(PropertyType):
    funnel_chart_aggregated_field_wells: FunnelChartAggregatedFieldWells | None = None


@dataclass
class FunnelChartSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class FunnelChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: FunnelChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class GaugeChartArcConditionalFormatting(PropertyType):
    foreground_color: ConditionalFormattingColor | None = None


@dataclass
class GaugeChartColorConfiguration(PropertyType):
    background_color: str | None = None
    foreground_color: str | None = None


@dataclass
class GaugeChartConditionalFormatting(PropertyType):
    conditional_formatting_options: list[GaugeChartConditionalFormattingOption] = field(
        default_factory=list
    )


@dataclass
class GaugeChartConditionalFormattingOption(PropertyType):
    arc: GaugeChartArcConditionalFormatting | None = None
    primary_value: GaugeChartPrimaryValueConditionalFormatting | None = None


@dataclass
class GaugeChartConfiguration(PropertyType):
    color_configuration: GaugeChartColorConfiguration | None = None
    data_labels: DataLabelOptions | None = None
    field_wells: GaugeChartFieldWells | None = None
    gauge_chart_options: GaugeChartOptions | None = None
    interactions: VisualInteractionOptions | None = None
    tooltip_options: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class GaugeChartFieldWells(PropertyType):
    target_values: list[MeasureField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class GaugeChartOptions(PropertyType):
    arc: ArcConfiguration | None = None
    arc_axis: ArcAxisConfiguration | None = None
    comparison: ComparisonConfiguration | None = None
    primary_value_display_type: str | None = None
    primary_value_font_configuration: FontConfiguration | None = None


@dataclass
class GaugeChartPrimaryValueConditionalFormatting(PropertyType):
    icon: ConditionalFormattingIcon | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class GaugeChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: GaugeChartConfiguration | None = None
    conditional_formatting: GaugeChartConditionalFormatting | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class GeospatialCategoricalColor(PropertyType):
    category_data_colors: list[GeospatialCategoricalDataColor] = field(
        default_factory=list
    )
    default_opacity: float | None = None
    null_data_settings: GeospatialNullDataSettings | None = None
    null_data_visibility: str | None = None


@dataclass
class GeospatialCategoricalDataColor(PropertyType):
    color: str | None = None
    data_value: str | None = None


@dataclass
class GeospatialCircleRadius(PropertyType):
    radius: float | None = None


@dataclass
class GeospatialCircleSymbolStyle(PropertyType):
    circle_radius: GeospatialCircleRadius | None = None
    fill_color: GeospatialColor | None = None
    stroke_color: GeospatialColor | None = None
    stroke_width: GeospatialLineWidth | None = None


@dataclass
class GeospatialColor(PropertyType):
    categorical: GeospatialCategoricalColor | None = None
    gradient: GeospatialGradientColor | None = None
    solid: GeospatialSolidColor | None = None


@dataclass
class GeospatialCoordinateBounds(PropertyType):
    east: float | None = None
    north: float | None = None
    south: float | None = None
    west: float | None = None


@dataclass
class GeospatialDataSourceItem(PropertyType):
    static_file_data_source: GeospatialStaticFileSource | None = None


@dataclass
class GeospatialGradientColor(PropertyType):
    step_colors: list[GeospatialGradientStepColor] = field(default_factory=list)
    default_opacity: float | None = None
    null_data_settings: GeospatialNullDataSettings | None = None
    null_data_visibility: str | None = None


@dataclass
class GeospatialGradientStepColor(PropertyType):
    color: str | None = None
    data_value: float | None = None


@dataclass
class GeospatialHeatmapColorScale(PropertyType):
    colors: list[GeospatialHeatmapDataColor] = field(default_factory=list)


@dataclass
class GeospatialHeatmapConfiguration(PropertyType):
    heatmap_color: GeospatialHeatmapColorScale | None = None


@dataclass
class GeospatialHeatmapDataColor(PropertyType):
    color: str | None = None


@dataclass
class GeospatialLayerColorField(PropertyType):
    color_dimensions_fields: list[DimensionField] = field(default_factory=list)
    color_values_fields: list[MeasureField] = field(default_factory=list)


@dataclass
class GeospatialLayerDefinition(PropertyType):
    line_layer: GeospatialLineLayer | None = None
    point_layer: GeospatialPointLayer | None = None
    polygon_layer: GeospatialPolygonLayer | None = None


@dataclass
class GeospatialLayerItem(PropertyType):
    layer_id: str | None = None
    actions: list[LayerCustomAction] = field(default_factory=list)
    data_source: GeospatialDataSourceItem | None = None
    join_definition: GeospatialLayerJoinDefinition | None = None
    label: str | None = None
    layer_definition: GeospatialLayerDefinition | None = None
    layer_type: str | None = None
    tooltip: TooltipOptions | None = None
    visibility: str | None = None


@dataclass
class GeospatialLayerJoinDefinition(PropertyType):
    color_field: GeospatialLayerColorField | None = None
    dataset_key_field: UnaggregatedField | None = None
    shape_key_field: str | None = None


@dataclass
class GeospatialLayerMapConfiguration(PropertyType):
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    map_layers: list[GeospatialLayerItem] = field(default_factory=list)
    map_state: GeospatialMapState | None = None
    map_style: GeospatialMapStyle | None = None


@dataclass
class GeospatialLineLayer(PropertyType):
    style: GeospatialLineStyle | None = None


@dataclass
class GeospatialLineStyle(PropertyType):
    line_symbol_style: GeospatialLineSymbolStyle | None = None


@dataclass
class GeospatialLineSymbolStyle(PropertyType):
    fill_color: GeospatialColor | None = None
    line_width: GeospatialLineWidth | None = None


@dataclass
class GeospatialLineWidth(PropertyType):
    line_width: float | None = None


@dataclass
class GeospatialMapAggregatedFieldWells(PropertyType):
    colors: list[DimensionField] = field(default_factory=list)
    geospatial: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class GeospatialMapConfiguration(PropertyType):
    field_wells: GeospatialMapFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    map_style_options: GeospatialMapStyleOptions | None = None
    point_style_options: GeospatialPointStyleOptions | None = None
    tooltip: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None
    window_options: GeospatialWindowOptions | None = None


@dataclass
class GeospatialMapFieldWells(PropertyType):
    geospatial_map_aggregated_field_wells: GeospatialMapAggregatedFieldWells | None = (
        None
    )


@dataclass
class GeospatialMapState(PropertyType):
    bounds: GeospatialCoordinateBounds | None = None
    map_navigation: str | None = None


@dataclass
class GeospatialMapStyle(PropertyType):
    background_color: str | None = None
    base_map_style: str | None = None
    base_map_visibility: str | None = None


@dataclass
class GeospatialMapStyleOptions(PropertyType):
    base_map_style: str | None = None


@dataclass
class GeospatialMapVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: GeospatialMapConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class GeospatialNullDataSettings(PropertyType):
    symbol_style: GeospatialNullSymbolStyle | None = None


@dataclass
class GeospatialNullSymbolStyle(PropertyType):
    fill_color: str | None = None
    stroke_color: str | None = None
    stroke_width: float | None = None


@dataclass
class GeospatialPointLayer(PropertyType):
    style: GeospatialPointStyle | None = None


@dataclass
class GeospatialPointStyle(PropertyType):
    circle_symbol_style: GeospatialCircleSymbolStyle | None = None


@dataclass
class GeospatialPointStyleOptions(PropertyType):
    cluster_marker_configuration: ClusterMarkerConfiguration | None = None
    heatmap_configuration: GeospatialHeatmapConfiguration | None = None
    selected_point_style: str | None = None


@dataclass
class GeospatialPolygonLayer(PropertyType):
    style: GeospatialPolygonStyle | None = None


@dataclass
class GeospatialPolygonStyle(PropertyType):
    polygon_symbol_style: GeospatialPolygonSymbolStyle | None = None


@dataclass
class GeospatialPolygonSymbolStyle(PropertyType):
    fill_color: GeospatialColor | None = None
    stroke_color: GeospatialColor | None = None
    stroke_width: GeospatialLineWidth | None = None


@dataclass
class GeospatialSolidColor(PropertyType):
    color: str | None = None
    state: str | None = None


@dataclass
class GeospatialStaticFileSource(PropertyType):
    static_file_id: str | None = None


@dataclass
class GeospatialWindowOptions(PropertyType):
    bounds: GeospatialCoordinateBounds | None = None
    map_zoom_mode: str | None = None


@dataclass
class GlobalTableBorderOptions(PropertyType):
    side_specific_border: TableSideBorderOptions | None = None
    uniform_border: TableBorderOptions | None = None


@dataclass
class GradientColor(PropertyType):
    stops: list[GradientStop] = field(default_factory=list)


@dataclass
class GradientStop(PropertyType):
    gradient_offset: float | None = None
    color: str | None = None
    data_value: float | None = None


@dataclass
class GridLayoutCanvasSizeOptions(PropertyType):
    screen_canvas_size_options: GridLayoutScreenCanvasSizeOptions | None = None


@dataclass
class GridLayoutConfiguration(PropertyType):
    elements: list[GridLayoutElement] = field(default_factory=list)
    canvas_size_options: GridLayoutCanvasSizeOptions | None = None


@dataclass
class GridLayoutElement(PropertyType):
    column_span: float | None = None
    element_id: str | None = None
    element_type: str | None = None
    row_span: float | None = None
    column_index: float | None = None
    row_index: float | None = None


@dataclass
class GridLayoutScreenCanvasSizeOptions(PropertyType):
    resize_option: str | None = None
    optimized_view_port_width: str | None = None


@dataclass
class GrowthRateComputation(PropertyType):
    computation_id: str | None = None
    name: str | None = None
    period_size: float | None = None
    time: DimensionField | None = None
    value: MeasureField | None = None


@dataclass
class HeaderFooterSectionConfiguration(PropertyType):
    layout: SectionLayoutConfiguration | None = None
    section_id: str | None = None
    style: SectionStyle | None = None


@dataclass
class HeatMapAggregatedFieldWells(PropertyType):
    columns: list[DimensionField] = field(default_factory=list)
    rows: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class HeatMapConfiguration(PropertyType):
    color_scale: ColorScale | None = None
    column_label_options: ChartAxisLabelOptions | None = None
    data_labels: DataLabelOptions | None = None
    field_wells: HeatMapFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    row_label_options: ChartAxisLabelOptions | None = None
    sort_configuration: HeatMapSortConfiguration | None = None
    tooltip: TooltipOptions | None = None


@dataclass
class HeatMapFieldWells(PropertyType):
    heat_map_aggregated_field_wells: HeatMapAggregatedFieldWells | None = None


@dataclass
class HeatMapSortConfiguration(PropertyType):
    heat_map_column_items_limit_configuration: ItemsLimitConfiguration | None = None
    heat_map_column_sort: list[FieldSortOptions] = field(default_factory=list)
    heat_map_row_items_limit_configuration: ItemsLimitConfiguration | None = None
    heat_map_row_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class HeatMapVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: HeatMapConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class HistogramAggregatedFieldWells(PropertyType):
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class HistogramBinOptions(PropertyType):
    bin_count: BinCountOptions | None = None
    bin_width: BinWidthOptions | None = None
    selected_bin_type: str | None = None
    start_value: float | None = None


@dataclass
class HistogramConfiguration(PropertyType):
    bin_options: HistogramBinOptions | None = None
    data_labels: DataLabelOptions | None = None
    field_wells: HistogramFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    tooltip: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None
    x_axis_display_options: AxisDisplayOptions | None = None
    x_axis_label_options: ChartAxisLabelOptions | None = None
    y_axis_display_options: AxisDisplayOptions | None = None


@dataclass
class HistogramFieldWells(PropertyType):
    histogram_aggregated_field_wells: HistogramAggregatedFieldWells | None = None


@dataclass
class HistogramVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: HistogramConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class ImageCustomAction(PropertyType):
    action_operations: list[ImageCustomActionOperation] = field(default_factory=list)
    custom_action_id: str | None = None
    name: str | None = None
    trigger: str | None = None
    status: str | None = None


@dataclass
class ImageCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_operation": "URLOperation",
    }

    navigation_operation: CustomActionNavigationOperation | None = None
    set_parameters_operation: CustomActionSetParametersOperation | None = None
    url_operation: CustomActionURLOperation | None = None


@dataclass
class ImageInteractionOptions(PropertyType):
    image_menu_option: ImageMenuOption | None = None


@dataclass
class ImageMenuOption(PropertyType):
    availability_status: str | None = None


@dataclass
class ImageStaticFile(PropertyType):
    static_file_id: str | None = None
    source: StaticFileSource | None = None


@dataclass
class InnerFilter(PropertyType):
    category_inner_filter: CategoryInnerFilter | None = None


@dataclass
class InsightConfiguration(PropertyType):
    computations: list[Computation] = field(default_factory=list)
    custom_narrative: CustomNarrativeOptions | None = None
    interactions: VisualInteractionOptions | None = None


@dataclass
class InsightVisual(PropertyType):
    data_set_identifier: str | None = None
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    insight_configuration: InsightConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class IntegerDefaultValues(PropertyType):
    dynamic_value: DynamicDefaultValue | None = None
    static_values: list[Double] = field(default_factory=list)


@dataclass
class IntegerParameter(PropertyType):
    name: str | None = None
    values: list[Double] = field(default_factory=list)


@dataclass
class IntegerParameterDeclaration(PropertyType):
    name: str | None = None
    parameter_value_type: str | None = None
    default_values: IntegerDefaultValues | None = None
    mapped_data_set_parameters: list[MappedDataSetParameter] = field(
        default_factory=list
    )
    value_when_unset: IntegerValueWhenUnsetConfiguration | None = None


@dataclass
class IntegerValueWhenUnsetConfiguration(PropertyType):
    custom_value: float | None = None
    value_when_unset_option: str | None = None


@dataclass
class ItemsLimitConfiguration(PropertyType):
    items_limit: float | None = None
    other_categories: str | None = None


@dataclass
class KPIActualValueConditionalFormatting(PropertyType):
    icon: ConditionalFormattingIcon | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class KPIComparisonValueConditionalFormatting(PropertyType):
    icon: ConditionalFormattingIcon | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class KPIConditionalFormatting(PropertyType):
    conditional_formatting_options: list[KPIConditionalFormattingOption] = field(
        default_factory=list
    )


@dataclass
class KPIConditionalFormattingOption(PropertyType):
    actual_value: KPIActualValueConditionalFormatting | None = None
    comparison_value: KPIComparisonValueConditionalFormatting | None = None
    primary_value: KPIPrimaryValueConditionalFormatting | None = None
    progress_bar: KPIProgressBarConditionalFormatting | None = None


@dataclass
class KPIConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kpi_options": "KPIOptions",
    }

    field_wells: KPIFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    kpi_options: KPIOptions | None = None
    sort_configuration: KPISortConfiguration | None = None


@dataclass
class KPIFieldWells(PropertyType):
    target_values: list[MeasureField] = field(default_factory=list)
    trend_groups: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class KPIOptions(PropertyType):
    comparison: ComparisonConfiguration | None = None
    primary_value_display_type: str | None = None
    primary_value_font_configuration: FontConfiguration | None = None
    progress_bar: ProgressBarOptions | None = None
    secondary_value: SecondaryValueOptions | None = None
    secondary_value_font_configuration: FontConfiguration | None = None
    sparkline: KPISparklineOptions | None = None
    trend_arrows: TrendArrowOptions | None = None
    visual_layout_options: KPIVisualLayoutOptions | None = None


@dataclass
class KPIPrimaryValueConditionalFormatting(PropertyType):
    icon: ConditionalFormattingIcon | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class KPIProgressBarConditionalFormatting(PropertyType):
    foreground_color: ConditionalFormattingColor | None = None


@dataclass
class KPISortConfiguration(PropertyType):
    trend_group_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class KPISparklineOptions(PropertyType):
    type_: str | None = None
    color: str | None = None
    tooltip_visibility: str | None = None
    visibility: str | None = None


@dataclass
class KPIVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: KPIConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    conditional_formatting: KPIConditionalFormatting | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class KPIVisualLayoutOptions(PropertyType):
    standard_layout: KPIVisualStandardLayout | None = None


@dataclass
class KPIVisualStandardLayout(PropertyType):
    type_: str | None = None


@dataclass
class LabelOptions(PropertyType):
    custom_label: str | None = None
    font_configuration: FontConfiguration | None = None
    visibility: str | None = None


@dataclass
class LayerCustomAction(PropertyType):
    action_operations: list[LayerCustomActionOperation] = field(default_factory=list)
    custom_action_id: str | None = None
    name: str | None = None
    trigger: str | None = None
    status: str | None = None


@dataclass
class LayerCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_operation": "URLOperation",
    }

    filter_operation: CustomActionFilterOperation | None = None
    navigation_operation: CustomActionNavigationOperation | None = None
    set_parameters_operation: CustomActionSetParametersOperation | None = None
    url_operation: CustomActionURLOperation | None = None


@dataclass
class LayerMapVisual(PropertyType):
    data_set_identifier: str | None = None
    visual_id: str | None = None
    chart_configuration: GeospatialLayerMapConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class Layout(PropertyType):
    configuration: LayoutConfiguration | None = None


@dataclass
class LayoutConfiguration(PropertyType):
    free_form_layout: FreeFormLayoutConfiguration | None = None
    grid_layout: GridLayoutConfiguration | None = None
    section_based_layout: SectionBasedLayoutConfiguration | None = None


@dataclass
class LegendOptions(PropertyType):
    height: str | None = None
    position: str | None = None
    title: LabelOptions | None = None
    value_font_configuration: FontConfiguration | None = None
    visibility: str | None = None
    width: str | None = None


@dataclass
class LineChartAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    colors: list[DimensionField] = field(default_factory=list)
    small_multiples: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class LineChartConfiguration(PropertyType):
    contribution_analysis_defaults: list[ContributionAnalysisDefault] = field(
        default_factory=list
    )
    data_labels: DataLabelOptions | None = None
    default_series_settings: LineChartDefaultSeriesSettings | None = None
    field_wells: LineChartFieldWells | None = None
    forecast_configurations: list[ForecastConfiguration] = field(default_factory=list)
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    primary_y_axis_display_options: LineSeriesAxisDisplayOptions | None = None
    primary_y_axis_label_options: ChartAxisLabelOptions | None = None
    reference_lines: list[ReferenceLine] = field(default_factory=list)
    secondary_y_axis_display_options: LineSeriesAxisDisplayOptions | None = None
    secondary_y_axis_label_options: ChartAxisLabelOptions | None = None
    series: list[SeriesItem] = field(default_factory=list)
    single_axis_options: SingleAxisOptions | None = None
    small_multiples_options: SmallMultiplesOptions | None = None
    sort_configuration: LineChartSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    type_: str | None = None
    visual_palette: VisualPalette | None = None
    x_axis_display_options: AxisDisplayOptions | None = None
    x_axis_label_options: ChartAxisLabelOptions | None = None


@dataclass
class LineChartDefaultSeriesSettings(PropertyType):
    axis_binding: str | None = None
    line_style_settings: LineChartLineStyleSettings | None = None
    marker_style_settings: LineChartMarkerStyleSettings | None = None


@dataclass
class LineChartFieldWells(PropertyType):
    line_chart_aggregated_field_wells: LineChartAggregatedFieldWells | None = None


@dataclass
class LineChartLineStyleSettings(PropertyType):
    line_interpolation: str | None = None
    line_style: str | None = None
    line_visibility: str | None = None
    line_width: str | None = None


@dataclass
class LineChartMarkerStyleSettings(PropertyType):
    marker_color: str | None = None
    marker_shape: str | None = None
    marker_size: str | None = None
    marker_visibility: str | None = None


@dataclass
class LineChartSeriesSettings(PropertyType):
    line_style_settings: LineChartLineStyleSettings | None = None
    marker_style_settings: LineChartMarkerStyleSettings | None = None


@dataclass
class LineChartSortConfiguration(PropertyType):
    category_items_limit_configuration: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    color_items_limit_configuration: ItemsLimitConfiguration | None = None
    small_multiples_limit_configuration: ItemsLimitConfiguration | None = None
    small_multiples_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class LineChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: LineChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class LineSeriesAxisDisplayOptions(PropertyType):
    axis_options: AxisDisplayOptions | None = None
    missing_data_configurations: list[MissingDataConfiguration] = field(
        default_factory=list
    )


@dataclass
class ListControlDisplayOptions(PropertyType):
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    search_options: ListControlSearchOptions | None = None
    select_all_options: ListControlSelectAllOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class ListControlSearchOptions(PropertyType):
    visibility: str | None = None


@dataclass
class ListControlSelectAllOptions(PropertyType):
    visibility: str | None = None


@dataclass
class LoadingAnimation(PropertyType):
    visibility: str | None = None


@dataclass
class LocalNavigationConfiguration(PropertyType):
    target_sheet_id: str | None = None


@dataclass
class LongFormatText(PropertyType):
    plain_text: str | None = None
    rich_text: str | None = None


@dataclass
class MappedDataSetParameter(PropertyType):
    data_set_identifier: str | None = None
    data_set_parameter_name: str | None = None


@dataclass
class MaximumLabelType(PropertyType):
    visibility: str | None = None


@dataclass
class MaximumMinimumComputation(PropertyType):
    computation_id: str | None = None
    type_: str | None = None
    name: str | None = None
    time: DimensionField | None = None
    value: MeasureField | None = None


@dataclass
class MeasureField(PropertyType):
    calculated_measure_field: CalculatedMeasureField | None = None
    categorical_measure_field: CategoricalMeasureField | None = None
    date_measure_field: DateMeasureField | None = None
    numerical_measure_field: NumericalMeasureField | None = None


@dataclass
class MetricComparisonComputation(PropertyType):
    computation_id: str | None = None
    from_value: MeasureField | None = None
    name: str | None = None
    target_value: MeasureField | None = None
    time: DimensionField | None = None


@dataclass
class MinimumLabelType(PropertyType):
    visibility: str | None = None


@dataclass
class MissingDataConfiguration(PropertyType):
    treatment_option: str | None = None


@dataclass
class NegativeValueConfiguration(PropertyType):
    display_mode: str | None = None


@dataclass
class NestedFilter(PropertyType):
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    include_inner_set: bool | None = None
    inner_filter: InnerFilter | None = None


@dataclass
class NullValueFormatConfiguration(PropertyType):
    null_string: str | None = None


@dataclass
class NumberDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DecimalPlacesConfiguration | None = None
    negative_value_configuration: NegativeValueConfiguration | None = None
    null_value_format_configuration: NullValueFormatConfiguration | None = None
    number_scale: str | None = None
    prefix: str | None = None
    separator_configuration: NumericSeparatorConfiguration | None = None
    suffix: str | None = None


@dataclass
class NumberFormatConfiguration(PropertyType):
    format_configuration: NumericFormatConfiguration | None = None


@dataclass
class NumericAxisOptions(PropertyType):
    range: AxisDisplayRange | None = None
    scale: AxisScale | None = None


@dataclass
class NumericEqualityDrillDownFilter(PropertyType):
    column: ColumnIdentifier | None = None
    value: float | None = None


@dataclass
class NumericEqualityFilter(PropertyType):
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    match_operator: str | None = None
    null_option: str | None = None
    aggregation_function: AggregationFunction | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    parameter_name: str | None = None
    select_all_options: str | None = None
    value: float | None = None


@dataclass
class NumericFormatConfiguration(PropertyType):
    currency_display_format_configuration: CurrencyDisplayFormatConfiguration | None = (
        None
    )
    number_display_format_configuration: NumberDisplayFormatConfiguration | None = None
    percentage_display_format_configuration: (
        PercentageDisplayFormatConfiguration | None
    ) = None


@dataclass
class NumericRangeFilter(PropertyType):
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    null_option: str | None = None
    aggregation_function: AggregationFunction | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    include_maximum: bool | None = None
    include_minimum: bool | None = None
    range_maximum: NumericRangeFilterValue | None = None
    range_minimum: NumericRangeFilterValue | None = None
    select_all_options: str | None = None


@dataclass
class NumericRangeFilterValue(PropertyType):
    parameter: str | None = None
    static_value: float | None = None


@dataclass
class NumericSeparatorConfiguration(PropertyType):
    decimal_separator: str | None = None
    thousands_separator: ThousandSeparatorOptions | None = None


@dataclass
class NumericalAggregationFunction(PropertyType):
    percentile_aggregation: PercentileAggregation | None = None
    simple_numerical_aggregation: str | None = None


@dataclass
class NumericalDimensionField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    format_configuration: NumberFormatConfiguration | None = None
    hierarchy_id: str | None = None


@dataclass
class NumericalMeasureField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    aggregation_function: NumericalAggregationFunction | None = None
    format_configuration: NumberFormatConfiguration | None = None


@dataclass
class PaginationConfiguration(PropertyType):
    page_number: float | None = None
    page_size: float | None = None


@dataclass
class PanelConfiguration(PropertyType):
    background_color: str | None = None
    background_visibility: str | None = None
    border_color: str | None = None
    border_style: str | None = None
    border_thickness: str | None = None
    border_visibility: str | None = None
    gutter_spacing: str | None = None
    gutter_visibility: str | None = None
    title: PanelTitleOptions | None = None


@dataclass
class PanelTitleOptions(PropertyType):
    font_configuration: FontConfiguration | None = None
    horizontal_text_alignment: str | None = None
    visibility: str | None = None


@dataclass
class ParameterControl(PropertyType):
    date_time_picker: ParameterDateTimePickerControl | None = None
    dropdown: ParameterDropDownControl | None = None
    list: ParameterListControl | None = None
    slider: ParameterSliderControl | None = None
    text_area: ParameterTextAreaControl | None = None
    text_field: ParameterTextFieldControl | None = None


@dataclass
class ParameterDateTimePickerControl(PropertyType):
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    title: str | None = None
    display_options: DateTimePickerControlDisplayOptions | None = None


@dataclass
class ParameterDeclaration(PropertyType):
    date_time_parameter_declaration: DateTimeParameterDeclaration | None = None
    decimal_parameter_declaration: DecimalParameterDeclaration | None = None
    integer_parameter_declaration: IntegerParameterDeclaration | None = None
    string_parameter_declaration: StringParameterDeclaration | None = None


@dataclass
class ParameterDropDownControl(PropertyType):
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    title: str | None = None
    cascading_control_configuration: CascadingControlConfiguration | None = None
    commit_mode: str | None = None
    display_options: DropDownControlDisplayOptions | None = None
    selectable_values: ParameterSelectableValues | None = None
    type_: str | None = None


@dataclass
class ParameterListControl(PropertyType):
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    title: str | None = None
    cascading_control_configuration: CascadingControlConfiguration | None = None
    display_options: ListControlDisplayOptions | None = None
    selectable_values: ParameterSelectableValues | None = None
    type_: str | None = None


@dataclass
class ParameterSelectableValues(PropertyType):
    link_to_data_set_column: ColumnIdentifier | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class ParameterSliderControl(PropertyType):
    maximum_value: float | None = None
    minimum_value: float | None = None
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    step_size: float | None = None
    title: str | None = None
    display_options: SliderControlDisplayOptions | None = None


@dataclass
class ParameterTextAreaControl(PropertyType):
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    title: str | None = None
    delimiter: str | None = None
    display_options: TextAreaControlDisplayOptions | None = None


@dataclass
class ParameterTextFieldControl(PropertyType):
    parameter_control_id: str | None = None
    source_parameter_name: str | None = None
    title: str | None = None
    display_options: TextFieldControlDisplayOptions | None = None


@dataclass
class Parameters(PropertyType):
    date_time_parameters: list[DateTimeParameter] = field(default_factory=list)
    decimal_parameters: list[DecimalParameter] = field(default_factory=list)
    integer_parameters: list[IntegerParameter] = field(default_factory=list)
    string_parameters: list[StringParameter] = field(default_factory=list)


@dataclass
class PercentVisibleRange(PropertyType):
    from_: float | None = None
    to: float | None = None


@dataclass
class PercentageDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DecimalPlacesConfiguration | None = None
    negative_value_configuration: NegativeValueConfiguration | None = None
    null_value_format_configuration: NullValueFormatConfiguration | None = None
    prefix: str | None = None
    separator_configuration: NumericSeparatorConfiguration | None = None
    suffix: str | None = None


@dataclass
class PercentileAggregation(PropertyType):
    percentile_value: float | None = None


@dataclass
class PeriodOverPeriodComputation(PropertyType):
    computation_id: str | None = None
    name: str | None = None
    time: DimensionField | None = None
    value: MeasureField | None = None


@dataclass
class PeriodToDateComputation(PropertyType):
    computation_id: str | None = None
    name: str | None = None
    period_time_granularity: str | None = None
    time: DimensionField | None = None
    value: MeasureField | None = None


@dataclass
class PieChartAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    small_multiples: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class PieChartConfiguration(PropertyType):
    category_label_options: ChartAxisLabelOptions | None = None
    contribution_analysis_defaults: list[ContributionAnalysisDefault] = field(
        default_factory=list
    )
    data_labels: DataLabelOptions | None = None
    donut_options: DonutOptions | None = None
    field_wells: PieChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    small_multiples_options: SmallMultiplesOptions | None = None
    sort_configuration: PieChartSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    value_label_options: ChartAxisLabelOptions | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class PieChartFieldWells(PropertyType):
    pie_chart_aggregated_field_wells: PieChartAggregatedFieldWells | None = None


@dataclass
class PieChartSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    small_multiples_limit_configuration: ItemsLimitConfiguration | None = None
    small_multiples_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class PieChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: PieChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class PivotFieldSortOptions(PropertyType):
    field_id: str | None = None
    sort_by: PivotTableSortBy | None = None


@dataclass
class PivotTableAggregatedFieldWells(PropertyType):
    columns: list[DimensionField] = field(default_factory=list)
    rows: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class PivotTableCellConditionalFormatting(PropertyType):
    field_id: str | None = None
    scope: PivotTableConditionalFormattingScope | None = None
    scopes: list[PivotTableConditionalFormattingScope] = field(default_factory=list)
    text_format: TextConditionalFormat | None = None


@dataclass
class PivotTableConditionalFormatting(PropertyType):
    conditional_formatting_options: list[PivotTableConditionalFormattingOption] = field(
        default_factory=list
    )


@dataclass
class PivotTableConditionalFormattingOption(PropertyType):
    cell: PivotTableCellConditionalFormatting | None = None


@dataclass
class PivotTableConditionalFormattingScope(PropertyType):
    role: str | None = None


@dataclass
class PivotTableConfiguration(PropertyType):
    field_options: PivotTableFieldOptions | None = None
    field_wells: PivotTableFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    paginated_report_options: PivotTablePaginatedReportOptions | None = None
    sort_configuration: PivotTableSortConfiguration | None = None
    table_options: PivotTableOptions | None = None
    total_options: PivotTableTotalOptions | None = None


@dataclass
class PivotTableDataPathOption(PropertyType):
    data_path_list: list[DataPathValue] = field(default_factory=list)
    width: str | None = None


@dataclass
class PivotTableFieldCollapseStateOption(PropertyType):
    target: PivotTableFieldCollapseStateTarget | None = None
    state: str | None = None


@dataclass
class PivotTableFieldCollapseStateTarget(PropertyType):
    field_data_path_values: list[DataPathValue] = field(default_factory=list)
    field_id: str | None = None


@dataclass
class PivotTableFieldOption(PropertyType):
    field_id: str | None = None
    custom_label: str | None = None
    visibility: str | None = None


@dataclass
class PivotTableFieldOptions(PropertyType):
    collapse_state_options: list[PivotTableFieldCollapseStateOption] = field(
        default_factory=list
    )
    data_path_options: list[PivotTableDataPathOption] = field(default_factory=list)
    selected_field_options: list[PivotTableFieldOption] = field(default_factory=list)


@dataclass
class PivotTableFieldSubtotalOptions(PropertyType):
    field_id: str | None = None


@dataclass
class PivotTableFieldWells(PropertyType):
    pivot_table_aggregated_field_wells: PivotTableAggregatedFieldWells | None = None


@dataclass
class PivotTableOptions(PropertyType):
    cell_style: TableCellStyle | None = None
    collapsed_row_dimensions_visibility: str | None = None
    column_header_style: TableCellStyle | None = None
    column_names_visibility: str | None = None
    default_cell_width: str | None = None
    metric_placement: str | None = None
    row_alternate_color_options: RowAlternateColorOptions | None = None
    row_field_names_style: TableCellStyle | None = None
    row_header_style: TableCellStyle | None = None
    rows_label_options: PivotTableRowsLabelOptions | None = None
    rows_layout: str | None = None
    single_metric_visibility: str | None = None
    toggle_buttons_visibility: str | None = None


@dataclass
class PivotTablePaginatedReportOptions(PropertyType):
    overflow_column_header_visibility: str | None = None
    vertical_overflow_visibility: str | None = None


@dataclass
class PivotTableRowsLabelOptions(PropertyType):
    custom_label: str | None = None
    visibility: str | None = None


@dataclass
class PivotTableSortBy(PropertyType):
    column: ColumnSort | None = None
    data_path: DataPathSort | None = None
    field_: FieldSort | None = None


@dataclass
class PivotTableSortConfiguration(PropertyType):
    field_sort_options: list[PivotFieldSortOptions] = field(default_factory=list)


@dataclass
class PivotTableTotalOptions(PropertyType):
    column_subtotal_options: SubtotalOptions | None = None
    column_total_options: PivotTotalOptions | None = None
    row_subtotal_options: SubtotalOptions | None = None
    row_total_options: PivotTotalOptions | None = None


@dataclass
class PivotTableVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: PivotTableConfiguration | None = None
    conditional_formatting: PivotTableConditionalFormatting | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class PivotTotalOptions(PropertyType):
    custom_label: str | None = None
    metric_header_cell_style: TableCellStyle | None = None
    placement: str | None = None
    scroll_status: str | None = None
    total_aggregation_options: list[TotalAggregationOption] = field(
        default_factory=list
    )
    total_cell_style: TableCellStyle | None = None
    totals_visibility: str | None = None
    value_cell_style: TableCellStyle | None = None


@dataclass
class PluginVisual(PropertyType):
    plugin_arn: str | None = None
    visual_id: str | None = None
    chart_configuration: PluginVisualConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class PluginVisualConfiguration(PropertyType):
    field_wells: list[PluginVisualFieldWell] = field(default_factory=list)
    sort_configuration: PluginVisualSortConfiguration | None = None
    visual_options: PluginVisualOptions | None = None


@dataclass
class PluginVisualFieldWell(PropertyType):
    axis_name: str | None = None
    dimensions: list[DimensionField] = field(default_factory=list)
    measures: list[MeasureField] = field(default_factory=list)
    unaggregated: list[UnaggregatedField] = field(default_factory=list)


@dataclass
class PluginVisualItemsLimitConfiguration(PropertyType):
    items_limit: float | None = None


@dataclass
class PluginVisualOptions(PropertyType):
    visual_properties: list[PluginVisualProperty] = field(default_factory=list)


@dataclass
class PluginVisualProperty(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class PluginVisualSortConfiguration(PropertyType):
    plugin_visual_table_query_sort: PluginVisualTableQuerySort | None = None


@dataclass
class PluginVisualTableQuerySort(PropertyType):
    items_limit_configuration: PluginVisualItemsLimitConfiguration | None = None
    row_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class PredefinedHierarchy(PropertyType):
    columns: list[ColumnIdentifier] = field(default_factory=list)
    hierarchy_id: str | None = None
    drill_down_filters: list[DrillDownFilter] = field(default_factory=list)


@dataclass
class ProgressBarOptions(PropertyType):
    visibility: str | None = None


@dataclass
class QueryExecutionOptions(PropertyType):
    query_execution_mode: str | None = None


@dataclass
class RadarChartAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    color: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class RadarChartAreaStyleSettings(PropertyType):
    visibility: str | None = None


@dataclass
class RadarChartConfiguration(PropertyType):
    alternate_band_colors_visibility: str | None = None
    alternate_band_even_color: str | None = None
    alternate_band_odd_color: str | None = None
    axes_range_scale: str | None = None
    base_series_settings: RadarChartSeriesSettings | None = None
    category_axis: AxisDisplayOptions | None = None
    category_label_options: ChartAxisLabelOptions | None = None
    color_axis: AxisDisplayOptions | None = None
    color_label_options: ChartAxisLabelOptions | None = None
    field_wells: RadarChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    shape: str | None = None
    sort_configuration: RadarChartSortConfiguration | None = None
    start_angle: float | None = None
    visual_palette: VisualPalette | None = None


@dataclass
class RadarChartFieldWells(PropertyType):
    radar_chart_aggregated_field_wells: RadarChartAggregatedFieldWells | None = None


@dataclass
class RadarChartSeriesSettings(PropertyType):
    area_style_settings: RadarChartAreaStyleSettings | None = None


@dataclass
class RadarChartSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)
    color_items_limit: ItemsLimitConfiguration | None = None
    color_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class RadarChartVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: RadarChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class RangeEndsLabelType(PropertyType):
    visibility: str | None = None


@dataclass
class ReferenceLine(PropertyType):
    data_configuration: ReferenceLineDataConfiguration | None = None
    label_configuration: ReferenceLineLabelConfiguration | None = None
    status: str | None = None
    style_configuration: ReferenceLineStyleConfiguration | None = None


@dataclass
class ReferenceLineCustomLabelConfiguration(PropertyType):
    custom_label: str | None = None


@dataclass
class ReferenceLineDataConfiguration(PropertyType):
    axis_binding: str | None = None
    dynamic_configuration: ReferenceLineDynamicDataConfiguration | None = None
    series_type: str | None = None
    static_configuration: ReferenceLineStaticDataConfiguration | None = None


@dataclass
class ReferenceLineDynamicDataConfiguration(PropertyType):
    calculation: NumericalAggregationFunction | None = None
    column: ColumnIdentifier | None = None
    measure_aggregation_function: AggregationFunction | None = None


@dataclass
class ReferenceLineLabelConfiguration(PropertyType):
    custom_label_configuration: ReferenceLineCustomLabelConfiguration | None = None
    font_color: str | None = None
    font_configuration: FontConfiguration | None = None
    horizontal_position: str | None = None
    value_label_configuration: ReferenceLineValueLabelConfiguration | None = None
    vertical_position: str | None = None


@dataclass
class ReferenceLineStaticDataConfiguration(PropertyType):
    value: float | None = None


@dataclass
class ReferenceLineStyleConfiguration(PropertyType):
    color: str | None = None
    pattern: str | None = None


@dataclass
class ReferenceLineValueLabelConfiguration(PropertyType):
    format_configuration: NumericFormatConfiguration | None = None
    relative_position: str | None = None


@dataclass
class RelativeDateTimeControlDisplayOptions(PropertyType):
    date_time_format: str | None = None
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class RelativeDatesFilter(PropertyType):
    anchor_date_configuration: AnchorDateConfiguration | None = None
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    null_option: str | None = None
    relative_date_type: str | None = None
    time_granularity: str | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    exclude_period_configuration: ExcludePeriodConfiguration | None = None
    minimum_granularity: str | None = None
    parameter_name: str | None = None
    relative_date_value: float | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[String] = field(default_factory=list)
    principal: str | None = None


@dataclass
class RollingDateConfiguration(PropertyType):
    expression: str | None = None
    data_set_identifier: str | None = None


@dataclass
class RowAlternateColorOptions(PropertyType):
    row_alternate_colors: list[String] = field(default_factory=list)
    status: str | None = None
    use_primary_background_color: str | None = None


@dataclass
class SameSheetTargetVisualConfiguration(PropertyType):
    target_visual_options: str | None = None
    target_visuals: list[String] = field(default_factory=list)


@dataclass
class SankeyDiagramAggregatedFieldWells(PropertyType):
    destination: list[DimensionField] = field(default_factory=list)
    source: list[DimensionField] = field(default_factory=list)
    weight: list[MeasureField] = field(default_factory=list)


@dataclass
class SankeyDiagramChartConfiguration(PropertyType):
    data_labels: DataLabelOptions | None = None
    field_wells: SankeyDiagramFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    sort_configuration: SankeyDiagramSortConfiguration | None = None


@dataclass
class SankeyDiagramFieldWells(PropertyType):
    sankey_diagram_aggregated_field_wells: SankeyDiagramAggregatedFieldWells | None = (
        None
    )


@dataclass
class SankeyDiagramSortConfiguration(PropertyType):
    destination_items_limit: ItemsLimitConfiguration | None = None
    source_items_limit: ItemsLimitConfiguration | None = None
    weight_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class SankeyDiagramVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: SankeyDiagramChartConfiguration | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class ScatterPlotCategoricallyAggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    label: list[DimensionField] = field(default_factory=list)
    size: list[MeasureField] = field(default_factory=list)
    x_axis: list[MeasureField] = field(default_factory=list)
    y_axis: list[MeasureField] = field(default_factory=list)


@dataclass
class ScatterPlotConfiguration(PropertyType):
    data_labels: DataLabelOptions | None = None
    field_wells: ScatterPlotFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    sort_configuration: ScatterPlotSortConfiguration | None = None
    tooltip: TooltipOptions | None = None
    visual_palette: VisualPalette | None = None
    x_axis_display_options: AxisDisplayOptions | None = None
    x_axis_label_options: ChartAxisLabelOptions | None = None
    y_axis_display_options: AxisDisplayOptions | None = None
    y_axis_label_options: ChartAxisLabelOptions | None = None


@dataclass
class ScatterPlotFieldWells(PropertyType):
    scatter_plot_categorically_aggregated_field_wells: (
        ScatterPlotCategoricallyAggregatedFieldWells | None
    ) = None
    scatter_plot_unaggregated_field_wells: ScatterPlotUnaggregatedFieldWells | None = (
        None
    )


@dataclass
class ScatterPlotSortConfiguration(PropertyType):
    scatter_plot_limit_configuration: ItemsLimitConfiguration | None = None


@dataclass
class ScatterPlotUnaggregatedFieldWells(PropertyType):
    category: list[DimensionField] = field(default_factory=list)
    label: list[DimensionField] = field(default_factory=list)
    size: list[MeasureField] = field(default_factory=list)
    x_axis: list[DimensionField] = field(default_factory=list)
    y_axis: list[DimensionField] = field(default_factory=list)


@dataclass
class ScatterPlotVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: ScatterPlotConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class ScrollBarOptions(PropertyType):
    visibility: str | None = None
    visible_range: VisibleRangeOptions | None = None


@dataclass
class SecondaryValueOptions(PropertyType):
    visibility: str | None = None


@dataclass
class SectionAfterPageBreak(PropertyType):
    status: str | None = None


@dataclass
class SectionBasedLayoutCanvasSizeOptions(PropertyType):
    paper_canvas_size_options: SectionBasedLayoutPaperCanvasSizeOptions | None = None


@dataclass
class SectionBasedLayoutConfiguration(PropertyType):
    body_sections: list[BodySectionConfiguration] = field(default_factory=list)
    canvas_size_options: SectionBasedLayoutCanvasSizeOptions | None = None
    footer_sections: list[HeaderFooterSectionConfiguration] = field(
        default_factory=list
    )
    header_sections: list[HeaderFooterSectionConfiguration] = field(
        default_factory=list
    )


@dataclass
class SectionBasedLayoutPaperCanvasSizeOptions(PropertyType):
    paper_margin: Spacing | None = None
    paper_orientation: str | None = None
    paper_size: str | None = None


@dataclass
class SectionLayoutConfiguration(PropertyType):
    free_form_layout: FreeFormSectionLayoutConfiguration | None = None


@dataclass
class SectionPageBreakConfiguration(PropertyType):
    after: SectionAfterPageBreak | None = None


@dataclass
class SectionStyle(PropertyType):
    height: str | None = None
    padding: Spacing | None = None


@dataclass
class SelectedSheetsFilterScopeConfiguration(PropertyType):
    sheet_visual_scoping_configurations: list[SheetVisualScopingConfiguration] = field(
        default_factory=list
    )


@dataclass
class SeriesItem(PropertyType):
    data_field_series_item: DataFieldSeriesItem | None = None
    field_series_item: FieldSeriesItem | None = None


@dataclass
class SetParameterValueConfiguration(PropertyType):
    destination_parameter_name: str | None = None
    value: DestinationParameterValueConfiguration | None = None


@dataclass
class ShapeConditionalFormat(PropertyType):
    background_color: ConditionalFormattingColor | None = None


@dataclass
class Sheet(PropertyType):
    name: str | None = None
    sheet_id: str | None = None


@dataclass
class SheetControlInfoIconLabelOptions(PropertyType):
    info_icon_text: str | None = None
    visibility: str | None = None


@dataclass
class SheetControlLayout(PropertyType):
    configuration: SheetControlLayoutConfiguration | None = None


@dataclass
class SheetControlLayoutConfiguration(PropertyType):
    grid_layout: GridLayoutConfiguration | None = None


@dataclass
class SheetDefinition(PropertyType):
    sheet_id: str | None = None
    content_type: str | None = None
    description: str | None = None
    filter_controls: list[FilterControl] = field(default_factory=list)
    images: list[SheetImage] = field(default_factory=list)
    layouts: list[Layout] = field(default_factory=list)
    name: str | None = None
    parameter_controls: list[ParameterControl] = field(default_factory=list)
    sheet_control_layouts: list[SheetControlLayout] = field(default_factory=list)
    text_boxes: list[SheetTextBox] = field(default_factory=list)
    title: str | None = None
    visuals: list[Visual] = field(default_factory=list)


@dataclass
class SheetElementConfigurationOverrides(PropertyType):
    visibility: str | None = None


@dataclass
class SheetElementRenderingRule(PropertyType):
    configuration_overrides: SheetElementConfigurationOverrides | None = None
    expression: str | None = None


@dataclass
class SheetImage(PropertyType):
    sheet_image_id: str | None = None
    source: SheetImageSource | None = None
    actions: list[ImageCustomAction] = field(default_factory=list)
    image_content_alt_text: str | None = None
    interactions: ImageInteractionOptions | None = None
    scaling: SheetImageScalingConfiguration | None = None
    tooltip: SheetImageTooltipConfiguration | None = None


@dataclass
class SheetImageScalingConfiguration(PropertyType):
    scaling_type: str | None = None


@dataclass
class SheetImageSource(PropertyType):
    sheet_image_static_file_source: SheetImageStaticFileSource | None = None


@dataclass
class SheetImageStaticFileSource(PropertyType):
    static_file_id: str | None = None


@dataclass
class SheetImageTooltipConfiguration(PropertyType):
    tooltip_text: SheetImageTooltipText | None = None
    visibility: str | None = None


@dataclass
class SheetImageTooltipText(PropertyType):
    plain_text: str | None = None


@dataclass
class SheetTextBox(PropertyType):
    sheet_text_box_id: str | None = None
    content: str | None = None


@dataclass
class SheetVisualScopingConfiguration(PropertyType):
    scope: str | None = None
    sheet_id: str | None = None
    visual_ids: list[String] = field(default_factory=list)


@dataclass
class ShortFormatText(PropertyType):
    plain_text: str | None = None
    rich_text: str | None = None


@dataclass
class SimpleClusterMarker(PropertyType):
    color: str | None = None


@dataclass
class SingleAxisOptions(PropertyType):
    y_axis_options: YAxisOptions | None = None


@dataclass
class SliderControlDisplayOptions(PropertyType):
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class SmallMultiplesAxisProperties(PropertyType):
    placement: str | None = None
    scale: str | None = None


@dataclass
class SmallMultiplesOptions(PropertyType):
    max_visible_columns: float | None = None
    max_visible_rows: float | None = None
    panel_configuration: PanelConfiguration | None = None
    x_axis: SmallMultiplesAxisProperties | None = None
    y_axis: SmallMultiplesAxisProperties | None = None


@dataclass
class Spacing(PropertyType):
    bottom: str | None = None
    left: str | None = None
    right: str | None = None
    top: str | None = None


@dataclass
class SpatialStaticFile(PropertyType):
    static_file_id: str | None = None
    source: StaticFileSource | None = None


@dataclass
class StaticFile(PropertyType):
    image_static_file: ImageStaticFile | None = None
    spatial_static_file: SpatialStaticFile | None = None


@dataclass
class StaticFileS3SourceOptions(PropertyType):
    bucket_name: str | None = None
    object_key: str | None = None
    region: str | None = None


@dataclass
class StaticFileSource(PropertyType):
    s3_options: StaticFileS3SourceOptions | None = None
    url_options: StaticFileUrlSourceOptions | None = None


@dataclass
class StaticFileUrlSourceOptions(PropertyType):
    url: str | None = None


@dataclass
class StringDefaultValues(PropertyType):
    dynamic_value: DynamicDefaultValue | None = None
    static_values: list[String] = field(default_factory=list)


@dataclass
class StringFormatConfiguration(PropertyType):
    null_value_format_configuration: NullValueFormatConfiguration | None = None
    numeric_format_configuration: NumericFormatConfiguration | None = None


@dataclass
class StringParameter(PropertyType):
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class StringParameterDeclaration(PropertyType):
    name: str | None = None
    parameter_value_type: str | None = None
    default_values: StringDefaultValues | None = None
    mapped_data_set_parameters: list[MappedDataSetParameter] = field(
        default_factory=list
    )
    value_when_unset: StringValueWhenUnsetConfiguration | None = None


@dataclass
class StringValueWhenUnsetConfiguration(PropertyType):
    custom_value: str | None = None
    value_when_unset_option: str | None = None


@dataclass
class SubtotalOptions(PropertyType):
    custom_label: str | None = None
    field_level: str | None = None
    field_level_options: list[PivotTableFieldSubtotalOptions] = field(
        default_factory=list
    )
    metric_header_cell_style: TableCellStyle | None = None
    style_targets: list[TableStyleTarget] = field(default_factory=list)
    total_cell_style: TableCellStyle | None = None
    totals_visibility: str | None = None
    value_cell_style: TableCellStyle | None = None


@dataclass
class TableAggregatedFieldWells(PropertyType):
    group_by: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class TableBorderOptions(PropertyType):
    color: str | None = None
    style: str | None = None
    thickness: float | None = None


@dataclass
class TableCellConditionalFormatting(PropertyType):
    field_id: str | None = None
    text_format: TextConditionalFormat | None = None


@dataclass
class TableCellImageSizingConfiguration(PropertyType):
    table_cell_image_scaling_configuration: str | None = None


@dataclass
class TableCellStyle(PropertyType):
    background_color: str | None = None
    border: GlobalTableBorderOptions | None = None
    font_configuration: FontConfiguration | None = None
    height: float | None = None
    horizontal_text_alignment: str | None = None
    text_wrap: str | None = None
    vertical_text_alignment: str | None = None
    visibility: str | None = None


@dataclass
class TableConditionalFormatting(PropertyType):
    conditional_formatting_options: list[TableConditionalFormattingOption] = field(
        default_factory=list
    )


@dataclass
class TableConditionalFormattingOption(PropertyType):
    cell: TableCellConditionalFormatting | None = None
    row: TableRowConditionalFormatting | None = None


@dataclass
class TableConfiguration(PropertyType):
    field_options: TableFieldOptions | None = None
    field_wells: TableFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    paginated_report_options: TablePaginatedReportOptions | None = None
    sort_configuration: TableSortConfiguration | None = None
    table_inline_visualizations: list[TableInlineVisualization] = field(
        default_factory=list
    )
    table_options: TableOptions | None = None
    total_options: TotalOptions | None = None


@dataclass
class TableFieldCustomIconContent(PropertyType):
    icon: str | None = None


@dataclass
class TableFieldCustomTextContent(PropertyType):
    font_configuration: FontConfiguration | None = None
    value: str | None = None


@dataclass
class TableFieldImageConfiguration(PropertyType):
    sizing_options: TableCellImageSizingConfiguration | None = None


@dataclass
class TableFieldLinkConfiguration(PropertyType):
    content: TableFieldLinkContentConfiguration | None = None
    target: str | None = None


@dataclass
class TableFieldLinkContentConfiguration(PropertyType):
    custom_icon_content: TableFieldCustomIconContent | None = None
    custom_text_content: TableFieldCustomTextContent | None = None


@dataclass
class TableFieldOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_styling": "URLStyling",
    }

    field_id: str | None = None
    custom_label: str | None = None
    url_styling: TableFieldURLConfiguration | None = None
    visibility: str | None = None
    width: str | None = None


@dataclass
class TableFieldOptions(PropertyType):
    order: list[String] = field(default_factory=list)
    pinned_field_options: TablePinnedFieldOptions | None = None
    selected_field_options: list[TableFieldOption] = field(default_factory=list)
    transposed_table_options: list[TransposedTableOption] = field(default_factory=list)


@dataclass
class TableFieldURLConfiguration(PropertyType):
    image_configuration: TableFieldImageConfiguration | None = None
    link_configuration: TableFieldLinkConfiguration | None = None


@dataclass
class TableFieldWells(PropertyType):
    table_aggregated_field_wells: TableAggregatedFieldWells | None = None
    table_unaggregated_field_wells: TableUnaggregatedFieldWells | None = None


@dataclass
class TableInlineVisualization(PropertyType):
    data_bars: DataBarsOptions | None = None


@dataclass
class TableOptions(PropertyType):
    cell_style: TableCellStyle | None = None
    header_style: TableCellStyle | None = None
    orientation: str | None = None
    row_alternate_color_options: RowAlternateColorOptions | None = None


@dataclass
class TablePaginatedReportOptions(PropertyType):
    overflow_column_header_visibility: str | None = None
    vertical_overflow_visibility: str | None = None


@dataclass
class TablePinnedFieldOptions(PropertyType):
    pinned_left_fields: list[String] = field(default_factory=list)


@dataclass
class TableRowConditionalFormatting(PropertyType):
    background_color: ConditionalFormattingColor | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class TableSideBorderOptions(PropertyType):
    bottom: TableBorderOptions | None = None
    inner_horizontal: TableBorderOptions | None = None
    inner_vertical: TableBorderOptions | None = None
    left: TableBorderOptions | None = None
    right: TableBorderOptions | None = None
    top: TableBorderOptions | None = None


@dataclass
class TableSortConfiguration(PropertyType):
    pagination_configuration: PaginationConfiguration | None = None
    row_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class TableStyleTarget(PropertyType):
    cell_type: str | None = None


@dataclass
class TableUnaggregatedFieldWells(PropertyType):
    values: list[UnaggregatedField] = field(default_factory=list)


@dataclass
class TableVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: TableConfiguration | None = None
    conditional_formatting: TableConditionalFormatting | None = None
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class TextAreaControlDisplayOptions(PropertyType):
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    placeholder_options: TextControlPlaceholderOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class TextConditionalFormat(PropertyType):
    background_color: ConditionalFormattingColor | None = None
    icon: ConditionalFormattingIcon | None = None
    text_color: ConditionalFormattingColor | None = None


@dataclass
class TextControlPlaceholderOptions(PropertyType):
    visibility: str | None = None


@dataclass
class TextFieldControlDisplayOptions(PropertyType):
    info_icon_label_options: SheetControlInfoIconLabelOptions | None = None
    placeholder_options: TextControlPlaceholderOptions | None = None
    title_options: LabelOptions | None = None


@dataclass
class ThousandSeparatorOptions(PropertyType):
    grouping_style: str | None = None
    symbol: str | None = None
    visibility: str | None = None


@dataclass
class TimeBasedForecastProperties(PropertyType):
    lower_boundary: float | None = None
    periods_backward: float | None = None
    periods_forward: float | None = None
    prediction_interval: float | None = None
    seasonality: float | None = None
    upper_boundary: float | None = None


@dataclass
class TimeEqualityFilter(PropertyType):
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    parameter_name: str | None = None
    rolling_date: RollingDateConfiguration | None = None
    time_granularity: str | None = None
    value: str | None = None


@dataclass
class TimeRangeDrillDownFilter(PropertyType):
    column: ColumnIdentifier | None = None
    range_maximum: str | None = None
    range_minimum: str | None = None
    time_granularity: str | None = None


@dataclass
class TimeRangeFilter(PropertyType):
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    null_option: str | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    exclude_period_configuration: ExcludePeriodConfiguration | None = None
    include_maximum: bool | None = None
    include_minimum: bool | None = None
    range_maximum_value: TimeRangeFilterValue | None = None
    range_minimum_value: TimeRangeFilterValue | None = None
    time_granularity: str | None = None


@dataclass
class TimeRangeFilterValue(PropertyType):
    parameter: str | None = None
    rolling_date: RollingDateConfiguration | None = None
    static_value: str | None = None


@dataclass
class TooltipItem(PropertyType):
    column_tooltip_item: ColumnTooltipItem | None = None
    field_tooltip_item: FieldTooltipItem | None = None


@dataclass
class TooltipOptions(PropertyType):
    field_based_tooltip: FieldBasedTooltip | None = None
    selected_tooltip_type: str | None = None
    tooltip_visibility: str | None = None


@dataclass
class TopBottomFilter(PropertyType):
    aggregation_sort_configurations: list[AggregationSortConfiguration] = field(
        default_factory=list
    )
    column: ColumnIdentifier | None = None
    filter_id: str | None = None
    default_filter_control_configuration: DefaultFilterControlConfiguration | None = (
        None
    )
    limit: float | None = None
    parameter_name: str | None = None
    time_granularity: str | None = None


@dataclass
class TopBottomMoversComputation(PropertyType):
    computation_id: str | None = None
    type_: str | None = None
    category: DimensionField | None = None
    mover_size: float | None = None
    name: str | None = None
    sort_order: str | None = None
    time: DimensionField | None = None
    value: MeasureField | None = None


@dataclass
class TopBottomRankedComputation(PropertyType):
    computation_id: str | None = None
    type_: str | None = None
    category: DimensionField | None = None
    name: str | None = None
    result_size: float | None = None
    value: MeasureField | None = None


@dataclass
class TotalAggregationComputation(PropertyType):
    computation_id: str | None = None
    name: str | None = None
    value: MeasureField | None = None


@dataclass
class TotalAggregationFunction(PropertyType):
    simple_total_aggregation_function: str | None = None


@dataclass
class TotalAggregationOption(PropertyType):
    field_id: str | None = None
    total_aggregation_function: TotalAggregationFunction | None = None


@dataclass
class TotalOptions(PropertyType):
    custom_label: str | None = None
    placement: str | None = None
    scroll_status: str | None = None
    total_aggregation_options: list[TotalAggregationOption] = field(
        default_factory=list
    )
    total_cell_style: TableCellStyle | None = None
    totals_visibility: str | None = None


@dataclass
class TransposedTableOption(PropertyType):
    column_type: str | None = None
    column_index: float | None = None
    column_width: str | None = None


@dataclass
class TreeMapAggregatedFieldWells(PropertyType):
    colors: list[MeasureField] = field(default_factory=list)
    groups: list[DimensionField] = field(default_factory=list)
    sizes: list[MeasureField] = field(default_factory=list)


@dataclass
class TreeMapConfiguration(PropertyType):
    color_label_options: ChartAxisLabelOptions | None = None
    color_scale: ColorScale | None = None
    data_labels: DataLabelOptions | None = None
    field_wells: TreeMapFieldWells | None = None
    group_label_options: ChartAxisLabelOptions | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    size_label_options: ChartAxisLabelOptions | None = None
    sort_configuration: TreeMapSortConfiguration | None = None
    tooltip: TooltipOptions | None = None


@dataclass
class TreeMapFieldWells(PropertyType):
    tree_map_aggregated_field_wells: TreeMapAggregatedFieldWells | None = None


@dataclass
class TreeMapSortConfiguration(PropertyType):
    tree_map_group_items_limit_configuration: ItemsLimitConfiguration | None = None
    tree_map_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class TreeMapVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: TreeMapConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class TrendArrowOptions(PropertyType):
    visibility: str | None = None


@dataclass
class UnaggregatedField(PropertyType):
    column: ColumnIdentifier | None = None
    field_id: str | None = None
    format_configuration: FormatConfiguration | None = None


@dataclass
class UniqueValuesComputation(PropertyType):
    computation_id: str | None = None
    category: DimensionField | None = None
    name: str | None = None


@dataclass
class ValidationStrategy(PropertyType):
    mode: str | None = None


@dataclass
class VisibleRangeOptions(PropertyType):
    percent_range: PercentVisibleRange | None = None


@dataclass
class Visual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kpi_visual": "KPIVisual",
    }

    bar_chart_visual: BarChartVisual | None = None
    box_plot_visual: BoxPlotVisual | None = None
    combo_chart_visual: ComboChartVisual | None = None
    custom_content_visual: CustomContentVisual | None = None
    empty_visual: EmptyVisual | None = None
    filled_map_visual: FilledMapVisual | None = None
    funnel_chart_visual: FunnelChartVisual | None = None
    gauge_chart_visual: GaugeChartVisual | None = None
    geospatial_map_visual: GeospatialMapVisual | None = None
    heat_map_visual: HeatMapVisual | None = None
    histogram_visual: HistogramVisual | None = None
    insight_visual: InsightVisual | None = None
    kpi_visual: KPIVisual | None = None
    layer_map_visual: LayerMapVisual | None = None
    line_chart_visual: LineChartVisual | None = None
    pie_chart_visual: PieChartVisual | None = None
    pivot_table_visual: PivotTableVisual | None = None
    plugin_visual: PluginVisual | None = None
    radar_chart_visual: RadarChartVisual | None = None
    sankey_diagram_visual: SankeyDiagramVisual | None = None
    scatter_plot_visual: ScatterPlotVisual | None = None
    table_visual: TableVisual | None = None
    tree_map_visual: TreeMapVisual | None = None
    waterfall_visual: WaterfallVisual | None = None
    word_cloud_visual: WordCloudVisual | None = None


@dataclass
class VisualCustomAction(PropertyType):
    action_operations: list[VisualCustomActionOperation] = field(default_factory=list)
    custom_action_id: str | None = None
    name: str | None = None
    trigger: str | None = None
    status: str | None = None


@dataclass
class VisualCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_operation": "URLOperation",
    }

    filter_operation: CustomActionFilterOperation | None = None
    navigation_operation: CustomActionNavigationOperation | None = None
    set_parameters_operation: CustomActionSetParametersOperation | None = None
    url_operation: CustomActionURLOperation | None = None


@dataclass
class VisualInteractionOptions(PropertyType):
    context_menu_option: ContextMenuOption | None = None
    visual_menu_option: VisualMenuOption | None = None


@dataclass
class VisualMenuOption(PropertyType):
    availability_status: str | None = None


@dataclass
class VisualPalette(PropertyType):
    chart_color: str | None = None
    color_map: list[DataPathColor] = field(default_factory=list)


@dataclass
class VisualSubtitleLabelOptions(PropertyType):
    format_text: LongFormatText | None = None
    visibility: str | None = None


@dataclass
class VisualTitleLabelOptions(PropertyType):
    format_text: ShortFormatText | None = None
    visibility: str | None = None


@dataclass
class WaterfallChartAggregatedFieldWells(PropertyType):
    breakdowns: list[DimensionField] = field(default_factory=list)
    categories: list[DimensionField] = field(default_factory=list)
    values: list[MeasureField] = field(default_factory=list)


@dataclass
class WaterfallChartColorConfiguration(PropertyType):
    group_color_configuration: WaterfallChartGroupColorConfiguration | None = None


@dataclass
class WaterfallChartConfiguration(PropertyType):
    category_axis_display_options: AxisDisplayOptions | None = None
    category_axis_label_options: ChartAxisLabelOptions | None = None
    color_configuration: WaterfallChartColorConfiguration | None = None
    data_labels: DataLabelOptions | None = None
    field_wells: WaterfallChartFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    legend: LegendOptions | None = None
    primary_y_axis_display_options: AxisDisplayOptions | None = None
    primary_y_axis_label_options: ChartAxisLabelOptions | None = None
    sort_configuration: WaterfallChartSortConfiguration | None = None
    visual_palette: VisualPalette | None = None
    waterfall_chart_options: WaterfallChartOptions | None = None


@dataclass
class WaterfallChartFieldWells(PropertyType):
    waterfall_chart_aggregated_field_wells: (
        WaterfallChartAggregatedFieldWells | None
    ) = None


@dataclass
class WaterfallChartGroupColorConfiguration(PropertyType):
    negative_bar_color: str | None = None
    positive_bar_color: str | None = None
    total_bar_color: str | None = None


@dataclass
class WaterfallChartOptions(PropertyType):
    total_bar_label: str | None = None


@dataclass
class WaterfallChartSortConfiguration(PropertyType):
    breakdown_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class WaterfallVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: WaterfallChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class WhatIfPointScenario(PropertyType):
    date: str | None = None
    value: float | None = None


@dataclass
class WhatIfRangeScenario(PropertyType):
    end_date: str | None = None
    start_date: str | None = None
    value: float | None = None


@dataclass
class WordCloudAggregatedFieldWells(PropertyType):
    group_by: list[DimensionField] = field(default_factory=list)
    size: list[MeasureField] = field(default_factory=list)


@dataclass
class WordCloudChartConfiguration(PropertyType):
    category_label_options: ChartAxisLabelOptions | None = None
    field_wells: WordCloudFieldWells | None = None
    interactions: VisualInteractionOptions | None = None
    sort_configuration: WordCloudSortConfiguration | None = None
    word_cloud_options: WordCloudOptions | None = None


@dataclass
class WordCloudFieldWells(PropertyType):
    word_cloud_aggregated_field_wells: WordCloudAggregatedFieldWells | None = None


@dataclass
class WordCloudOptions(PropertyType):
    cloud_layout: str | None = None
    maximum_string_length: float | None = None
    word_casing: str | None = None
    word_orientation: str | None = None
    word_padding: str | None = None
    word_scaling: str | None = None


@dataclass
class WordCloudSortConfiguration(PropertyType):
    category_items_limit: ItemsLimitConfiguration | None = None
    category_sort: list[FieldSortOptions] = field(default_factory=list)


@dataclass
class WordCloudVisual(PropertyType):
    visual_id: str | None = None
    actions: list[VisualCustomAction] = field(default_factory=list)
    chart_configuration: WordCloudChartConfiguration | None = None
    column_hierarchies: list[ColumnHierarchy] = field(default_factory=list)
    subtitle: VisualSubtitleLabelOptions | None = None
    title: VisualTitleLabelOptions | None = None
    visual_content_alt_text: str | None = None


@dataclass
class YAxisOptions(PropertyType):
    y_axis: str | None = None
