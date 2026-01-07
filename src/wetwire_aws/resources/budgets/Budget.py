"""PropertyTypes for AWS::Budgets::Budget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoAdjustData(PropertyType):
    auto_adjust_type: DslValue[str] | None = None
    historical_options: DslValue[HistoricalOptions] | None = None


@dataclass
class BudgetData(PropertyType):
    budget_type: DslValue[str] | None = None
    time_unit: DslValue[str] | None = None
    auto_adjust_data: DslValue[AutoAdjustData] | None = None
    billing_view_arn: DslValue[str] | None = None
    budget_limit: DslValue[Spend] | None = None
    budget_name: DslValue[str] | None = None
    cost_filters: DslValue[dict[str, Any]] | None = None
    cost_types: DslValue[CostTypes] | None = None
    filter_expression: DslValue[Expression] | None = None
    metrics: list[DslValue[str]] = field(default_factory=list)
    planned_budget_limits: DslValue[dict[str, Any]] | None = None
    time_period: DslValue[TimePeriod] | None = None


@dataclass
class CostCategoryValues(PropertyType):
    key: DslValue[str] | None = None
    match_options: list[DslValue[str]] = field(default_factory=list)
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CostTypes(PropertyType):
    include_credit: DslValue[bool] | None = None
    include_discount: DslValue[bool] | None = None
    include_other_subscription: DslValue[bool] | None = None
    include_recurring: DslValue[bool] | None = None
    include_refund: DslValue[bool] | None = None
    include_subscription: DslValue[bool] | None = None
    include_support: DslValue[bool] | None = None
    include_tax: DslValue[bool] | None = None
    include_upfront: DslValue[bool] | None = None
    use_amortized: DslValue[bool] | None = None
    use_blended: DslValue[bool] | None = None


@dataclass
class Expression(PropertyType):
    and_: list[DslValue[Expression]] = field(default_factory=list)
    cost_categories: DslValue[CostCategoryValues] | None = None
    dimensions: DslValue[ExpressionDimensionValues] | None = None
    not_: DslValue[Expression] | None = None
    or_: list[DslValue[Expression]] = field(default_factory=list)
    tags: DslValue[TagValues] | None = None


@dataclass
class ExpressionDimensionValues(PropertyType):
    key: DslValue[str] | None = None
    match_options: list[DslValue[str]] = field(default_factory=list)
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HistoricalOptions(PropertyType):
    budget_adjustment_period: DslValue[int] | None = None


@dataclass
class Notification(PropertyType):
    comparison_operator: DslValue[str] | None = None
    notification_type: DslValue[str] | None = None
    threshold: DslValue[float] | None = None
    threshold_type: DslValue[str] | None = None


@dataclass
class NotificationWithSubscribers(PropertyType):
    notification: DslValue[Notification] | None = None
    subscribers: list[DslValue[Subscriber]] = field(default_factory=list)


@dataclass
class ResourceTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Spend(PropertyType):
    amount: DslValue[float] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Subscriber(PropertyType):
    address: DslValue[str] | None = None
    subscription_type: DslValue[str] | None = None


@dataclass
class TagValues(PropertyType):
    key: DslValue[str] | None = None
    match_options: list[DslValue[str]] = field(default_factory=list)
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TimePeriod(PropertyType):
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None
