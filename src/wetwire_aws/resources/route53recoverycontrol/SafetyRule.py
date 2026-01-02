"""PropertyTypes for AWS::Route53RecoveryControl::SafetyRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssertionRule(PropertyType):
    asserted_controls: list[String] = field(default_factory=list)
    wait_period_ms: int | None = None


@dataclass
class GatingRule(PropertyType):
    gating_controls: list[String] = field(default_factory=list)
    target_controls: list[String] = field(default_factory=list)
    wait_period_ms: int | None = None


@dataclass
class RuleConfig(PropertyType):
    inverted: bool | None = None
    threshold: int | None = None
    type_: str | None = None
