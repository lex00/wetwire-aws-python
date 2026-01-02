"""PropertyTypes for AWS::SecurityHub::AutomationRuleV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutomationRulesActionV2(PropertyType):
    type_: str | None = None
    external_integration_configuration: ExternalIntegrationConfiguration | None = None
    finding_fields_update: AutomationRulesFindingFieldsUpdateV2 | None = None


@dataclass
class AutomationRulesFindingFieldsUpdateV2(PropertyType):
    comment: str | None = None
    severity_id: int | None = None
    status_id: int | None = None


@dataclass
class BooleanFilter(PropertyType):
    value: bool | None = None


@dataclass
class CompositeFilter(PropertyType):
    boolean_filters: list[OcsfBooleanFilter] = field(default_factory=list)
    date_filters: list[OcsfDateFilter] = field(default_factory=list)
    map_filters: list[OcsfMapFilter] = field(default_factory=list)
    number_filters: list[OcsfNumberFilter] = field(default_factory=list)
    operator: str | None = None
    string_filters: list[OcsfStringFilter] = field(default_factory=list)


@dataclass
class Criteria(PropertyType):
    ocsf_finding_criteria: OcsfFindingFilters | None = None


@dataclass
class DateFilter(PropertyType):
    date_range: DateRange | None = None
    end: str | None = None
    start: str | None = None


@dataclass
class DateRange(PropertyType):
    unit: str | None = None
    value: float | None = None


@dataclass
class ExternalIntegrationConfiguration(PropertyType):
    connector_arn: str | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: float | None = None
    gte: float | None = None
    lte: float | None = None


@dataclass
class OcsfBooleanFilter(PropertyType):
    field_name: str | None = None
    filter: BooleanFilter | None = None


@dataclass
class OcsfDateFilter(PropertyType):
    field_name: str | None = None
    filter: DateFilter | None = None


@dataclass
class OcsfFindingFilters(PropertyType):
    composite_filters: list[CompositeFilter] = field(default_factory=list)
    composite_operator: str | None = None


@dataclass
class OcsfMapFilter(PropertyType):
    field_name: str | None = None
    filter: MapFilter | None = None


@dataclass
class OcsfNumberFilter(PropertyType):
    field_name: str | None = None
    filter: NumberFilter | None = None


@dataclass
class OcsfStringFilter(PropertyType):
    field_name: str | None = None
    filter: StringFilter | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: str | None = None
    value: str | None = None
