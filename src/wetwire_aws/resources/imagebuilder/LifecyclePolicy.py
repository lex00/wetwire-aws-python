"""PropertyTypes for AWS::ImageBuilder::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    type_: str | None = None
    include_resources: IncludeResources | None = None


@dataclass
class AmiExclusionRules(PropertyType):
    is_public: bool | None = None
    last_launched: LastLaunched | None = None
    regions: list[String] = field(default_factory=list)
    shared_accounts: list[String] = field(default_factory=list)
    tag_map: dict[str, String] = field(default_factory=dict)


@dataclass
class ExclusionRules(PropertyType):
    amis: AmiExclusionRules | None = None
    tag_map: dict[str, String] = field(default_factory=dict)


@dataclass
class Filter(PropertyType):
    type_: str | None = None
    value: int | None = None
    retain_at_least: int | None = None
    unit: str | None = None


@dataclass
class IncludeResources(PropertyType):
    amis: bool | None = None
    containers: bool | None = None
    snapshots: bool | None = None


@dataclass
class LastLaunched(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class PolicyDetail(PropertyType):
    action: Action | None = None
    filter: Filter | None = None
    exclusion_rules: ExclusionRules | None = None


@dataclass
class RecipeSelection(PropertyType):
    name: str | None = None
    semantic_version: str | None = None


@dataclass
class ResourceSelection(PropertyType):
    recipes: list[RecipeSelection] = field(default_factory=list)
    tag_map: dict[str, String] = field(default_factory=dict)
