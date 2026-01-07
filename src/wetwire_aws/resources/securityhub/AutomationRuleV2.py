"""PropertyTypes for AWS::SecurityHub::AutomationRuleV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutomationRulesActionV2(PropertyType):
    type_: DslValue[str] | None = None
    external_integration_configuration: (
        DslValue[ExternalIntegrationConfiguration] | None
    ) = None
    finding_fields_update: DslValue[AutomationRulesFindingFieldsUpdateV2] | None = None


@dataclass
class AutomationRulesFindingFieldsUpdateV2(PropertyType):
    comment: DslValue[str] | None = None
    severity_id: DslValue[int] | None = None
    status_id: DslValue[int] | None = None


@dataclass
class BooleanFilter(PropertyType):
    value: DslValue[bool] | None = None


@dataclass
class CompositeFilter(PropertyType):
    boolean_filters: list[DslValue[OcsfBooleanFilter]] = field(default_factory=list)
    date_filters: list[DslValue[OcsfDateFilter]] = field(default_factory=list)
    map_filters: list[DslValue[OcsfMapFilter]] = field(default_factory=list)
    number_filters: list[DslValue[OcsfNumberFilter]] = field(default_factory=list)
    operator: DslValue[str] | None = None
    string_filters: list[DslValue[OcsfStringFilter]] = field(default_factory=list)


@dataclass
class Criteria(PropertyType):
    ocsf_finding_criteria: DslValue[OcsfFindingFilters] | None = None


@dataclass
class DateFilter(PropertyType):
    date_range: DslValue[DateRange] | None = None
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None


@dataclass
class DateRange(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class ExternalIntegrationConfiguration(PropertyType):
    connector_arn: DslValue[str] | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: DslValue[float] | None = None
    gte: DslValue[float] | None = None
    lte: DslValue[float] | None = None


@dataclass
class OcsfBooleanFilter(PropertyType):
    field_name: DslValue[str] | None = None
    filter: DslValue[BooleanFilter] | None = None


@dataclass
class OcsfDateFilter(PropertyType):
    field_name: DslValue[str] | None = None
    filter: DslValue[DateFilter] | None = None


@dataclass
class OcsfFindingFilters(PropertyType):
    composite_filters: list[DslValue[CompositeFilter]] = field(default_factory=list)
    composite_operator: DslValue[str] | None = None


@dataclass
class OcsfMapFilter(PropertyType):
    field_name: DslValue[str] | None = None
    filter: DslValue[MapFilter] | None = None


@dataclass
class OcsfNumberFilter(PropertyType):
    field_name: DslValue[str] | None = None
    filter: DslValue[NumberFilter] | None = None


@dataclass
class OcsfStringFilter(PropertyType):
    field_name: DslValue[str] | None = None
    filter: DslValue[StringFilter] | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: DslValue[str] | None = None
    value: DslValue[str] | None = None
