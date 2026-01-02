"""PropertyTypes for AWS::IoTFleetWise::Vehicle."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PeriodicStateTemplateUpdateStrategy(PropertyType):
    state_template_update_rate: TimePeriod | None = None


@dataclass
class StateTemplateAssociation(PropertyType):
    identifier: str | None = None
    state_template_update_strategy: StateTemplateUpdateStrategy | None = None


@dataclass
class StateTemplateUpdateStrategy(PropertyType):
    on_change: dict[str, Any] | None = None
    periodic: PeriodicStateTemplateUpdateStrategy | None = None


@dataclass
class TimePeriod(PropertyType):
    unit: str | None = None
    value: float | None = None
