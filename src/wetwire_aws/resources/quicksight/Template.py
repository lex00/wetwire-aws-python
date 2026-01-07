"""PropertyTypes for AWS::QuickSight::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AggregationFunction(PropertyType):
    attribute_aggregation_function: DslValue[AttributeAggregationFunction] | None = None
    categorical_aggregation_function: DslValue[str] | None = None
    date_aggregation_function: DslValue[str] | None = None
    numerical_aggregation_function: DslValue[NumericalAggregationFunction] | None = None


@dataclass
class AggregationSortConfiguration(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    sort_direction: DslValue[str] | None = None
    aggregation_function: DslValue[AggregationFunction] | None = None


@dataclass
class AnalysisDefaults(PropertyType):
    default_new_sheet_configuration: DslValue[DefaultNewSheetConfiguration] | None = (
        None
    )


@dataclass
class AnchorDateConfiguration(PropertyType):
    anchor_option: DslValue[str] | None = None
    parameter_name: DslValue[str] | None = None


@dataclass
class ArcAxisConfiguration(PropertyType):
    range: DslValue[ArcAxisDisplayRange] | None = None
    reserve_range: DslValue[float] | None = None


@dataclass
class ArcAxisDisplayRange(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class ArcConfiguration(PropertyType):
    arc_angle: DslValue[float] | None = None
    arc_thickness: DslValue[str] | None = None


@dataclass
class ArcOptions(PropertyType):
    arc_thickness: DslValue[str] | None = None


@dataclass
class AssetOptions(PropertyType):
    timezone: DslValue[str] | None = None
    week_start: DslValue[str] | None = None


@dataclass
class AttributeAggregationFunction(PropertyType):
    simple_attribute_aggregation: DslValue[str] | None = None
    value_for_multiple_values: DslValue[str] | None = None


@dataclass
class AxisDataOptions(PropertyType):
    date_axis_options: DslValue[DateAxisOptions] | None = None
    numeric_axis_options: DslValue[NumericAxisOptions] | None = None


@dataclass
class AxisDisplayMinMaxRange(PropertyType):
    maximum: DslValue[float] | None = None
    minimum: DslValue[float] | None = None


@dataclass
class AxisDisplayOptions(PropertyType):
    axis_line_visibility: DslValue[dict[str, Any]] | None = None
    axis_offset: DslValue[str] | None = None
    data_options: DslValue[AxisDataOptions] | None = None
    grid_line_visibility: DslValue[dict[str, Any]] | None = None
    scrollbar_options: DslValue[ScrollBarOptions] | None = None
    tick_label_options: DslValue[AxisTickLabelOptions] | None = None


@dataclass
class AxisDisplayRange(PropertyType):
    data_driven: DslValue[dict[str, Any]] | None = None
    min_max: DslValue[AxisDisplayMinMaxRange] | None = None


@dataclass
class AxisLabelOptions(PropertyType):
    apply_to: DslValue[AxisLabelReferenceOptions] | None = None
    custom_label: DslValue[str] | None = None
    font_configuration: DslValue[FontConfiguration] | None = None


@dataclass
class AxisLabelReferenceOptions(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None


@dataclass
class AxisLinearScale(PropertyType):
    step_count: DslValue[float] | None = None
    step_size: DslValue[float] | None = None


@dataclass
class AxisLogarithmicScale(PropertyType):
    base: DslValue[float] | None = None


@dataclass
class AxisScale(PropertyType):
    linear: DslValue[AxisLinearScale] | None = None
    logarithmic: DslValue[AxisLogarithmicScale] | None = None


@dataclass
class AxisTickLabelOptions(PropertyType):
    label_options: DslValue[LabelOptions] | None = None
    rotation_angle: DslValue[float] | None = None


@dataclass
class BarChartAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    colors: list[DslValue[DimensionField]] = field(default_factory=list)
    small_multiples: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class BarChartConfiguration(PropertyType):
    bars_arrangement: DslValue[str] | None = None
    category_axis: DslValue[AxisDisplayOptions] | None = None
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    color_label_options: DslValue[ChartAxisLabelOptions] | None = None
    contribution_analysis_defaults: list[DslValue[ContributionAnalysisDefault]] = field(
        default_factory=list
    )
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[BarChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    orientation: DslValue[str] | None = None
    reference_lines: list[DslValue[ReferenceLine]] = field(default_factory=list)
    small_multiples_options: DslValue[SmallMultiplesOptions] | None = None
    sort_configuration: DslValue[BarChartSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    value_axis: DslValue[AxisDisplayOptions] | None = None
    value_label_options: DslValue[ChartAxisLabelOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class BarChartFieldWells(PropertyType):
    bar_chart_aggregated_field_wells: DslValue[BarChartAggregatedFieldWells] | None = (
        None
    )


@dataclass
class BarChartSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    color_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    color_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    small_multiples_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None
    small_multiples_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class BarChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[BarChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class BinCountOptions(PropertyType):
    value: DslValue[float] | None = None


@dataclass
class BinWidthOptions(PropertyType):
    bin_count_limit: DslValue[float] | None = None
    value: DslValue[float] | None = None


@dataclass
class BodySectionConfiguration(PropertyType):
    content: DslValue[BodySectionContent] | None = None
    section_id: DslValue[str] | None = None
    page_break_configuration: DslValue[SectionPageBreakConfiguration] | None = None
    repeat_configuration: DslValue[BodySectionRepeatConfiguration] | None = None
    style: DslValue[SectionStyle] | None = None


@dataclass
class BodySectionContent(PropertyType):
    layout: DslValue[SectionLayoutConfiguration] | None = None


@dataclass
class BodySectionDynamicCategoryDimensionConfiguration(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    limit: DslValue[float] | None = None
    sort_by_metrics: list[DslValue[ColumnSort]] = field(default_factory=list)


@dataclass
class BodySectionDynamicNumericDimensionConfiguration(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    limit: DslValue[float] | None = None
    sort_by_metrics: list[DslValue[ColumnSort]] = field(default_factory=list)


@dataclass
class BodySectionRepeatConfiguration(PropertyType):
    dimension_configurations: list[
        DslValue[BodySectionRepeatDimensionConfiguration]
    ] = field(default_factory=list)
    non_repeating_visuals: list[DslValue[str]] = field(default_factory=list)
    page_break_configuration: (
        DslValue[BodySectionRepeatPageBreakConfiguration] | None
    ) = None


@dataclass
class BodySectionRepeatDimensionConfiguration(PropertyType):
    dynamic_category_dimension_configuration: (
        DslValue[BodySectionDynamicCategoryDimensionConfiguration] | None
    ) = None
    dynamic_numeric_dimension_configuration: (
        DslValue[BodySectionDynamicNumericDimensionConfiguration] | None
    ) = None


@dataclass
class BodySectionRepeatPageBreakConfiguration(PropertyType):
    after: DslValue[SectionAfterPageBreak] | None = None


@dataclass
class BoxPlotAggregatedFieldWells(PropertyType):
    group_by: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class BoxPlotChartConfiguration(PropertyType):
    box_plot_options: DslValue[BoxPlotOptions] | None = None
    category_axis: DslValue[AxisDisplayOptions] | None = None
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    field_wells: DslValue[BoxPlotFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    primary_y_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    primary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    reference_lines: list[DslValue[ReferenceLine]] = field(default_factory=list)
    sort_configuration: DslValue[BoxPlotSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class BoxPlotFieldWells(PropertyType):
    box_plot_aggregated_field_wells: DslValue[BoxPlotAggregatedFieldWells] | None = None


@dataclass
class BoxPlotOptions(PropertyType):
    all_data_points_visibility: DslValue[dict[str, Any]] | None = None
    outlier_visibility: DslValue[dict[str, Any]] | None = None
    style_options: DslValue[BoxPlotStyleOptions] | None = None


@dataclass
class BoxPlotSortConfiguration(PropertyType):
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    pagination_configuration: DslValue[PaginationConfiguration] | None = None


@dataclass
class BoxPlotStyleOptions(PropertyType):
    fill_style: DslValue[str] | None = None


@dataclass
class BoxPlotVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[BoxPlotChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class CalculatedField(PropertyType):
    data_set_identifier: DslValue[str] | None = None
    expression: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class CalculatedMeasureField(PropertyType):
    expression: DslValue[str] | None = None
    field_id: DslValue[str] | None = None


@dataclass
class CascadingControlConfiguration(PropertyType):
    source_controls: list[DslValue[CascadingControlSource]] = field(
        default_factory=list
    )


@dataclass
class CascadingControlSource(PropertyType):
    column_to_match: DslValue[ColumnIdentifier] | None = None
    source_sheet_control_id: DslValue[str] | None = None


@dataclass
class CategoricalDimensionField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    format_configuration: DslValue[StringFormatConfiguration] | None = None
    hierarchy_id: DslValue[str] | None = None


@dataclass
class CategoricalMeasureField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    aggregation_function: DslValue[str] | None = None
    format_configuration: DslValue[StringFormatConfiguration] | None = None


@dataclass
class CategoryDrillDownFilter(PropertyType):
    category_values: list[DslValue[str]] = field(default_factory=list)
    column: DslValue[ColumnIdentifier] | None = None


@dataclass
class CategoryFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    configuration: DslValue[CategoryFilterConfiguration] | None = None
    filter_id: DslValue[str] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None


@dataclass
class CategoryFilterConfiguration(PropertyType):
    custom_filter_configuration: DslValue[CustomFilterConfiguration] | None = None
    custom_filter_list_configuration: DslValue[CustomFilterListConfiguration] | None = (
        None
    )
    filter_list_configuration: DslValue[FilterListConfiguration] | None = None


@dataclass
class CategoryInnerFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    configuration: DslValue[CategoryFilterConfiguration] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None


@dataclass
class ChartAxisLabelOptions(PropertyType):
    axis_label_options: list[DslValue[AxisLabelOptions]] = field(default_factory=list)
    sort_icon_visibility: DslValue[dict[str, Any]] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class ClusterMarker(PropertyType):
    simple_cluster_marker: DslValue[SimpleClusterMarker] | None = None


@dataclass
class ClusterMarkerConfiguration(PropertyType):
    cluster_marker: DslValue[ClusterMarker] | None = None


@dataclass
class ColorScale(PropertyType):
    color_fill_type: DslValue[str] | None = None
    colors: list[DslValue[DataColor]] = field(default_factory=list)
    null_value_color: DslValue[DataColor] | None = None


@dataclass
class ColorsConfiguration(PropertyType):
    custom_colors: list[DslValue[CustomColor]] = field(default_factory=list)


@dataclass
class ColumnConfiguration(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    colors_configuration: DslValue[ColorsConfiguration] | None = None
    format_configuration: DslValue[FormatConfiguration] | None = None
    role: DslValue[str] | None = None


@dataclass
class ColumnGroupColumnSchema(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class ColumnGroupSchema(PropertyType):
    column_group_column_schema_list: list[DslValue[ColumnGroupColumnSchema]] = field(
        default_factory=list
    )
    name: DslValue[str] | None = None


@dataclass
class ColumnHierarchy(PropertyType):
    date_time_hierarchy: DslValue[DateTimeHierarchy] | None = None
    explicit_hierarchy: DslValue[ExplicitHierarchy] | None = None
    predefined_hierarchy: DslValue[PredefinedHierarchy] | None = None


@dataclass
class ColumnIdentifier(PropertyType):
    column_name: DslValue[str] | None = None
    data_set_identifier: DslValue[str] | None = None


@dataclass
class ColumnSchema(PropertyType):
    data_type: DslValue[str] | None = None
    geographic_role: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class ColumnSort(PropertyType):
    direction: DslValue[str] | None = None
    sort_by: DslValue[ColumnIdentifier] | None = None
    aggregation_function: DslValue[AggregationFunction] | None = None


@dataclass
class ColumnTooltipItem(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    aggregation: DslValue[AggregationFunction] | None = None
    label: DslValue[str] | None = None
    tooltip_target: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class ComboChartAggregatedFieldWells(PropertyType):
    bar_values: list[DslValue[MeasureField]] = field(default_factory=list)
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    colors: list[DslValue[DimensionField]] = field(default_factory=list)
    line_values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class ComboChartConfiguration(PropertyType):
    bar_data_labels: DslValue[DataLabelOptions] | None = None
    bars_arrangement: DslValue[str] | None = None
    category_axis: DslValue[AxisDisplayOptions] | None = None
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    color_label_options: DslValue[ChartAxisLabelOptions] | None = None
    field_wells: DslValue[ComboChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    line_data_labels: DslValue[DataLabelOptions] | None = None
    primary_y_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    primary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    reference_lines: list[DslValue[ReferenceLine]] = field(default_factory=list)
    secondary_y_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    secondary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    single_axis_options: DslValue[SingleAxisOptions] | None = None
    sort_configuration: DslValue[ComboChartSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class ComboChartFieldWells(PropertyType):
    combo_chart_aggregated_field_wells: (
        DslValue[ComboChartAggregatedFieldWells] | None
    ) = None


@dataclass
class ComboChartSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    color_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    color_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class ComboChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[ComboChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class ComparisonConfiguration(PropertyType):
    comparison_format: DslValue[ComparisonFormatConfiguration] | None = None
    comparison_method: DslValue[str] | None = None


@dataclass
class ComparisonFormatConfiguration(PropertyType):
    number_display_format_configuration: (
        DslValue[NumberDisplayFormatConfiguration] | None
    ) = None
    percentage_display_format_configuration: (
        DslValue[PercentageDisplayFormatConfiguration] | None
    ) = None


@dataclass
class Computation(PropertyType):
    forecast: DslValue[ForecastComputation] | None = None
    growth_rate: DslValue[GrowthRateComputation] | None = None
    maximum_minimum: DslValue[MaximumMinimumComputation] | None = None
    metric_comparison: DslValue[MetricComparisonComputation] | None = None
    period_over_period: DslValue[PeriodOverPeriodComputation] | None = None
    period_to_date: DslValue[PeriodToDateComputation] | None = None
    top_bottom_movers: DslValue[TopBottomMoversComputation] | None = None
    top_bottom_ranked: DslValue[TopBottomRankedComputation] | None = None
    total_aggregation: DslValue[TotalAggregationComputation] | None = None
    unique_values: DslValue[UniqueValuesComputation] | None = None


@dataclass
class ConditionalFormattingColor(PropertyType):
    gradient: DslValue[ConditionalFormattingGradientColor] | None = None
    solid: DslValue[ConditionalFormattingSolidColor] | None = None


@dataclass
class ConditionalFormattingCustomIconCondition(PropertyType):
    expression: DslValue[str] | None = None
    icon_options: DslValue[ConditionalFormattingCustomIconOptions] | None = None
    color: DslValue[str] | None = None
    display_configuration: (
        DslValue[ConditionalFormattingIconDisplayConfiguration] | None
    ) = None


@dataclass
class ConditionalFormattingCustomIconOptions(PropertyType):
    icon: DslValue[str] | None = None
    unicode_icon: DslValue[str] | None = None


@dataclass
class ConditionalFormattingGradientColor(PropertyType):
    color: DslValue[GradientColor] | None = None
    expression: DslValue[str] | None = None


@dataclass
class ConditionalFormattingIcon(PropertyType):
    custom_condition: DslValue[ConditionalFormattingCustomIconCondition] | None = None
    icon_set: DslValue[ConditionalFormattingIconSet] | None = None


@dataclass
class ConditionalFormattingIconDisplayConfiguration(PropertyType):
    icon_display_option: DslValue[str] | None = None


@dataclass
class ConditionalFormattingIconSet(PropertyType):
    expression: DslValue[str] | None = None
    icon_set_type: DslValue[str] | None = None


@dataclass
class ConditionalFormattingSolidColor(PropertyType):
    expression: DslValue[str] | None = None
    color: DslValue[str] | None = None


@dataclass
class ContextMenuOption(PropertyType):
    availability_status: DslValue[str] | None = None


@dataclass
class ContributionAnalysisDefault(PropertyType):
    contributor_dimensions: list[DslValue[ColumnIdentifier]] = field(
        default_factory=list
    )
    measure_field_id: DslValue[str] | None = None


@dataclass
class CurrencyDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DslValue[DecimalPlacesConfiguration] | None = None
    negative_value_configuration: DslValue[NegativeValueConfiguration] | None = None
    null_value_format_configuration: DslValue[NullValueFormatConfiguration] | None = (
        None
    )
    number_scale: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    separator_configuration: DslValue[NumericSeparatorConfiguration] | None = None
    suffix: DslValue[str] | None = None
    symbol: DslValue[str] | None = None


@dataclass
class CustomActionFilterOperation(PropertyType):
    selected_fields_configuration: (
        DslValue[FilterOperationSelectedFieldsConfiguration] | None
    ) = None
    target_visuals_configuration: (
        DslValue[FilterOperationTargetVisualsConfiguration] | None
    ) = None


@dataclass
class CustomActionNavigationOperation(PropertyType):
    local_navigation_configuration: DslValue[LocalNavigationConfiguration] | None = None


@dataclass
class CustomActionSetParametersOperation(PropertyType):
    parameter_value_configurations: list[DslValue[SetParameterValueConfiguration]] = (
        field(default_factory=list)
    )


@dataclass
class CustomActionURLOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_target": "URLTarget",
        "url_template": "URLTemplate",
    }

    url_target: DslValue[str] | None = None
    url_template: DslValue[str] | None = None


@dataclass
class CustomColor(PropertyType):
    color: DslValue[str] | None = None
    field_value: DslValue[str] | None = None
    special_value: DslValue[str] | None = None


@dataclass
class CustomContentConfiguration(PropertyType):
    content_type: DslValue[str] | None = None
    content_url: DslValue[str] | None = None
    image_scaling: DslValue[str] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None


@dataclass
class CustomContentVisual(PropertyType):
    data_set_identifier: DslValue[str] | None = None
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[CustomContentConfiguration] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class CustomFilterConfiguration(PropertyType):
    match_operator: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    category_value: DslValue[str] | None = None
    parameter_name: DslValue[str] | None = None
    select_all_options: DslValue[str] | None = None


@dataclass
class CustomFilterListConfiguration(PropertyType):
    match_operator: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    category_values: list[DslValue[str]] = field(default_factory=list)
    select_all_options: DslValue[str] | None = None


@dataclass
class CustomNarrativeOptions(PropertyType):
    narrative: DslValue[str] | None = None


@dataclass
class CustomParameterValues(PropertyType):
    date_time_values: list[DslValue[str]] = field(default_factory=list)
    decimal_values: list[DslValue[float]] = field(default_factory=list)
    integer_values: list[DslValue[float]] = field(default_factory=list)
    string_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CustomValuesConfiguration(PropertyType):
    custom_values: DslValue[CustomParameterValues] | None = None
    include_null_value: DslValue[bool] | None = None


@dataclass
class DataBarsOptions(PropertyType):
    field_id: DslValue[str] | None = None
    negative_color: DslValue[str] | None = None
    positive_color: DslValue[str] | None = None


@dataclass
class DataColor(PropertyType):
    color: DslValue[str] | None = None
    data_value: DslValue[float] | None = None


@dataclass
class DataFieldSeriesItem(PropertyType):
    axis_binding: DslValue[str] | None = None
    field_id: DslValue[str] | None = None
    field_value: DslValue[str] | None = None
    settings: DslValue[LineChartSeriesSettings] | None = None


@dataclass
class DataLabelOptions(PropertyType):
    category_label_visibility: DslValue[dict[str, Any]] | None = None
    data_label_types: list[DslValue[DataLabelType]] = field(default_factory=list)
    label_color: DslValue[str] | None = None
    label_content: DslValue[str] | None = None
    label_font_configuration: DslValue[FontConfiguration] | None = None
    measure_label_visibility: DslValue[dict[str, Any]] | None = None
    overlap: DslValue[str] | None = None
    position: DslValue[str] | None = None
    totals_visibility: DslValue[dict[str, Any]] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class DataLabelType(PropertyType):
    data_path_label_type: DslValue[DataPathLabelType] | None = None
    field_label_type: DslValue[FieldLabelType] | None = None
    maximum_label_type: DslValue[MaximumLabelType] | None = None
    minimum_label_type: DslValue[MinimumLabelType] | None = None
    range_ends_label_type: DslValue[RangeEndsLabelType] | None = None


@dataclass
class DataPathColor(PropertyType):
    color: DslValue[str] | None = None
    element: DslValue[DataPathValue] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class DataPathLabelType(PropertyType):
    field_id: DslValue[str] | None = None
    field_value: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class DataPathSort(PropertyType):
    direction: DslValue[str] | None = None
    sort_paths: list[DslValue[DataPathValue]] = field(default_factory=list)


@dataclass
class DataPathType(PropertyType):
    pivot_table_data_path_type: DslValue[str] | None = None


@dataclass
class DataPathValue(PropertyType):
    data_path_type: DslValue[DataPathType] | None = None
    field_id: DslValue[str] | None = None
    field_value: DslValue[str] | None = None


@dataclass
class DataSetConfiguration(PropertyType):
    column_group_schema_list: list[DslValue[ColumnGroupSchema]] = field(
        default_factory=list
    )
    data_set_schema: DslValue[DataSetSchema] | None = None
    placeholder: DslValue[str] | None = None


@dataclass
class DataSetReference(PropertyType):
    data_set_arn: DslValue[str] | None = None
    data_set_placeholder: DslValue[str] | None = None


@dataclass
class DataSetSchema(PropertyType):
    column_schema_list: list[DslValue[ColumnSchema]] = field(default_factory=list)


@dataclass
class DateAxisOptions(PropertyType):
    missing_date_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class DateDimensionField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    date_granularity: DslValue[str] | None = None
    format_configuration: DslValue[DateTimeFormatConfiguration] | None = None
    hierarchy_id: DslValue[str] | None = None


@dataclass
class DateMeasureField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    aggregation_function: DslValue[str] | None = None
    format_configuration: DslValue[DateTimeFormatConfiguration] | None = None


@dataclass
class DateTimeDefaultValues(PropertyType):
    dynamic_value: DslValue[DynamicDefaultValue] | None = None
    rolling_date: DslValue[RollingDateConfiguration] | None = None
    static_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DateTimeFormatConfiguration(PropertyType):
    date_time_format: DslValue[str] | None = None
    null_value_format_configuration: DslValue[NullValueFormatConfiguration] | None = (
        None
    )
    numeric_format_configuration: DslValue[NumericFormatConfiguration] | None = None


@dataclass
class DateTimeHierarchy(PropertyType):
    hierarchy_id: DslValue[str] | None = None
    drill_down_filters: list[DslValue[DrillDownFilter]] = field(default_factory=list)


@dataclass
class DateTimeParameterDeclaration(PropertyType):
    name: DslValue[str] | None = None
    default_values: DslValue[DateTimeDefaultValues] | None = None
    mapped_data_set_parameters: list[DslValue[MappedDataSetParameter]] = field(
        default_factory=list
    )
    time_granularity: DslValue[str] | None = None
    value_when_unset: DslValue[DateTimeValueWhenUnsetConfiguration] | None = None


@dataclass
class DateTimePickerControlDisplayOptions(PropertyType):
    date_icon_visibility: DslValue[dict[str, Any]] | None = None
    date_time_format: DslValue[str] | None = None
    helper_text_visibility: DslValue[dict[str, Any]] | None = None
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class DateTimeValueWhenUnsetConfiguration(PropertyType):
    custom_value: DslValue[str] | None = None
    value_when_unset_option: DslValue[str] | None = None


@dataclass
class DecimalDefaultValues(PropertyType):
    dynamic_value: DslValue[DynamicDefaultValue] | None = None
    static_values: list[DslValue[float]] = field(default_factory=list)


@dataclass
class DecimalParameterDeclaration(PropertyType):
    name: DslValue[str] | None = None
    parameter_value_type: DslValue[str] | None = None
    default_values: DslValue[DecimalDefaultValues] | None = None
    mapped_data_set_parameters: list[DslValue[MappedDataSetParameter]] = field(
        default_factory=list
    )
    value_when_unset: DslValue[DecimalValueWhenUnsetConfiguration] | None = None


@dataclass
class DecimalPlacesConfiguration(PropertyType):
    decimal_places: DslValue[float] | None = None


@dataclass
class DecimalValueWhenUnsetConfiguration(PropertyType):
    custom_value: DslValue[float] | None = None
    value_when_unset_option: DslValue[str] | None = None


@dataclass
class DefaultDateTimePickerControlOptions(PropertyType):
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[DateTimePickerControlDisplayOptions] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DefaultFilterControlConfiguration(PropertyType):
    control_options: DslValue[DefaultFilterControlOptions] | None = None
    title: DslValue[str] | None = None


@dataclass
class DefaultFilterControlOptions(PropertyType):
    default_date_time_picker_options: (
        DslValue[DefaultDateTimePickerControlOptions] | None
    ) = None
    default_dropdown_options: DslValue[DefaultFilterDropDownControlOptions] | None = (
        None
    )
    default_list_options: DslValue[DefaultFilterListControlOptions] | None = None
    default_relative_date_time_options: (
        DslValue[DefaultRelativeDateTimeControlOptions] | None
    ) = None
    default_slider_options: DslValue[DefaultSliderControlOptions] | None = None
    default_text_area_options: DslValue[DefaultTextAreaControlOptions] | None = None
    default_text_field_options: DslValue[DefaultTextFieldControlOptions] | None = None


@dataclass
class DefaultFilterDropDownControlOptions(PropertyType):
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[DropDownControlDisplayOptions] | None = None
    selectable_values: DslValue[FilterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DefaultFilterListControlOptions(PropertyType):
    display_options: DslValue[ListControlDisplayOptions] | None = None
    selectable_values: DslValue[FilterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DefaultFreeFormLayoutConfiguration(PropertyType):
    canvas_size_options: DslValue[FreeFormLayoutCanvasSizeOptions] | None = None


@dataclass
class DefaultGridLayoutConfiguration(PropertyType):
    canvas_size_options: DslValue[GridLayoutCanvasSizeOptions] | None = None


@dataclass
class DefaultInteractiveLayoutConfiguration(PropertyType):
    free_form: DslValue[DefaultFreeFormLayoutConfiguration] | None = None
    grid: DslValue[DefaultGridLayoutConfiguration] | None = None


@dataclass
class DefaultNewSheetConfiguration(PropertyType):
    interactive_layout_configuration: (
        DslValue[DefaultInteractiveLayoutConfiguration] | None
    ) = None
    paginated_layout_configuration: (
        DslValue[DefaultPaginatedLayoutConfiguration] | None
    ) = None
    sheet_content_type: DslValue[str] | None = None


@dataclass
class DefaultPaginatedLayoutConfiguration(PropertyType):
    section_based: DslValue[DefaultSectionBasedLayoutConfiguration] | None = None


@dataclass
class DefaultRelativeDateTimeControlOptions(PropertyType):
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[RelativeDateTimeControlDisplayOptions] | None = None


@dataclass
class DefaultSectionBasedLayoutConfiguration(PropertyType):
    canvas_size_options: DslValue[SectionBasedLayoutCanvasSizeOptions] | None = None


@dataclass
class DefaultSliderControlOptions(PropertyType):
    maximum_value: DslValue[float] | None = None
    minimum_value: DslValue[float] | None = None
    step_size: DslValue[float] | None = None
    display_options: DslValue[SliderControlDisplayOptions] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DefaultTextAreaControlOptions(PropertyType):
    delimiter: DslValue[str] | None = None
    display_options: DslValue[TextAreaControlDisplayOptions] | None = None


@dataclass
class DefaultTextFieldControlOptions(PropertyType):
    display_options: DslValue[TextFieldControlDisplayOptions] | None = None


@dataclass
class DestinationParameterValueConfiguration(PropertyType):
    custom_values_configuration: DslValue[CustomValuesConfiguration] | None = None
    select_all_value_options: DslValue[str] | None = None
    source_column: DslValue[ColumnIdentifier] | None = None
    source_field: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None


@dataclass
class DimensionField(PropertyType):
    categorical_dimension_field: DslValue[CategoricalDimensionField] | None = None
    date_dimension_field: DslValue[DateDimensionField] | None = None
    numerical_dimension_field: DslValue[NumericalDimensionField] | None = None


@dataclass
class DonutCenterOptions(PropertyType):
    label_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class DonutOptions(PropertyType):
    arc_options: DslValue[ArcOptions] | None = None
    donut_center_options: DslValue[DonutCenterOptions] | None = None


@dataclass
class DrillDownFilter(PropertyType):
    category_filter: DslValue[CategoryDrillDownFilter] | None = None
    numeric_equality_filter: DslValue[NumericEqualityDrillDownFilter] | None = None
    time_range_filter: DslValue[TimeRangeDrillDownFilter] | None = None


@dataclass
class DropDownControlDisplayOptions(PropertyType):
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    select_all_options: DslValue[ListControlSelectAllOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class DynamicDefaultValue(PropertyType):
    default_value_column: DslValue[ColumnIdentifier] | None = None
    group_name_column: DslValue[ColumnIdentifier] | None = None
    user_name_column: DslValue[ColumnIdentifier] | None = None


@dataclass
class EmptyVisual(PropertyType):
    data_set_identifier: DslValue[str] | None = None
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)


@dataclass
class Entity(PropertyType):
    path: DslValue[str] | None = None


@dataclass
class ExcludePeriodConfiguration(PropertyType):
    amount: DslValue[float] | None = None
    granularity: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class ExplicitHierarchy(PropertyType):
    columns: list[DslValue[ColumnIdentifier]] = field(default_factory=list)
    hierarchy_id: DslValue[str] | None = None
    drill_down_filters: list[DslValue[DrillDownFilter]] = field(default_factory=list)


@dataclass
class FieldBasedTooltip(PropertyType):
    aggregation_visibility: DslValue[dict[str, Any]] | None = None
    tooltip_fields: list[DslValue[TooltipItem]] = field(default_factory=list)
    tooltip_title_type: DslValue[str] | None = None


@dataclass
class FieldLabelType(PropertyType):
    field_id: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FieldSeriesItem(PropertyType):
    axis_binding: DslValue[str] | None = None
    field_id: DslValue[str] | None = None
    settings: DslValue[LineChartSeriesSettings] | None = None


@dataclass
class FieldSort(PropertyType):
    direction: DslValue[str] | None = None
    field_id: DslValue[str] | None = None


@dataclass
class FieldSortOptions(PropertyType):
    column_sort: DslValue[ColumnSort] | None = None
    field_sort: DslValue[FieldSort] | None = None


@dataclass
class FieldTooltipItem(PropertyType):
    field_id: DslValue[str] | None = None
    label: DslValue[str] | None = None
    tooltip_target: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FilledMapAggregatedFieldWells(PropertyType):
    geospatial: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class FilledMapConditionalFormatting(PropertyType):
    conditional_formatting_options: list[
        DslValue[FilledMapConditionalFormattingOption]
    ] = field(default_factory=list)


@dataclass
class FilledMapConditionalFormattingOption(PropertyType):
    shape: DslValue[FilledMapShapeConditionalFormatting] | None = None


@dataclass
class FilledMapConfiguration(PropertyType):
    field_wells: DslValue[FilledMapFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    map_style_options: DslValue[GeospatialMapStyleOptions] | None = None
    sort_configuration: DslValue[FilledMapSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    window_options: DslValue[GeospatialWindowOptions] | None = None


@dataclass
class FilledMapFieldWells(PropertyType):
    filled_map_aggregated_field_wells: (
        DslValue[FilledMapAggregatedFieldWells] | None
    ) = None


@dataclass
class FilledMapShapeConditionalFormatting(PropertyType):
    field_id: DslValue[str] | None = None
    format: DslValue[ShapeConditionalFormat] | None = None


@dataclass
class FilledMapSortConfiguration(PropertyType):
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class FilledMapVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[FilledMapConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    conditional_formatting: DslValue[FilledMapConditionalFormatting] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class Filter(PropertyType):
    category_filter: DslValue[CategoryFilter] | None = None
    nested_filter: DslValue[NestedFilter] | None = None
    numeric_equality_filter: DslValue[NumericEqualityFilter] | None = None
    numeric_range_filter: DslValue[NumericRangeFilter] | None = None
    relative_dates_filter: DslValue[RelativeDatesFilter] | None = None
    time_equality_filter: DslValue[TimeEqualityFilter] | None = None
    time_range_filter: DslValue[TimeRangeFilter] | None = None
    top_bottom_filter: DslValue[TopBottomFilter] | None = None


@dataclass
class FilterControl(PropertyType):
    cross_sheet: DslValue[FilterCrossSheetControl] | None = None
    date_time_picker: DslValue[FilterDateTimePickerControl] | None = None
    dropdown: DslValue[FilterDropDownControl] | None = None
    list: DslValue[FilterListControl] | None = None
    relative_date_time: DslValue[FilterRelativeDateTimeControl] | None = None
    slider: DslValue[FilterSliderControl] | None = None
    text_area: DslValue[FilterTextAreaControl] | None = None
    text_field: DslValue[FilterTextFieldControl] | None = None


@dataclass
class FilterCrossSheetControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    cascading_control_configuration: DslValue[CascadingControlConfiguration] | None = (
        None
    )


@dataclass
class FilterDateTimePickerControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[DateTimePickerControlDisplayOptions] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FilterDropDownControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    cascading_control_configuration: DslValue[CascadingControlConfiguration] | None = (
        None
    )
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[DropDownControlDisplayOptions] | None = None
    selectable_values: DslValue[FilterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FilterGroup(PropertyType):
    cross_dataset: DslValue[str] | None = None
    filter_group_id: DslValue[str] | None = None
    filters: list[DslValue[Filter]] = field(default_factory=list)
    scope_configuration: DslValue[FilterScopeConfiguration] | None = None
    status: DslValue[str] | None = None


@dataclass
class FilterListConfiguration(PropertyType):
    match_operator: DslValue[str] | None = None
    category_values: list[DslValue[str]] = field(default_factory=list)
    null_option: DslValue[str] | None = None
    select_all_options: DslValue[str] | None = None


@dataclass
class FilterListControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    cascading_control_configuration: DslValue[CascadingControlConfiguration] | None = (
        None
    )
    display_options: DslValue[ListControlDisplayOptions] | None = None
    selectable_values: DslValue[FilterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FilterOperationSelectedFieldsConfiguration(PropertyType):
    selected_columns: list[DslValue[ColumnIdentifier]] = field(default_factory=list)
    selected_field_options: DslValue[str] | None = None
    selected_fields: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FilterOperationTargetVisualsConfiguration(PropertyType):
    same_sheet_target_visual_configuration: (
        DslValue[SameSheetTargetVisualConfiguration] | None
    ) = None


@dataclass
class FilterRelativeDateTimeControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[RelativeDateTimeControlDisplayOptions] | None = None


@dataclass
class FilterScopeConfiguration(PropertyType):
    all_sheets: DslValue[dict[str, Any]] | None = None
    selected_sheets: DslValue[SelectedSheetsFilterScopeConfiguration] | None = None


@dataclass
class FilterSelectableValues(PropertyType):
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FilterSliderControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    maximum_value: DslValue[float] | None = None
    minimum_value: DslValue[float] | None = None
    source_filter_id: DslValue[str] | None = None
    step_size: DslValue[float] | None = None
    title: DslValue[str] | None = None
    display_options: DslValue[SliderControlDisplayOptions] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FilterTextAreaControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    delimiter: DslValue[str] | None = None
    display_options: DslValue[TextAreaControlDisplayOptions] | None = None


@dataclass
class FilterTextFieldControl(PropertyType):
    filter_control_id: DslValue[str] | None = None
    source_filter_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    display_options: DslValue[TextFieldControlDisplayOptions] | None = None


@dataclass
class FontConfiguration(PropertyType):
    font_color: DslValue[str] | None = None
    font_decoration: DslValue[str] | None = None
    font_family: DslValue[str] | None = None
    font_size: DslValue[FontSize] | None = None
    font_style: DslValue[str] | None = None
    font_weight: DslValue[FontWeight] | None = None


@dataclass
class FontSize(PropertyType):
    absolute: DslValue[str] | None = None
    relative: DslValue[str] | None = None


@dataclass
class FontWeight(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class ForecastComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    custom_seasonality_value: DslValue[float] | None = None
    lower_boundary: DslValue[float] | None = None
    name: DslValue[str] | None = None
    periods_backward: DslValue[float] | None = None
    periods_forward: DslValue[float] | None = None
    prediction_interval: DslValue[float] | None = None
    seasonality: DslValue[str] | None = None
    time: DslValue[DimensionField] | None = None
    upper_boundary: DslValue[float] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class ForecastConfiguration(PropertyType):
    forecast_properties: DslValue[TimeBasedForecastProperties] | None = None
    scenario: DslValue[ForecastScenario] | None = None


@dataclass
class ForecastScenario(PropertyType):
    what_if_point_scenario: DslValue[WhatIfPointScenario] | None = None
    what_if_range_scenario: DslValue[WhatIfRangeScenario] | None = None


@dataclass
class FormatConfiguration(PropertyType):
    date_time_format_configuration: DslValue[DateTimeFormatConfiguration] | None = None
    number_format_configuration: DslValue[NumberFormatConfiguration] | None = None
    string_format_configuration: DslValue[StringFormatConfiguration] | None = None


@dataclass
class FreeFormLayoutCanvasSizeOptions(PropertyType):
    screen_canvas_size_options: (
        DslValue[FreeFormLayoutScreenCanvasSizeOptions] | None
    ) = None


@dataclass
class FreeFormLayoutConfiguration(PropertyType):
    elements: list[DslValue[FreeFormLayoutElement]] = field(default_factory=list)
    canvas_size_options: DslValue[FreeFormLayoutCanvasSizeOptions] | None = None


@dataclass
class FreeFormLayoutElement(PropertyType):
    element_id: DslValue[str] | None = None
    element_type: DslValue[str] | None = None
    height: DslValue[str] | None = None
    width: DslValue[str] | None = None
    x_axis_location: DslValue[str] | None = None
    y_axis_location: DslValue[str] | None = None
    background_style: DslValue[FreeFormLayoutElementBackgroundStyle] | None = None
    border_style: DslValue[FreeFormLayoutElementBorderStyle] | None = None
    loading_animation: DslValue[LoadingAnimation] | None = None
    rendering_rules: list[DslValue[SheetElementRenderingRule]] = field(
        default_factory=list
    )
    selected_border_style: DslValue[FreeFormLayoutElementBorderStyle] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FreeFormLayoutElementBackgroundStyle(PropertyType):
    color: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FreeFormLayoutElementBorderStyle(PropertyType):
    color: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FreeFormLayoutScreenCanvasSizeOptions(PropertyType):
    optimized_view_port_width: DslValue[str] | None = None


@dataclass
class FreeFormSectionLayoutConfiguration(PropertyType):
    elements: list[DslValue[FreeFormLayoutElement]] = field(default_factory=list)


@dataclass
class FunnelChartAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class FunnelChartConfiguration(PropertyType):
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    data_label_options: DslValue[FunnelChartDataLabelOptions] | None = None
    field_wells: DslValue[FunnelChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    sort_configuration: DslValue[FunnelChartSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    value_label_options: DslValue[ChartAxisLabelOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class FunnelChartDataLabelOptions(PropertyType):
    category_label_visibility: DslValue[dict[str, Any]] | None = None
    label_color: DslValue[str] | None = None
    label_font_configuration: DslValue[FontConfiguration] | None = None
    measure_data_label_style: DslValue[str] | None = None
    measure_label_visibility: DslValue[dict[str, Any]] | None = None
    position: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class FunnelChartFieldWells(PropertyType):
    funnel_chart_aggregated_field_wells: (
        DslValue[FunnelChartAggregatedFieldWells] | None
    ) = None


@dataclass
class FunnelChartSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class FunnelChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[FunnelChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class GaugeChartArcConditionalFormatting(PropertyType):
    foreground_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class GaugeChartColorConfiguration(PropertyType):
    background_color: DslValue[str] | None = None
    foreground_color: DslValue[str] | None = None


@dataclass
class GaugeChartConditionalFormatting(PropertyType):
    conditional_formatting_options: list[
        DslValue[GaugeChartConditionalFormattingOption]
    ] = field(default_factory=list)


@dataclass
class GaugeChartConditionalFormattingOption(PropertyType):
    arc: DslValue[GaugeChartArcConditionalFormatting] | None = None
    primary_value: DslValue[GaugeChartPrimaryValueConditionalFormatting] | None = None


@dataclass
class GaugeChartConfiguration(PropertyType):
    color_configuration: DslValue[GaugeChartColorConfiguration] | None = None
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[GaugeChartFieldWells] | None = None
    gauge_chart_options: DslValue[GaugeChartOptions] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    tooltip_options: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class GaugeChartFieldWells(PropertyType):
    target_values: list[DslValue[MeasureField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class GaugeChartOptions(PropertyType):
    arc: DslValue[ArcConfiguration] | None = None
    arc_axis: DslValue[ArcAxisConfiguration] | None = None
    comparison: DslValue[ComparisonConfiguration] | None = None
    primary_value_display_type: DslValue[str] | None = None
    primary_value_font_configuration: DslValue[FontConfiguration] | None = None


@dataclass
class GaugeChartPrimaryValueConditionalFormatting(PropertyType):
    icon: DslValue[ConditionalFormattingIcon] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class GaugeChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[GaugeChartConfiguration] | None = None
    conditional_formatting: DslValue[GaugeChartConditionalFormatting] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class GeospatialCoordinateBounds(PropertyType):
    east: DslValue[float] | None = None
    north: DslValue[float] | None = None
    south: DslValue[float] | None = None
    west: DslValue[float] | None = None


@dataclass
class GeospatialHeatmapColorScale(PropertyType):
    colors: list[DslValue[GeospatialHeatmapDataColor]] = field(default_factory=list)


@dataclass
class GeospatialHeatmapConfiguration(PropertyType):
    heatmap_color: DslValue[GeospatialHeatmapColorScale] | None = None


@dataclass
class GeospatialHeatmapDataColor(PropertyType):
    color: DslValue[str] | None = None


@dataclass
class GeospatialMapAggregatedFieldWells(PropertyType):
    colors: list[DslValue[DimensionField]] = field(default_factory=list)
    geospatial: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class GeospatialMapConfiguration(PropertyType):
    field_wells: DslValue[GeospatialMapFieldWells] | None = None
    legend: DslValue[LegendOptions] | None = None
    map_style_options: DslValue[GeospatialMapStyleOptions] | None = None
    point_style_options: DslValue[GeospatialPointStyleOptions] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None
    window_options: DslValue[GeospatialWindowOptions] | None = None


@dataclass
class GeospatialMapFieldWells(PropertyType):
    geospatial_map_aggregated_field_wells: (
        DslValue[GeospatialMapAggregatedFieldWells] | None
    ) = None


@dataclass
class GeospatialMapStyleOptions(PropertyType):
    base_map_style: DslValue[str] | None = None


@dataclass
class GeospatialMapVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[GeospatialMapConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class GeospatialPointStyleOptions(PropertyType):
    cluster_marker_configuration: DslValue[ClusterMarkerConfiguration] | None = None
    heatmap_configuration: DslValue[GeospatialHeatmapConfiguration] | None = None
    selected_point_style: DslValue[str] | None = None


@dataclass
class GeospatialWindowOptions(PropertyType):
    bounds: DslValue[GeospatialCoordinateBounds] | None = None
    map_zoom_mode: DslValue[str] | None = None


@dataclass
class GlobalTableBorderOptions(PropertyType):
    side_specific_border: DslValue[TableSideBorderOptions] | None = None
    uniform_border: DslValue[TableBorderOptions] | None = None


@dataclass
class GradientColor(PropertyType):
    stops: list[DslValue[GradientStop]] = field(default_factory=list)


@dataclass
class GradientStop(PropertyType):
    gradient_offset: DslValue[float] | None = None
    color: DslValue[str] | None = None
    data_value: DslValue[float] | None = None


@dataclass
class GridLayoutCanvasSizeOptions(PropertyType):
    screen_canvas_size_options: DslValue[GridLayoutScreenCanvasSizeOptions] | None = (
        None
    )


@dataclass
class GridLayoutConfiguration(PropertyType):
    elements: list[DslValue[GridLayoutElement]] = field(default_factory=list)
    canvas_size_options: DslValue[GridLayoutCanvasSizeOptions] | None = None


@dataclass
class GridLayoutElement(PropertyType):
    column_span: DslValue[float] | None = None
    element_id: DslValue[str] | None = None
    element_type: DslValue[str] | None = None
    row_span: DslValue[float] | None = None
    column_index: DslValue[float] | None = None
    row_index: DslValue[float] | None = None


@dataclass
class GridLayoutScreenCanvasSizeOptions(PropertyType):
    resize_option: DslValue[str] | None = None
    optimized_view_port_width: DslValue[str] | None = None


@dataclass
class GrowthRateComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    period_size: DslValue[float] | None = None
    time: DslValue[DimensionField] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class HeaderFooterSectionConfiguration(PropertyType):
    layout: DslValue[SectionLayoutConfiguration] | None = None
    section_id: DslValue[str] | None = None
    style: DslValue[SectionStyle] | None = None


@dataclass
class HeatMapAggregatedFieldWells(PropertyType):
    columns: list[DslValue[DimensionField]] = field(default_factory=list)
    rows: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class HeatMapConfiguration(PropertyType):
    color_scale: DslValue[ColorScale] | None = None
    column_label_options: DslValue[ChartAxisLabelOptions] | None = None
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[HeatMapFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    row_label_options: DslValue[ChartAxisLabelOptions] | None = None
    sort_configuration: DslValue[HeatMapSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None


@dataclass
class HeatMapFieldWells(PropertyType):
    heat_map_aggregated_field_wells: DslValue[HeatMapAggregatedFieldWells] | None = None


@dataclass
class HeatMapSortConfiguration(PropertyType):
    heat_map_column_items_limit_configuration: (
        DslValue[ItemsLimitConfiguration] | None
    ) = None
    heat_map_column_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    heat_map_row_items_limit_configuration: DslValue[ItemsLimitConfiguration] | None = (
        None
    )
    heat_map_row_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class HeatMapVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[HeatMapConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class HistogramAggregatedFieldWells(PropertyType):
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class HistogramBinOptions(PropertyType):
    bin_count: DslValue[BinCountOptions] | None = None
    bin_width: DslValue[BinWidthOptions] | None = None
    selected_bin_type: DslValue[str] | None = None
    start_value: DslValue[float] | None = None


@dataclass
class HistogramConfiguration(PropertyType):
    bin_options: DslValue[HistogramBinOptions] | None = None
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[HistogramFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None
    x_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    x_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    y_axis_display_options: DslValue[AxisDisplayOptions] | None = None


@dataclass
class HistogramFieldWells(PropertyType):
    histogram_aggregated_field_wells: DslValue[HistogramAggregatedFieldWells] | None = (
        None
    )


@dataclass
class HistogramVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[HistogramConfiguration] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class ImageCustomAction(PropertyType):
    action_operations: list[DslValue[ImageCustomActionOperation]] = field(
        default_factory=list
    )
    custom_action_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    trigger: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class ImageCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_operation": "URLOperation",
    }

    navigation_operation: DslValue[CustomActionNavigationOperation] | None = None
    set_parameters_operation: DslValue[CustomActionSetParametersOperation] | None = None
    url_operation: DslValue[CustomActionURLOperation] | None = None


@dataclass
class ImageInteractionOptions(PropertyType):
    image_menu_option: DslValue[ImageMenuOption] | None = None


@dataclass
class ImageMenuOption(PropertyType):
    availability_status: DslValue[str] | None = None


@dataclass
class InnerFilter(PropertyType):
    category_inner_filter: DslValue[CategoryInnerFilter] | None = None


@dataclass
class InsightConfiguration(PropertyType):
    computations: list[DslValue[Computation]] = field(default_factory=list)
    custom_narrative: DslValue[CustomNarrativeOptions] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None


@dataclass
class InsightVisual(PropertyType):
    data_set_identifier: DslValue[str] | None = None
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    insight_configuration: DslValue[InsightConfiguration] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class IntegerDefaultValues(PropertyType):
    dynamic_value: DslValue[DynamicDefaultValue] | None = None
    static_values: list[DslValue[float]] = field(default_factory=list)


@dataclass
class IntegerParameterDeclaration(PropertyType):
    name: DslValue[str] | None = None
    parameter_value_type: DslValue[str] | None = None
    default_values: DslValue[IntegerDefaultValues] | None = None
    mapped_data_set_parameters: list[DslValue[MappedDataSetParameter]] = field(
        default_factory=list
    )
    value_when_unset: DslValue[IntegerValueWhenUnsetConfiguration] | None = None


@dataclass
class IntegerValueWhenUnsetConfiguration(PropertyType):
    custom_value: DslValue[float] | None = None
    value_when_unset_option: DslValue[str] | None = None


@dataclass
class ItemsLimitConfiguration(PropertyType):
    items_limit: DslValue[float] | None = None
    other_categories: DslValue[str] | None = None


@dataclass
class KPIActualValueConditionalFormatting(PropertyType):
    icon: DslValue[ConditionalFormattingIcon] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class KPIComparisonValueConditionalFormatting(PropertyType):
    icon: DslValue[ConditionalFormattingIcon] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class KPIConditionalFormatting(PropertyType):
    conditional_formatting_options: list[DslValue[KPIConditionalFormattingOption]] = (
        field(default_factory=list)
    )


@dataclass
class KPIConditionalFormattingOption(PropertyType):
    actual_value: DslValue[KPIActualValueConditionalFormatting] | None = None
    comparison_value: DslValue[KPIComparisonValueConditionalFormatting] | None = None
    primary_value: DslValue[KPIPrimaryValueConditionalFormatting] | None = None
    progress_bar: DslValue[KPIProgressBarConditionalFormatting] | None = None


@dataclass
class KPIConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kpi_options": "KPIOptions",
    }

    field_wells: DslValue[KPIFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    kpi_options: DslValue[KPIOptions] | None = None
    sort_configuration: DslValue[KPISortConfiguration] | None = None


@dataclass
class KPIFieldWells(PropertyType):
    target_values: list[DslValue[MeasureField]] = field(default_factory=list)
    trend_groups: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class KPIOptions(PropertyType):
    comparison: DslValue[ComparisonConfiguration] | None = None
    primary_value_display_type: DslValue[str] | None = None
    primary_value_font_configuration: DslValue[FontConfiguration] | None = None
    progress_bar: DslValue[ProgressBarOptions] | None = None
    secondary_value: DslValue[SecondaryValueOptions] | None = None
    secondary_value_font_configuration: DslValue[FontConfiguration] | None = None
    sparkline: DslValue[KPISparklineOptions] | None = None
    trend_arrows: DslValue[TrendArrowOptions] | None = None
    visual_layout_options: DslValue[KPIVisualLayoutOptions] | None = None


@dataclass
class KPIPrimaryValueConditionalFormatting(PropertyType):
    icon: DslValue[ConditionalFormattingIcon] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class KPIProgressBarConditionalFormatting(PropertyType):
    foreground_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class KPISortConfiguration(PropertyType):
    trend_group_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class KPISparklineOptions(PropertyType):
    type_: DslValue[str] | None = None
    color: DslValue[str] | None = None
    tooltip_visibility: DslValue[dict[str, Any]] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class KPIVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[KPIConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    conditional_formatting: DslValue[KPIConditionalFormatting] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class KPIVisualLayoutOptions(PropertyType):
    standard_layout: DslValue[KPIVisualStandardLayout] | None = None


@dataclass
class KPIVisualStandardLayout(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class LabelOptions(PropertyType):
    custom_label: DslValue[str] | None = None
    font_configuration: DslValue[FontConfiguration] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class Layout(PropertyType):
    configuration: DslValue[LayoutConfiguration] | None = None


@dataclass
class LayoutConfiguration(PropertyType):
    free_form_layout: DslValue[FreeFormLayoutConfiguration] | None = None
    grid_layout: DslValue[GridLayoutConfiguration] | None = None
    section_based_layout: DslValue[SectionBasedLayoutConfiguration] | None = None


@dataclass
class LegendOptions(PropertyType):
    height: DslValue[str] | None = None
    position: DslValue[str] | None = None
    title: DslValue[LabelOptions] | None = None
    value_font_configuration: DslValue[FontConfiguration] | None = None
    visibility: DslValue[dict[str, Any]] | None = None
    width: DslValue[str] | None = None


@dataclass
class LineChartAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    colors: list[DslValue[DimensionField]] = field(default_factory=list)
    small_multiples: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class LineChartConfiguration(PropertyType):
    contribution_analysis_defaults: list[DslValue[ContributionAnalysisDefault]] = field(
        default_factory=list
    )
    data_labels: DslValue[DataLabelOptions] | None = None
    default_series_settings: DslValue[LineChartDefaultSeriesSettings] | None = None
    field_wells: DslValue[LineChartFieldWells] | None = None
    forecast_configurations: list[DslValue[ForecastConfiguration]] = field(
        default_factory=list
    )
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    primary_y_axis_display_options: DslValue[LineSeriesAxisDisplayOptions] | None = None
    primary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    reference_lines: list[DslValue[ReferenceLine]] = field(default_factory=list)
    secondary_y_axis_display_options: DslValue[LineSeriesAxisDisplayOptions] | None = (
        None
    )
    secondary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    series: list[DslValue[SeriesItem]] = field(default_factory=list)
    single_axis_options: DslValue[SingleAxisOptions] | None = None
    small_multiples_options: DslValue[SmallMultiplesOptions] | None = None
    sort_configuration: DslValue[LineChartSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    type_: DslValue[str] | None = None
    visual_palette: DslValue[VisualPalette] | None = None
    x_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    x_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None


@dataclass
class LineChartDefaultSeriesSettings(PropertyType):
    axis_binding: DslValue[str] | None = None
    line_style_settings: DslValue[LineChartLineStyleSettings] | None = None
    marker_style_settings: DslValue[LineChartMarkerStyleSettings] | None = None


@dataclass
class LineChartFieldWells(PropertyType):
    line_chart_aggregated_field_wells: (
        DslValue[LineChartAggregatedFieldWells] | None
    ) = None


@dataclass
class LineChartLineStyleSettings(PropertyType):
    line_interpolation: DslValue[str] | None = None
    line_style: DslValue[str] | None = None
    line_visibility: DslValue[dict[str, Any]] | None = None
    line_width: DslValue[str] | None = None


@dataclass
class LineChartMarkerStyleSettings(PropertyType):
    marker_color: DslValue[str] | None = None
    marker_shape: DslValue[str] | None = None
    marker_size: DslValue[str] | None = None
    marker_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class LineChartSeriesSettings(PropertyType):
    line_style_settings: DslValue[LineChartLineStyleSettings] | None = None
    marker_style_settings: DslValue[LineChartMarkerStyleSettings] | None = None


@dataclass
class LineChartSortConfiguration(PropertyType):
    category_items_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    color_items_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None
    small_multiples_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None
    small_multiples_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class LineChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[LineChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class LineSeriesAxisDisplayOptions(PropertyType):
    axis_options: DslValue[AxisDisplayOptions] | None = None
    missing_data_configurations: list[DslValue[MissingDataConfiguration]] = field(
        default_factory=list
    )


@dataclass
class ListControlDisplayOptions(PropertyType):
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    search_options: DslValue[ListControlSearchOptions] | None = None
    select_all_options: DslValue[ListControlSelectAllOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class ListControlSearchOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class ListControlSelectAllOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class LoadingAnimation(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class LocalNavigationConfiguration(PropertyType):
    target_sheet_id: DslValue[str] | None = None


@dataclass
class LongFormatText(PropertyType):
    plain_text: DslValue[str] | None = None
    rich_text: DslValue[str] | None = None


@dataclass
class MappedDataSetParameter(PropertyType):
    data_set_identifier: DslValue[str] | None = None
    data_set_parameter_name: DslValue[str] | None = None


@dataclass
class MaximumLabelType(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class MaximumMinimumComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    name: DslValue[str] | None = None
    time: DslValue[DimensionField] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class MeasureField(PropertyType):
    calculated_measure_field: DslValue[CalculatedMeasureField] | None = None
    categorical_measure_field: DslValue[CategoricalMeasureField] | None = None
    date_measure_field: DslValue[DateMeasureField] | None = None
    numerical_measure_field: DslValue[NumericalMeasureField] | None = None


@dataclass
class MetricComparisonComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    from_value: DslValue[MeasureField] | None = None
    name: DslValue[str] | None = None
    target_value: DslValue[MeasureField] | None = None
    time: DslValue[DimensionField] | None = None


@dataclass
class MinimumLabelType(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class MissingDataConfiguration(PropertyType):
    treatment_option: DslValue[str] | None = None


@dataclass
class NegativeValueConfiguration(PropertyType):
    display_mode: DslValue[str] | None = None


@dataclass
class NestedFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    include_inner_set: DslValue[bool] | None = None
    inner_filter: DslValue[InnerFilter] | None = None


@dataclass
class NullValueFormatConfiguration(PropertyType):
    null_string: DslValue[str] | None = None


@dataclass
class NumberDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DslValue[DecimalPlacesConfiguration] | None = None
    negative_value_configuration: DslValue[NegativeValueConfiguration] | None = None
    null_value_format_configuration: DslValue[NullValueFormatConfiguration] | None = (
        None
    )
    number_scale: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    separator_configuration: DslValue[NumericSeparatorConfiguration] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class NumberFormatConfiguration(PropertyType):
    format_configuration: DslValue[NumericFormatConfiguration] | None = None


@dataclass
class NumericAxisOptions(PropertyType):
    range: DslValue[AxisDisplayRange] | None = None
    scale: DslValue[AxisScale] | None = None


@dataclass
class NumericEqualityDrillDownFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    value: DslValue[float] | None = None


@dataclass
class NumericEqualityFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    match_operator: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    aggregation_function: DslValue[AggregationFunction] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    parameter_name: DslValue[str] | None = None
    select_all_options: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class NumericFormatConfiguration(PropertyType):
    currency_display_format_configuration: (
        DslValue[CurrencyDisplayFormatConfiguration] | None
    ) = None
    number_display_format_configuration: (
        DslValue[NumberDisplayFormatConfiguration] | None
    ) = None
    percentage_display_format_configuration: (
        DslValue[PercentageDisplayFormatConfiguration] | None
    ) = None


@dataclass
class NumericRangeFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    aggregation_function: DslValue[AggregationFunction] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    include_maximum: DslValue[bool] | None = None
    include_minimum: DslValue[bool] | None = None
    range_maximum: DslValue[NumericRangeFilterValue] | None = None
    range_minimum: DslValue[NumericRangeFilterValue] | None = None
    select_all_options: DslValue[str] | None = None


@dataclass
class NumericRangeFilterValue(PropertyType):
    parameter: DslValue[str] | None = None
    static_value: DslValue[float] | None = None


@dataclass
class NumericSeparatorConfiguration(PropertyType):
    decimal_separator: DslValue[str] | None = None
    thousands_separator: DslValue[ThousandSeparatorOptions] | None = None


@dataclass
class NumericalAggregationFunction(PropertyType):
    percentile_aggregation: DslValue[PercentileAggregation] | None = None
    simple_numerical_aggregation: DslValue[str] | None = None


@dataclass
class NumericalDimensionField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    format_configuration: DslValue[NumberFormatConfiguration] | None = None
    hierarchy_id: DslValue[str] | None = None


@dataclass
class NumericalMeasureField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    aggregation_function: DslValue[NumericalAggregationFunction] | None = None
    format_configuration: DslValue[NumberFormatConfiguration] | None = None


@dataclass
class PaginationConfiguration(PropertyType):
    page_number: DslValue[float] | None = None
    page_size: DslValue[float] | None = None


@dataclass
class PanelConfiguration(PropertyType):
    background_color: DslValue[str] | None = None
    background_visibility: DslValue[dict[str, Any]] | None = None
    border_color: DslValue[str] | None = None
    border_style: DslValue[str] | None = None
    border_thickness: DslValue[str] | None = None
    border_visibility: DslValue[dict[str, Any]] | None = None
    gutter_spacing: DslValue[str] | None = None
    gutter_visibility: DslValue[dict[str, Any]] | None = None
    title: DslValue[PanelTitleOptions] | None = None


@dataclass
class PanelTitleOptions(PropertyType):
    font_configuration: DslValue[FontConfiguration] | None = None
    horizontal_text_alignment: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class ParameterControl(PropertyType):
    date_time_picker: DslValue[ParameterDateTimePickerControl] | None = None
    dropdown: DslValue[ParameterDropDownControl] | None = None
    list: DslValue[ParameterListControl] | None = None
    slider: DslValue[ParameterSliderControl] | None = None
    text_area: DslValue[ParameterTextAreaControl] | None = None
    text_field: DslValue[ParameterTextFieldControl] | None = None


@dataclass
class ParameterDateTimePickerControl(PropertyType):
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    title: DslValue[str] | None = None
    display_options: DslValue[DateTimePickerControlDisplayOptions] | None = None


@dataclass
class ParameterDeclaration(PropertyType):
    date_time_parameter_declaration: DslValue[DateTimeParameterDeclaration] | None = (
        None
    )
    decimal_parameter_declaration: DslValue[DecimalParameterDeclaration] | None = None
    integer_parameter_declaration: DslValue[IntegerParameterDeclaration] | None = None
    string_parameter_declaration: DslValue[StringParameterDeclaration] | None = None


@dataclass
class ParameterDropDownControl(PropertyType):
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    title: DslValue[str] | None = None
    cascading_control_configuration: DslValue[CascadingControlConfiguration] | None = (
        None
    )
    commit_mode: DslValue[str] | None = None
    display_options: DslValue[DropDownControlDisplayOptions] | None = None
    selectable_values: DslValue[ParameterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ParameterListControl(PropertyType):
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    title: DslValue[str] | None = None
    cascading_control_configuration: DslValue[CascadingControlConfiguration] | None = (
        None
    )
    display_options: DslValue[ListControlDisplayOptions] | None = None
    selectable_values: DslValue[ParameterSelectableValues] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ParameterSelectableValues(PropertyType):
    link_to_data_set_column: DslValue[ColumnIdentifier] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ParameterSliderControl(PropertyType):
    maximum_value: DslValue[float] | None = None
    minimum_value: DslValue[float] | None = None
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    step_size: DslValue[float] | None = None
    title: DslValue[str] | None = None
    display_options: DslValue[SliderControlDisplayOptions] | None = None


@dataclass
class ParameterTextAreaControl(PropertyType):
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    title: DslValue[str] | None = None
    delimiter: DslValue[str] | None = None
    display_options: DslValue[TextAreaControlDisplayOptions] | None = None


@dataclass
class ParameterTextFieldControl(PropertyType):
    parameter_control_id: DslValue[str] | None = None
    source_parameter_name: DslValue[str] | None = None
    title: DslValue[str] | None = None
    display_options: DslValue[TextFieldControlDisplayOptions] | None = None


@dataclass
class PercentVisibleRange(PropertyType):
    from_: DslValue[float] | None = None
    to: DslValue[float] | None = None


@dataclass
class PercentageDisplayFormatConfiguration(PropertyType):
    decimal_places_configuration: DslValue[DecimalPlacesConfiguration] | None = None
    negative_value_configuration: DslValue[NegativeValueConfiguration] | None = None
    null_value_format_configuration: DslValue[NullValueFormatConfiguration] | None = (
        None
    )
    prefix: DslValue[str] | None = None
    separator_configuration: DslValue[NumericSeparatorConfiguration] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class PercentileAggregation(PropertyType):
    percentile_value: DslValue[float] | None = None


@dataclass
class PeriodOverPeriodComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    time: DslValue[DimensionField] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class PeriodToDateComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    period_time_granularity: DslValue[str] | None = None
    time: DslValue[DimensionField] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class PieChartAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    small_multiples: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class PieChartConfiguration(PropertyType):
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    contribution_analysis_defaults: list[DslValue[ContributionAnalysisDefault]] = field(
        default_factory=list
    )
    data_labels: DslValue[DataLabelOptions] | None = None
    donut_options: DslValue[DonutOptions] | None = None
    field_wells: DslValue[PieChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    small_multiples_options: DslValue[SmallMultiplesOptions] | None = None
    sort_configuration: DslValue[PieChartSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    value_label_options: DslValue[ChartAxisLabelOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class PieChartFieldWells(PropertyType):
    pie_chart_aggregated_field_wells: DslValue[PieChartAggregatedFieldWells] | None = (
        None
    )


@dataclass
class PieChartSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    small_multiples_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None
    small_multiples_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class PieChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[PieChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class PivotFieldSortOptions(PropertyType):
    field_id: DslValue[str] | None = None
    sort_by: DslValue[PivotTableSortBy] | None = None


@dataclass
class PivotTableAggregatedFieldWells(PropertyType):
    columns: list[DslValue[DimensionField]] = field(default_factory=list)
    rows: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class PivotTableCellConditionalFormatting(PropertyType):
    field_id: DslValue[str] | None = None
    scope: DslValue[PivotTableConditionalFormattingScope] | None = None
    scopes: list[DslValue[PivotTableConditionalFormattingScope]] = field(
        default_factory=list
    )
    text_format: DslValue[TextConditionalFormat] | None = None


@dataclass
class PivotTableConditionalFormatting(PropertyType):
    conditional_formatting_options: list[
        DslValue[PivotTableConditionalFormattingOption]
    ] = field(default_factory=list)


@dataclass
class PivotTableConditionalFormattingOption(PropertyType):
    cell: DslValue[PivotTableCellConditionalFormatting] | None = None


@dataclass
class PivotTableConditionalFormattingScope(PropertyType):
    role: DslValue[str] | None = None


@dataclass
class PivotTableConfiguration(PropertyType):
    field_options: DslValue[PivotTableFieldOptions] | None = None
    field_wells: DslValue[PivotTableFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    paginated_report_options: DslValue[PivotTablePaginatedReportOptions] | None = None
    sort_configuration: DslValue[PivotTableSortConfiguration] | None = None
    table_options: DslValue[PivotTableOptions] | None = None
    total_options: DslValue[PivotTableTotalOptions] | None = None


@dataclass
class PivotTableDataPathOption(PropertyType):
    data_path_list: list[DslValue[DataPathValue]] = field(default_factory=list)
    width: DslValue[str] | None = None


@dataclass
class PivotTableFieldCollapseStateOption(PropertyType):
    target: DslValue[PivotTableFieldCollapseStateTarget] | None = None
    state: DslValue[str] | None = None


@dataclass
class PivotTableFieldCollapseStateTarget(PropertyType):
    field_data_path_values: list[DslValue[DataPathValue]] = field(default_factory=list)
    field_id: DslValue[str] | None = None


@dataclass
class PivotTableFieldOption(PropertyType):
    field_id: DslValue[str] | None = None
    custom_label: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class PivotTableFieldOptions(PropertyType):
    collapse_state_options: list[DslValue[PivotTableFieldCollapseStateOption]] = field(
        default_factory=list
    )
    data_path_options: list[DslValue[PivotTableDataPathOption]] = field(
        default_factory=list
    )
    selected_field_options: list[DslValue[PivotTableFieldOption]] = field(
        default_factory=list
    )


@dataclass
class PivotTableFieldSubtotalOptions(PropertyType):
    field_id: DslValue[str] | None = None


@dataclass
class PivotTableFieldWells(PropertyType):
    pivot_table_aggregated_field_wells: (
        DslValue[PivotTableAggregatedFieldWells] | None
    ) = None


@dataclass
class PivotTableOptions(PropertyType):
    cell_style: DslValue[TableCellStyle] | None = None
    collapsed_row_dimensions_visibility: DslValue[dict[str, Any]] | None = None
    column_header_style: DslValue[TableCellStyle] | None = None
    column_names_visibility: DslValue[dict[str, Any]] | None = None
    default_cell_width: DslValue[str] | None = None
    metric_placement: DslValue[str] | None = None
    row_alternate_color_options: DslValue[RowAlternateColorOptions] | None = None
    row_field_names_style: DslValue[TableCellStyle] | None = None
    row_header_style: DslValue[TableCellStyle] | None = None
    rows_label_options: DslValue[PivotTableRowsLabelOptions] | None = None
    rows_layout: DslValue[str] | None = None
    single_metric_visibility: DslValue[dict[str, Any]] | None = None
    toggle_buttons_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class PivotTablePaginatedReportOptions(PropertyType):
    overflow_column_header_visibility: DslValue[dict[str, Any]] | None = None
    vertical_overflow_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class PivotTableRowsLabelOptions(PropertyType):
    custom_label: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class PivotTableSortBy(PropertyType):
    column: DslValue[ColumnSort] | None = None
    data_path: DslValue[DataPathSort] | None = None
    field_: DslValue[FieldSort] | None = None


@dataclass
class PivotTableSortConfiguration(PropertyType):
    field_sort_options: list[DslValue[PivotFieldSortOptions]] = field(
        default_factory=list
    )


@dataclass
class PivotTableTotalOptions(PropertyType):
    column_subtotal_options: DslValue[SubtotalOptions] | None = None
    column_total_options: DslValue[PivotTotalOptions] | None = None
    row_subtotal_options: DslValue[SubtotalOptions] | None = None
    row_total_options: DslValue[PivotTotalOptions] | None = None


@dataclass
class PivotTableVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[PivotTableConfiguration] | None = None
    conditional_formatting: DslValue[PivotTableConditionalFormatting] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class PivotTotalOptions(PropertyType):
    custom_label: DslValue[str] | None = None
    metric_header_cell_style: DslValue[TableCellStyle] | None = None
    placement: DslValue[str] | None = None
    scroll_status: DslValue[str] | None = None
    total_aggregation_options: list[DslValue[TotalAggregationOption]] = field(
        default_factory=list
    )
    total_cell_style: DslValue[TableCellStyle] | None = None
    totals_visibility: DslValue[dict[str, Any]] | None = None
    value_cell_style: DslValue[TableCellStyle] | None = None


@dataclass
class PluginVisual(PropertyType):
    plugin_arn: DslValue[str] | None = None
    visual_id: DslValue[str] | None = None
    chart_configuration: DslValue[PluginVisualConfiguration] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class PluginVisualConfiguration(PropertyType):
    field_wells: list[DslValue[PluginVisualFieldWell]] = field(default_factory=list)
    sort_configuration: DslValue[PluginVisualSortConfiguration] | None = None
    visual_options: DslValue[PluginVisualOptions] | None = None


@dataclass
class PluginVisualFieldWell(PropertyType):
    axis_name: DslValue[str] | None = None
    dimensions: list[DslValue[DimensionField]] = field(default_factory=list)
    measures: list[DslValue[MeasureField]] = field(default_factory=list)
    unaggregated: list[DslValue[UnaggregatedField]] = field(default_factory=list)


@dataclass
class PluginVisualItemsLimitConfiguration(PropertyType):
    items_limit: DslValue[float] | None = None


@dataclass
class PluginVisualOptions(PropertyType):
    visual_properties: list[DslValue[PluginVisualProperty]] = field(
        default_factory=list
    )


@dataclass
class PluginVisualProperty(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class PluginVisualSortConfiguration(PropertyType):
    plugin_visual_table_query_sort: DslValue[PluginVisualTableQuerySort] | None = None


@dataclass
class PluginVisualTableQuerySort(PropertyType):
    items_limit_configuration: DslValue[PluginVisualItemsLimitConfiguration] | None = (
        None
    )
    row_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class PredefinedHierarchy(PropertyType):
    columns: list[DslValue[ColumnIdentifier]] = field(default_factory=list)
    hierarchy_id: DslValue[str] | None = None
    drill_down_filters: list[DslValue[DrillDownFilter]] = field(default_factory=list)


@dataclass
class ProgressBarOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class QueryExecutionOptions(PropertyType):
    query_execution_mode: DslValue[str] | None = None


@dataclass
class RadarChartAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    color: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class RadarChartAreaStyleSettings(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class RadarChartConfiguration(PropertyType):
    alternate_band_colors_visibility: DslValue[dict[str, Any]] | None = None
    alternate_band_even_color: DslValue[str] | None = None
    alternate_band_odd_color: DslValue[str] | None = None
    axes_range_scale: DslValue[str] | None = None
    base_series_settings: DslValue[RadarChartSeriesSettings] | None = None
    category_axis: DslValue[AxisDisplayOptions] | None = None
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    color_axis: DslValue[AxisDisplayOptions] | None = None
    color_label_options: DslValue[ChartAxisLabelOptions] | None = None
    field_wells: DslValue[RadarChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    shape: DslValue[str] | None = None
    sort_configuration: DslValue[RadarChartSortConfiguration] | None = None
    start_angle: DslValue[float] | None = None
    visual_palette: DslValue[VisualPalette] | None = None


@dataclass
class RadarChartFieldWells(PropertyType):
    radar_chart_aggregated_field_wells: (
        DslValue[RadarChartAggregatedFieldWells] | None
    ) = None


@dataclass
class RadarChartSeriesSettings(PropertyType):
    area_style_settings: DslValue[RadarChartAreaStyleSettings] | None = None


@dataclass
class RadarChartSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)
    color_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    color_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class RadarChartVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[RadarChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class RangeEndsLabelType(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class ReferenceLine(PropertyType):
    data_configuration: DslValue[ReferenceLineDataConfiguration] | None = None
    label_configuration: DslValue[ReferenceLineLabelConfiguration] | None = None
    status: DslValue[str] | None = None
    style_configuration: DslValue[ReferenceLineStyleConfiguration] | None = None


@dataclass
class ReferenceLineCustomLabelConfiguration(PropertyType):
    custom_label: DslValue[str] | None = None


@dataclass
class ReferenceLineDataConfiguration(PropertyType):
    axis_binding: DslValue[str] | None = None
    dynamic_configuration: DslValue[ReferenceLineDynamicDataConfiguration] | None = None
    series_type: DslValue[str] | None = None
    static_configuration: DslValue[ReferenceLineStaticDataConfiguration] | None = None


@dataclass
class ReferenceLineDynamicDataConfiguration(PropertyType):
    calculation: DslValue[NumericalAggregationFunction] | None = None
    column: DslValue[ColumnIdentifier] | None = None
    measure_aggregation_function: DslValue[AggregationFunction] | None = None


@dataclass
class ReferenceLineLabelConfiguration(PropertyType):
    custom_label_configuration: (
        DslValue[ReferenceLineCustomLabelConfiguration] | None
    ) = None
    font_color: DslValue[str] | None = None
    font_configuration: DslValue[FontConfiguration] | None = None
    horizontal_position: DslValue[str] | None = None
    value_label_configuration: DslValue[ReferenceLineValueLabelConfiguration] | None = (
        None
    )
    vertical_position: DslValue[str] | None = None


@dataclass
class ReferenceLineStaticDataConfiguration(PropertyType):
    value: DslValue[float] | None = None


@dataclass
class ReferenceLineStyleConfiguration(PropertyType):
    color: DslValue[str] | None = None
    pattern: DslValue[str] | None = None


@dataclass
class ReferenceLineValueLabelConfiguration(PropertyType):
    format_configuration: DslValue[NumericFormatConfiguration] | None = None
    relative_position: DslValue[str] | None = None


@dataclass
class RelativeDateTimeControlDisplayOptions(PropertyType):
    date_time_format: DslValue[str] | None = None
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class RelativeDatesFilter(PropertyType):
    anchor_date_configuration: DslValue[AnchorDateConfiguration] | None = None
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    relative_date_type: DslValue[str] | None = None
    time_granularity: DslValue[str] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    exclude_period_configuration: DslValue[ExcludePeriodConfiguration] | None = None
    minimum_granularity: DslValue[str] | None = None
    parameter_name: DslValue[str] | None = None
    relative_date_value: DslValue[float] | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[str] | None = None


@dataclass
class RollingDateConfiguration(PropertyType):
    expression: DslValue[str] | None = None
    data_set_identifier: DslValue[str] | None = None


@dataclass
class RowAlternateColorOptions(PropertyType):
    row_alternate_colors: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    use_primary_background_color: DslValue[str] | None = None


@dataclass
class SameSheetTargetVisualConfiguration(PropertyType):
    target_visual_options: DslValue[str] | None = None
    target_visuals: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SankeyDiagramAggregatedFieldWells(PropertyType):
    destination: list[DslValue[DimensionField]] = field(default_factory=list)
    source: list[DslValue[DimensionField]] = field(default_factory=list)
    weight: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class SankeyDiagramChartConfiguration(PropertyType):
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[SankeyDiagramFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    sort_configuration: DslValue[SankeyDiagramSortConfiguration] | None = None


@dataclass
class SankeyDiagramFieldWells(PropertyType):
    sankey_diagram_aggregated_field_wells: (
        DslValue[SankeyDiagramAggregatedFieldWells] | None
    ) = None


@dataclass
class SankeyDiagramSortConfiguration(PropertyType):
    destination_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    source_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    weight_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class SankeyDiagramVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[SankeyDiagramChartConfiguration] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class ScatterPlotCategoricallyAggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    label: list[DslValue[DimensionField]] = field(default_factory=list)
    size: list[DslValue[MeasureField]] = field(default_factory=list)
    x_axis: list[DslValue[MeasureField]] = field(default_factory=list)
    y_axis: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class ScatterPlotConfiguration(PropertyType):
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[ScatterPlotFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    sort_configuration: DslValue[ScatterPlotSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None
    visual_palette: DslValue[VisualPalette] | None = None
    x_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    x_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    y_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None


@dataclass
class ScatterPlotFieldWells(PropertyType):
    scatter_plot_categorically_aggregated_field_wells: (
        DslValue[ScatterPlotCategoricallyAggregatedFieldWells] | None
    ) = None
    scatter_plot_unaggregated_field_wells: (
        DslValue[ScatterPlotUnaggregatedFieldWells] | None
    ) = None


@dataclass
class ScatterPlotSortConfiguration(PropertyType):
    scatter_plot_limit_configuration: DslValue[ItemsLimitConfiguration] | None = None


@dataclass
class ScatterPlotUnaggregatedFieldWells(PropertyType):
    category: list[DslValue[DimensionField]] = field(default_factory=list)
    label: list[DslValue[DimensionField]] = field(default_factory=list)
    size: list[DslValue[MeasureField]] = field(default_factory=list)
    x_axis: list[DslValue[DimensionField]] = field(default_factory=list)
    y_axis: list[DslValue[DimensionField]] = field(default_factory=list)


@dataclass
class ScatterPlotVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[ScatterPlotConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class ScrollBarOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None
    visible_range: DslValue[VisibleRangeOptions] | None = None


@dataclass
class SecondaryValueOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class SectionAfterPageBreak(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class SectionBasedLayoutCanvasSizeOptions(PropertyType):
    paper_canvas_size_options: (
        DslValue[SectionBasedLayoutPaperCanvasSizeOptions] | None
    ) = None


@dataclass
class SectionBasedLayoutConfiguration(PropertyType):
    body_sections: list[DslValue[BodySectionConfiguration]] = field(
        default_factory=list
    )
    canvas_size_options: DslValue[SectionBasedLayoutCanvasSizeOptions] | None = None
    footer_sections: list[DslValue[HeaderFooterSectionConfiguration]] = field(
        default_factory=list
    )
    header_sections: list[DslValue[HeaderFooterSectionConfiguration]] = field(
        default_factory=list
    )


@dataclass
class SectionBasedLayoutPaperCanvasSizeOptions(PropertyType):
    paper_margin: DslValue[Spacing] | None = None
    paper_orientation: DslValue[str] | None = None
    paper_size: DslValue[str] | None = None


@dataclass
class SectionLayoutConfiguration(PropertyType):
    free_form_layout: DslValue[FreeFormSectionLayoutConfiguration] | None = None


@dataclass
class SectionPageBreakConfiguration(PropertyType):
    after: DslValue[SectionAfterPageBreak] | None = None


@dataclass
class SectionStyle(PropertyType):
    height: DslValue[str] | None = None
    padding: DslValue[Spacing] | None = None


@dataclass
class SelectedSheetsFilterScopeConfiguration(PropertyType):
    sheet_visual_scoping_configurations: list[
        DslValue[SheetVisualScopingConfiguration]
    ] = field(default_factory=list)


@dataclass
class SeriesItem(PropertyType):
    data_field_series_item: DslValue[DataFieldSeriesItem] | None = None
    field_series_item: DslValue[FieldSeriesItem] | None = None


@dataclass
class SetParameterValueConfiguration(PropertyType):
    destination_parameter_name: DslValue[str] | None = None
    value: DslValue[DestinationParameterValueConfiguration] | None = None


@dataclass
class ShapeConditionalFormat(PropertyType):
    background_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class Sheet(PropertyType):
    name: DslValue[str] | None = None
    sheet_id: DslValue[str] | None = None


@dataclass
class SheetControlInfoIconLabelOptions(PropertyType):
    info_icon_text: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class SheetControlLayout(PropertyType):
    configuration: DslValue[SheetControlLayoutConfiguration] | None = None


@dataclass
class SheetControlLayoutConfiguration(PropertyType):
    grid_layout: DslValue[GridLayoutConfiguration] | None = None


@dataclass
class SheetDefinition(PropertyType):
    sheet_id: DslValue[str] | None = None
    content_type: DslValue[str] | None = None
    description: DslValue[str] | None = None
    filter_controls: list[DslValue[FilterControl]] = field(default_factory=list)
    images: list[DslValue[SheetImage]] = field(default_factory=list)
    layouts: list[DslValue[Layout]] = field(default_factory=list)
    name: DslValue[str] | None = None
    parameter_controls: list[DslValue[ParameterControl]] = field(default_factory=list)
    sheet_control_layouts: list[DslValue[SheetControlLayout]] = field(
        default_factory=list
    )
    text_boxes: list[DslValue[SheetTextBox]] = field(default_factory=list)
    title: DslValue[str] | None = None
    visuals: list[DslValue[Visual]] = field(default_factory=list)


@dataclass
class SheetElementConfigurationOverrides(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class SheetElementRenderingRule(PropertyType):
    configuration_overrides: DslValue[SheetElementConfigurationOverrides] | None = None
    expression: DslValue[str] | None = None


@dataclass
class SheetImage(PropertyType):
    sheet_image_id: DslValue[str] | None = None
    source: DslValue[SheetImageSource] | None = None
    actions: list[DslValue[ImageCustomAction]] = field(default_factory=list)
    image_content_alt_text: DslValue[str] | None = None
    interactions: DslValue[ImageInteractionOptions] | None = None
    scaling: DslValue[SheetImageScalingConfiguration] | None = None
    tooltip: DslValue[SheetImageTooltipConfiguration] | None = None


@dataclass
class SheetImageScalingConfiguration(PropertyType):
    scaling_type: DslValue[str] | None = None


@dataclass
class SheetImageSource(PropertyType):
    sheet_image_static_file_source: DslValue[SheetImageStaticFileSource] | None = None


@dataclass
class SheetImageStaticFileSource(PropertyType):
    static_file_id: DslValue[str] | None = None


@dataclass
class SheetImageTooltipConfiguration(PropertyType):
    tooltip_text: DslValue[SheetImageTooltipText] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class SheetImageTooltipText(PropertyType):
    plain_text: DslValue[str] | None = None


@dataclass
class SheetTextBox(PropertyType):
    sheet_text_box_id: DslValue[str] | None = None
    content: DslValue[str] | None = None


@dataclass
class SheetVisualScopingConfiguration(PropertyType):
    scope: DslValue[str] | None = None
    sheet_id: DslValue[str] | None = None
    visual_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ShortFormatText(PropertyType):
    plain_text: DslValue[str] | None = None
    rich_text: DslValue[str] | None = None


@dataclass
class SimpleClusterMarker(PropertyType):
    color: DslValue[str] | None = None


@dataclass
class SingleAxisOptions(PropertyType):
    y_axis_options: DslValue[YAxisOptions] | None = None


@dataclass
class SliderControlDisplayOptions(PropertyType):
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class SmallMultiplesAxisProperties(PropertyType):
    placement: DslValue[str] | None = None
    scale: DslValue[str] | None = None


@dataclass
class SmallMultiplesOptions(PropertyType):
    max_visible_columns: DslValue[float] | None = None
    max_visible_rows: DslValue[float] | None = None
    panel_configuration: DslValue[PanelConfiguration] | None = None
    x_axis: DslValue[SmallMultiplesAxisProperties] | None = None
    y_axis: DslValue[SmallMultiplesAxisProperties] | None = None


@dataclass
class Spacing(PropertyType):
    bottom: DslValue[str] | None = None
    left: DslValue[str] | None = None
    right: DslValue[str] | None = None
    top: DslValue[str] | None = None


@dataclass
class StringDefaultValues(PropertyType):
    dynamic_value: DslValue[DynamicDefaultValue] | None = None
    static_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StringFormatConfiguration(PropertyType):
    null_value_format_configuration: DslValue[NullValueFormatConfiguration] | None = (
        None
    )
    numeric_format_configuration: DslValue[NumericFormatConfiguration] | None = None


@dataclass
class StringParameterDeclaration(PropertyType):
    name: DslValue[str] | None = None
    parameter_value_type: DslValue[str] | None = None
    default_values: DslValue[StringDefaultValues] | None = None
    mapped_data_set_parameters: list[DslValue[MappedDataSetParameter]] = field(
        default_factory=list
    )
    value_when_unset: DslValue[StringValueWhenUnsetConfiguration] | None = None


@dataclass
class StringValueWhenUnsetConfiguration(PropertyType):
    custom_value: DslValue[str] | None = None
    value_when_unset_option: DslValue[str] | None = None


@dataclass
class SubtotalOptions(PropertyType):
    custom_label: DslValue[str] | None = None
    field_level: DslValue[str] | None = None
    field_level_options: list[DslValue[PivotTableFieldSubtotalOptions]] = field(
        default_factory=list
    )
    metric_header_cell_style: DslValue[TableCellStyle] | None = None
    style_targets: list[DslValue[TableStyleTarget]] = field(default_factory=list)
    total_cell_style: DslValue[TableCellStyle] | None = None
    totals_visibility: DslValue[dict[str, Any]] | None = None
    value_cell_style: DslValue[TableCellStyle] | None = None


@dataclass
class TableAggregatedFieldWells(PropertyType):
    group_by: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class TableBorderOptions(PropertyType):
    color: DslValue[str] | None = None
    style: DslValue[str] | None = None
    thickness: DslValue[float] | None = None


@dataclass
class TableCellConditionalFormatting(PropertyType):
    field_id: DslValue[str] | None = None
    text_format: DslValue[TextConditionalFormat] | None = None


@dataclass
class TableCellImageSizingConfiguration(PropertyType):
    table_cell_image_scaling_configuration: DslValue[str] | None = None


@dataclass
class TableCellStyle(PropertyType):
    background_color: DslValue[str] | None = None
    border: DslValue[GlobalTableBorderOptions] | None = None
    font_configuration: DslValue[FontConfiguration] | None = None
    height: DslValue[float] | None = None
    horizontal_text_alignment: DslValue[str] | None = None
    text_wrap: DslValue[str] | None = None
    vertical_text_alignment: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TableConditionalFormatting(PropertyType):
    conditional_formatting_options: list[DslValue[TableConditionalFormattingOption]] = (
        field(default_factory=list)
    )


@dataclass
class TableConditionalFormattingOption(PropertyType):
    cell: DslValue[TableCellConditionalFormatting] | None = None
    row: DslValue[TableRowConditionalFormatting] | None = None


@dataclass
class TableConfiguration(PropertyType):
    field_options: DslValue[TableFieldOptions] | None = None
    field_wells: DslValue[TableFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    paginated_report_options: DslValue[TablePaginatedReportOptions] | None = None
    sort_configuration: DslValue[TableSortConfiguration] | None = None
    table_inline_visualizations: list[DslValue[TableInlineVisualization]] = field(
        default_factory=list
    )
    table_options: DslValue[TableOptions] | None = None
    total_options: DslValue[TotalOptions] | None = None


@dataclass
class TableFieldCustomIconContent(PropertyType):
    icon: DslValue[str] | None = None


@dataclass
class TableFieldCustomTextContent(PropertyType):
    font_configuration: DslValue[FontConfiguration] | None = None
    value: DslValue[str] | None = None


@dataclass
class TableFieldImageConfiguration(PropertyType):
    sizing_options: DslValue[TableCellImageSizingConfiguration] | None = None


@dataclass
class TableFieldLinkConfiguration(PropertyType):
    content: DslValue[TableFieldLinkContentConfiguration] | None = None
    target: DslValue[str] | None = None


@dataclass
class TableFieldLinkContentConfiguration(PropertyType):
    custom_icon_content: DslValue[TableFieldCustomIconContent] | None = None
    custom_text_content: DslValue[TableFieldCustomTextContent] | None = None


@dataclass
class TableFieldOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_styling": "URLStyling",
    }

    field_id: DslValue[str] | None = None
    custom_label: DslValue[str] | None = None
    url_styling: DslValue[TableFieldURLConfiguration] | None = None
    visibility: DslValue[dict[str, Any]] | None = None
    width: DslValue[str] | None = None


@dataclass
class TableFieldOptions(PropertyType):
    order: list[DslValue[str]] = field(default_factory=list)
    pinned_field_options: DslValue[TablePinnedFieldOptions] | None = None
    selected_field_options: list[DslValue[TableFieldOption]] = field(
        default_factory=list
    )
    transposed_table_options: list[DslValue[TransposedTableOption]] = field(
        default_factory=list
    )


@dataclass
class TableFieldURLConfiguration(PropertyType):
    image_configuration: DslValue[TableFieldImageConfiguration] | None = None
    link_configuration: DslValue[TableFieldLinkConfiguration] | None = None


@dataclass
class TableFieldWells(PropertyType):
    table_aggregated_field_wells: DslValue[TableAggregatedFieldWells] | None = None
    table_unaggregated_field_wells: DslValue[TableUnaggregatedFieldWells] | None = None


@dataclass
class TableInlineVisualization(PropertyType):
    data_bars: DslValue[DataBarsOptions] | None = None


@dataclass
class TableOptions(PropertyType):
    cell_style: DslValue[TableCellStyle] | None = None
    header_style: DslValue[TableCellStyle] | None = None
    orientation: DslValue[str] | None = None
    row_alternate_color_options: DslValue[RowAlternateColorOptions] | None = None


@dataclass
class TablePaginatedReportOptions(PropertyType):
    overflow_column_header_visibility: DslValue[dict[str, Any]] | None = None
    vertical_overflow_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TablePinnedFieldOptions(PropertyType):
    pinned_left_fields: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TableRowConditionalFormatting(PropertyType):
    background_color: DslValue[ConditionalFormattingColor] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class TableSideBorderOptions(PropertyType):
    bottom: DslValue[TableBorderOptions] | None = None
    inner_horizontal: DslValue[TableBorderOptions] | None = None
    inner_vertical: DslValue[TableBorderOptions] | None = None
    left: DslValue[TableBorderOptions] | None = None
    right: DslValue[TableBorderOptions] | None = None
    top: DslValue[TableBorderOptions] | None = None


@dataclass
class TableSortConfiguration(PropertyType):
    pagination_configuration: DslValue[PaginationConfiguration] | None = None
    row_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class TableStyleTarget(PropertyType):
    cell_type: DslValue[str] | None = None


@dataclass
class TableUnaggregatedFieldWells(PropertyType):
    values: list[DslValue[UnaggregatedField]] = field(default_factory=list)


@dataclass
class TableVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[TableConfiguration] | None = None
    conditional_formatting: DslValue[TableConditionalFormatting] | None = None
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class TemplateError(PropertyType):
    message: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    violated_entities: list[DslValue[Entity]] = field(default_factory=list)


@dataclass
class TemplateSourceAnalysis(PropertyType):
    arn: DslValue[str] | None = None
    data_set_references: list[DslValue[DataSetReference]] = field(default_factory=list)


@dataclass
class TemplateSourceEntity(PropertyType):
    source_analysis: DslValue[TemplateSourceAnalysis] | None = None
    source_template: DslValue[TemplateSourceTemplate] | None = None


@dataclass
class TemplateSourceTemplate(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class TemplateVersion(PropertyType):
    created_time: DslValue[str] | None = None
    data_set_configurations: list[DslValue[DataSetConfiguration]] = field(
        default_factory=list
    )
    description: DslValue[str] | None = None
    errors: list[DslValue[TemplateError]] = field(default_factory=list)
    sheets: list[DslValue[Sheet]] = field(default_factory=list)
    source_entity_arn: DslValue[str] | None = None
    status: DslValue[str] | None = None
    theme_arn: DslValue[str] | None = None
    version_number: DslValue[float] | None = None


@dataclass
class TemplateVersionDefinition(PropertyType):
    data_set_configurations: list[DslValue[DataSetConfiguration]] = field(
        default_factory=list
    )
    analysis_defaults: DslValue[AnalysisDefaults] | None = None
    calculated_fields: list[DslValue[CalculatedField]] = field(default_factory=list)
    column_configurations: list[DslValue[ColumnConfiguration]] = field(
        default_factory=list
    )
    filter_groups: list[DslValue[FilterGroup]] = field(default_factory=list)
    options: DslValue[AssetOptions] | None = None
    parameter_declarations: list[DslValue[ParameterDeclaration]] = field(
        default_factory=list
    )
    query_execution_options: DslValue[QueryExecutionOptions] | None = None
    sheets: list[DslValue[SheetDefinition]] = field(default_factory=list)


@dataclass
class TextAreaControlDisplayOptions(PropertyType):
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    placeholder_options: DslValue[TextControlPlaceholderOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class TextConditionalFormat(PropertyType):
    background_color: DslValue[ConditionalFormattingColor] | None = None
    icon: DslValue[ConditionalFormattingIcon] | None = None
    text_color: DslValue[ConditionalFormattingColor] | None = None


@dataclass
class TextControlPlaceholderOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TextFieldControlDisplayOptions(PropertyType):
    info_icon_label_options: DslValue[SheetControlInfoIconLabelOptions] | None = None
    placeholder_options: DslValue[TextControlPlaceholderOptions] | None = None
    title_options: DslValue[LabelOptions] | None = None


@dataclass
class ThousandSeparatorOptions(PropertyType):
    grouping_style: DslValue[str] | None = None
    symbol: DslValue[str] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TimeBasedForecastProperties(PropertyType):
    lower_boundary: DslValue[float] | None = None
    periods_backward: DslValue[float] | None = None
    periods_forward: DslValue[float] | None = None
    prediction_interval: DslValue[float] | None = None
    seasonality: DslValue[float] | None = None
    upper_boundary: DslValue[float] | None = None


@dataclass
class TimeEqualityFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    parameter_name: DslValue[str] | None = None
    rolling_date: DslValue[RollingDateConfiguration] | None = None
    time_granularity: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TimeRangeDrillDownFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    range_maximum: DslValue[str] | None = None
    range_minimum: DslValue[str] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TimeRangeFilter(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    null_option: DslValue[str] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    exclude_period_configuration: DslValue[ExcludePeriodConfiguration] | None = None
    include_maximum: DslValue[bool] | None = None
    include_minimum: DslValue[bool] | None = None
    range_maximum_value: DslValue[TimeRangeFilterValue] | None = None
    range_minimum_value: DslValue[TimeRangeFilterValue] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TimeRangeFilterValue(PropertyType):
    parameter: DslValue[str] | None = None
    rolling_date: DslValue[RollingDateConfiguration] | None = None
    static_value: DslValue[str] | None = None


@dataclass
class TooltipItem(PropertyType):
    column_tooltip_item: DslValue[ColumnTooltipItem] | None = None
    field_tooltip_item: DslValue[FieldTooltipItem] | None = None


@dataclass
class TooltipOptions(PropertyType):
    field_based_tooltip: DslValue[FieldBasedTooltip] | None = None
    selected_tooltip_type: DslValue[str] | None = None
    tooltip_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TopBottomFilter(PropertyType):
    aggregation_sort_configurations: list[DslValue[AggregationSortConfiguration]] = (
        field(default_factory=list)
    )
    column: DslValue[ColumnIdentifier] | None = None
    filter_id: DslValue[str] | None = None
    default_filter_control_configuration: (
        DslValue[DefaultFilterControlConfiguration] | None
    ) = None
    limit: DslValue[float] | None = None
    parameter_name: DslValue[str] | None = None
    time_granularity: DslValue[str] | None = None


@dataclass
class TopBottomMoversComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    category: DslValue[DimensionField] | None = None
    mover_size: DslValue[float] | None = None
    name: DslValue[str] | None = None
    sort_order: DslValue[str] | None = None
    time: DslValue[DimensionField] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class TopBottomRankedComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    category: DslValue[DimensionField] | None = None
    name: DslValue[str] | None = None
    result_size: DslValue[float] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class TotalAggregationComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    value: DslValue[MeasureField] | None = None


@dataclass
class TotalAggregationFunction(PropertyType):
    simple_total_aggregation_function: DslValue[str] | None = None


@dataclass
class TotalAggregationOption(PropertyType):
    field_id: DslValue[str] | None = None
    total_aggregation_function: DslValue[TotalAggregationFunction] | None = None


@dataclass
class TotalOptions(PropertyType):
    custom_label: DslValue[str] | None = None
    placement: DslValue[str] | None = None
    scroll_status: DslValue[str] | None = None
    total_aggregation_options: list[DslValue[TotalAggregationOption]] = field(
        default_factory=list
    )
    total_cell_style: DslValue[TableCellStyle] | None = None
    totals_visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class TransposedTableOption(PropertyType):
    column_type: DslValue[str] | None = None
    column_index: DslValue[float] | None = None
    column_width: DslValue[str] | None = None


@dataclass
class TreeMapAggregatedFieldWells(PropertyType):
    colors: list[DslValue[MeasureField]] = field(default_factory=list)
    groups: list[DslValue[DimensionField]] = field(default_factory=list)
    sizes: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class TreeMapConfiguration(PropertyType):
    color_label_options: DslValue[ChartAxisLabelOptions] | None = None
    color_scale: DslValue[ColorScale] | None = None
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[TreeMapFieldWells] | None = None
    group_label_options: DslValue[ChartAxisLabelOptions] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    size_label_options: DslValue[ChartAxisLabelOptions] | None = None
    sort_configuration: DslValue[TreeMapSortConfiguration] | None = None
    tooltip: DslValue[TooltipOptions] | None = None


@dataclass
class TreeMapFieldWells(PropertyType):
    tree_map_aggregated_field_wells: DslValue[TreeMapAggregatedFieldWells] | None = None


@dataclass
class TreeMapSortConfiguration(PropertyType):
    tree_map_group_items_limit_configuration: (
        DslValue[ItemsLimitConfiguration] | None
    ) = None
    tree_map_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class TreeMapVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[TreeMapConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class TrendArrowOptions(PropertyType):
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class UnaggregatedField(PropertyType):
    column: DslValue[ColumnIdentifier] | None = None
    field_id: DslValue[str] | None = None
    format_configuration: DslValue[FormatConfiguration] | None = None


@dataclass
class UniqueValuesComputation(PropertyType):
    computation_id: DslValue[str] | None = None
    category: DslValue[DimensionField] | None = None
    name: DslValue[str] | None = None


@dataclass
class ValidationStrategy(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class VisibleRangeOptions(PropertyType):
    percent_range: DslValue[PercentVisibleRange] | None = None


@dataclass
class Visual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kpi_visual": "KPIVisual",
    }

    bar_chart_visual: DslValue[BarChartVisual] | None = None
    box_plot_visual: DslValue[BoxPlotVisual] | None = None
    combo_chart_visual: DslValue[ComboChartVisual] | None = None
    custom_content_visual: DslValue[CustomContentVisual] | None = None
    empty_visual: DslValue[EmptyVisual] | None = None
    filled_map_visual: DslValue[FilledMapVisual] | None = None
    funnel_chart_visual: DslValue[FunnelChartVisual] | None = None
    gauge_chart_visual: DslValue[GaugeChartVisual] | None = None
    geospatial_map_visual: DslValue[GeospatialMapVisual] | None = None
    heat_map_visual: DslValue[HeatMapVisual] | None = None
    histogram_visual: DslValue[HistogramVisual] | None = None
    insight_visual: DslValue[InsightVisual] | None = None
    kpi_visual: DslValue[KPIVisual] | None = None
    line_chart_visual: DslValue[LineChartVisual] | None = None
    pie_chart_visual: DslValue[PieChartVisual] | None = None
    pivot_table_visual: DslValue[PivotTableVisual] | None = None
    plugin_visual: DslValue[PluginVisual] | None = None
    radar_chart_visual: DslValue[RadarChartVisual] | None = None
    sankey_diagram_visual: DslValue[SankeyDiagramVisual] | None = None
    scatter_plot_visual: DslValue[ScatterPlotVisual] | None = None
    table_visual: DslValue[TableVisual] | None = None
    tree_map_visual: DslValue[TreeMapVisual] | None = None
    waterfall_visual: DslValue[WaterfallVisual] | None = None
    word_cloud_visual: DslValue[WordCloudVisual] | None = None


@dataclass
class VisualCustomAction(PropertyType):
    action_operations: list[DslValue[VisualCustomActionOperation]] = field(
        default_factory=list
    )
    custom_action_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    trigger: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class VisualCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_operation": "URLOperation",
    }

    filter_operation: DslValue[CustomActionFilterOperation] | None = None
    navigation_operation: DslValue[CustomActionNavigationOperation] | None = None
    set_parameters_operation: DslValue[CustomActionSetParametersOperation] | None = None
    url_operation: DslValue[CustomActionURLOperation] | None = None


@dataclass
class VisualInteractionOptions(PropertyType):
    context_menu_option: DslValue[ContextMenuOption] | None = None
    visual_menu_option: DslValue[VisualMenuOption] | None = None


@dataclass
class VisualMenuOption(PropertyType):
    availability_status: DslValue[str] | None = None


@dataclass
class VisualPalette(PropertyType):
    chart_color: DslValue[str] | None = None
    color_map: list[DslValue[DataPathColor]] = field(default_factory=list)


@dataclass
class VisualSubtitleLabelOptions(PropertyType):
    format_text: DslValue[LongFormatText] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class VisualTitleLabelOptions(PropertyType):
    format_text: DslValue[ShortFormatText] | None = None
    visibility: DslValue[dict[str, Any]] | None = None


@dataclass
class WaterfallChartAggregatedFieldWells(PropertyType):
    breakdowns: list[DslValue[DimensionField]] = field(default_factory=list)
    categories: list[DslValue[DimensionField]] = field(default_factory=list)
    values: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class WaterfallChartColorConfiguration(PropertyType):
    group_color_configuration: (
        DslValue[WaterfallChartGroupColorConfiguration] | None
    ) = None


@dataclass
class WaterfallChartConfiguration(PropertyType):
    category_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    category_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    color_configuration: DslValue[WaterfallChartColorConfiguration] | None = None
    data_labels: DslValue[DataLabelOptions] | None = None
    field_wells: DslValue[WaterfallChartFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    legend: DslValue[LegendOptions] | None = None
    primary_y_axis_display_options: DslValue[AxisDisplayOptions] | None = None
    primary_y_axis_label_options: DslValue[ChartAxisLabelOptions] | None = None
    sort_configuration: DslValue[WaterfallChartSortConfiguration] | None = None
    visual_palette: DslValue[VisualPalette] | None = None
    waterfall_chart_options: DslValue[WaterfallChartOptions] | None = None


@dataclass
class WaterfallChartFieldWells(PropertyType):
    waterfall_chart_aggregated_field_wells: (
        DslValue[WaterfallChartAggregatedFieldWells] | None
    ) = None


@dataclass
class WaterfallChartGroupColorConfiguration(PropertyType):
    negative_bar_color: DslValue[str] | None = None
    positive_bar_color: DslValue[str] | None = None
    total_bar_color: DslValue[str] | None = None


@dataclass
class WaterfallChartOptions(PropertyType):
    total_bar_label: DslValue[str] | None = None


@dataclass
class WaterfallChartSortConfiguration(PropertyType):
    breakdown_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class WaterfallVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[WaterfallChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class WhatIfPointScenario(PropertyType):
    date: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class WhatIfRangeScenario(PropertyType):
    end_date: DslValue[str] | None = None
    start_date: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class WordCloudAggregatedFieldWells(PropertyType):
    group_by: list[DslValue[DimensionField]] = field(default_factory=list)
    size: list[DslValue[MeasureField]] = field(default_factory=list)


@dataclass
class WordCloudChartConfiguration(PropertyType):
    category_label_options: DslValue[ChartAxisLabelOptions] | None = None
    field_wells: DslValue[WordCloudFieldWells] | None = None
    interactions: DslValue[VisualInteractionOptions] | None = None
    sort_configuration: DslValue[WordCloudSortConfiguration] | None = None
    word_cloud_options: DslValue[WordCloudOptions] | None = None


@dataclass
class WordCloudFieldWells(PropertyType):
    word_cloud_aggregated_field_wells: (
        DslValue[WordCloudAggregatedFieldWells] | None
    ) = None


@dataclass
class WordCloudOptions(PropertyType):
    cloud_layout: DslValue[str] | None = None
    maximum_string_length: DslValue[float] | None = None
    word_casing: DslValue[str] | None = None
    word_orientation: DslValue[str] | None = None
    word_padding: DslValue[str] | None = None
    word_scaling: DslValue[str] | None = None


@dataclass
class WordCloudSortConfiguration(PropertyType):
    category_items_limit: DslValue[ItemsLimitConfiguration] | None = None
    category_sort: list[DslValue[FieldSortOptions]] = field(default_factory=list)


@dataclass
class WordCloudVisual(PropertyType):
    visual_id: DslValue[str] | None = None
    actions: list[DslValue[VisualCustomAction]] = field(default_factory=list)
    chart_configuration: DslValue[WordCloudChartConfiguration] | None = None
    column_hierarchies: list[DslValue[ColumnHierarchy]] = field(default_factory=list)
    subtitle: DslValue[VisualSubtitleLabelOptions] | None = None
    title: DslValue[VisualTitleLabelOptions] | None = None
    visual_content_alt_text: DslValue[str] | None = None


@dataclass
class YAxisOptions(PropertyType):
    y_axis: DslValue[str] | None = None
