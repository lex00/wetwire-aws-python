"""PropertyTypes for AWS::BillingConductor::CustomLineItem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BillingPeriodRange(PropertyType):
    exclusive_end_billing_period: DslValue[str] | None = None
    inclusive_start_billing_period: DslValue[str] | None = None


@dataclass
class CustomLineItemChargeDetails(PropertyType):
    type_: DslValue[str] | None = None
    flat: DslValue[CustomLineItemFlatChargeDetails] | None = None
    line_item_filters: list[DslValue[LineItemFilter]] = field(default_factory=list)
    percentage: DslValue[CustomLineItemPercentageChargeDetails] | None = None


@dataclass
class CustomLineItemFlatChargeDetails(PropertyType):
    charge_value: DslValue[float] | None = None


@dataclass
class CustomLineItemPercentageChargeDetails(PropertyType):
    percentage_value: DslValue[float] | None = None
    child_associated_resources: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LineItemFilter(PropertyType):
    attribute: DslValue[str] | None = None
    match_option: DslValue[str] | None = None
    attribute_values: list[DslValue[str]] = field(default_factory=list)
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PresentationDetails(PropertyType):
    service: DslValue[str] | None = None
