"""PropertyTypes for AWS::IoTFleetWise::Vehicle."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PeriodicStateTemplateUpdateStrategy(PropertyType):
    state_template_update_rate: DslValue[TimePeriod] | None = None


@dataclass
class StateTemplateAssociation(PropertyType):
    identifier: DslValue[str] | None = None
    state_template_update_strategy: DslValue[StateTemplateUpdateStrategy] | None = None


@dataclass
class StateTemplateUpdateStrategy(PropertyType):
    on_change: DslValue[dict[str, Any]] | None = None
    periodic: DslValue[PeriodicStateTemplateUpdateStrategy] | None = None


@dataclass
class TimePeriod(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[float] | None = None
