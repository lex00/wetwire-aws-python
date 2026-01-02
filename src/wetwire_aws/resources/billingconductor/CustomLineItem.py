"""PropertyTypes for AWS::BillingConductor::CustomLineItem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BillingPeriodRange(PropertyType):
    exclusive_end_billing_period: str | None = None
    inclusive_start_billing_period: str | None = None


@dataclass
class CustomLineItemChargeDetails(PropertyType):
    type_: str | None = None
    flat: CustomLineItemFlatChargeDetails | None = None
    line_item_filters: list[LineItemFilter] = field(default_factory=list)
    percentage: CustomLineItemPercentageChargeDetails | None = None


@dataclass
class CustomLineItemFlatChargeDetails(PropertyType):
    charge_value: float | None = None


@dataclass
class CustomLineItemPercentageChargeDetails(PropertyType):
    percentage_value: float | None = None
    child_associated_resources: list[String] = field(default_factory=list)


@dataclass
class LineItemFilter(PropertyType):
    attribute: str | None = None
    match_option: str | None = None
    attribute_values: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class PresentationDetails(PropertyType):
    service: str | None = None
