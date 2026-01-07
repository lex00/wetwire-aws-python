"""PropertyTypes for AWS::SSM::PatchBaseline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PatchFilter(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PatchFilterGroup(PropertyType):
    patch_filters: list[DslValue[PatchFilter]] = field(default_factory=list)


@dataclass
class PatchSource(PropertyType):
    configuration: DslValue[str] | None = None
    name: DslValue[str] | None = None
    products: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    approve_after_days: DslValue[int] | None = None
    approve_until_date: DslValue[str] | None = None
    compliance_level: DslValue[str] | None = None
    enable_non_security: DslValue[bool] | None = None
    patch_filter_group: DslValue[PatchFilterGroup] | None = None


@dataclass
class RuleGroup(PropertyType):
    patch_rules: list[DslValue[Rule]] = field(default_factory=list)
