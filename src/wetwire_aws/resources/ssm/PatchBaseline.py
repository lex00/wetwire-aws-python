"""PropertyTypes for AWS::SSM::PatchBaseline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PatchFilter(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class PatchFilterGroup(PropertyType):
    patch_filters: list[PatchFilter] = field(default_factory=list)


@dataclass
class PatchSource(PropertyType):
    configuration: str | None = None
    name: str | None = None
    products: list[String] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    approve_after_days: int | None = None
    approve_until_date: str | None = None
    compliance_level: str | None = None
    enable_non_security: bool | None = None
    patch_filter_group: PatchFilterGroup | None = None


@dataclass
class RuleGroup(PropertyType):
    patch_rules: list[Rule] = field(default_factory=list)
