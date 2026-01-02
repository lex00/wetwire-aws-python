"""PropertyTypes for AWS::Budgets::Budget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoAdjustData(PropertyType):
    auto_adjust_type: str | None = None
    historical_options: HistoricalOptions | None = None


@dataclass
class BudgetData(PropertyType):
    budget_type: str | None = None
    time_unit: str | None = None
    auto_adjust_data: AutoAdjustData | None = None
    billing_view_arn: str | None = None
    budget_limit: Spend | None = None
    budget_name: str | None = None
    cost_filters: dict[str, Any] | None = None
    cost_types: CostTypes | None = None
    filter_expression: Expression | None = None
    metrics: list[String] = field(default_factory=list)
    planned_budget_limits: dict[str, Any] | None = None
    time_period: TimePeriod | None = None


@dataclass
class CostCategoryValues(PropertyType):
    key: str | None = None
    match_options: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class CostTypes(PropertyType):
    include_credit: bool | None = None
    include_discount: bool | None = None
    include_other_subscription: bool | None = None
    include_recurring: bool | None = None
    include_refund: bool | None = None
    include_subscription: bool | None = None
    include_support: bool | None = None
    include_tax: bool | None = None
    include_upfront: bool | None = None
    use_amortized: bool | None = None
    use_blended: bool | None = None


@dataclass
class Expression(PropertyType):
    and_: list[Expression] = field(default_factory=list)
    cost_categories: CostCategoryValues | None = None
    dimensions: ExpressionDimensionValues | None = None
    not_: Expression | None = None
    or_: list[Expression] = field(default_factory=list)
    tags: TagValues | None = None


@dataclass
class ExpressionDimensionValues(PropertyType):
    key: str | None = None
    match_options: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class HistoricalOptions(PropertyType):
    budget_adjustment_period: int | None = None


@dataclass
class Notification(PropertyType):
    comparison_operator: str | None = None
    notification_type: str | None = None
    threshold: float | None = None
    threshold_type: str | None = None


@dataclass
class NotificationWithSubscribers(PropertyType):
    notification: Notification | None = None
    subscribers: list[Subscriber] = field(default_factory=list)


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Spend(PropertyType):
    amount: float | None = None
    unit: str | None = None


@dataclass
class Subscriber(PropertyType):
    address: str | None = None
    subscription_type: str | None = None


@dataclass
class TagValues(PropertyType):
    key: str | None = None
    match_options: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class TimePeriod(PropertyType):
    end: str | None = None
    start: str | None = None
