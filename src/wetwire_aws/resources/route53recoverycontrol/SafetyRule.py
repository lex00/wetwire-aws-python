"""PropertyTypes for AWS::Route53RecoveryControl::SafetyRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssertionRule(PropertyType):
    asserted_controls: list[DslValue[str]] = field(default_factory=list)
    wait_period_ms: DslValue[int] | None = None


@dataclass
class GatingRule(PropertyType):
    gating_controls: list[DslValue[str]] = field(default_factory=list)
    target_controls: list[DslValue[str]] = field(default_factory=list)
    wait_period_ms: DslValue[int] | None = None


@dataclass
class RuleConfig(PropertyType):
    inverted: DslValue[bool] | None = None
    threshold: DslValue[int] | None = None
    type_: DslValue[str] | None = None
