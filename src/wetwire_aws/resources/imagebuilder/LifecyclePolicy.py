"""PropertyTypes for AWS::ImageBuilder::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    type_: DslValue[str] | None = None
    include_resources: DslValue[IncludeResources] | None = None


@dataclass
class AmiExclusionRules(PropertyType):
    is_public: DslValue[bool] | None = None
    last_launched: DslValue[LastLaunched] | None = None
    regions: list[DslValue[str]] = field(default_factory=list)
    shared_accounts: list[DslValue[str]] = field(default_factory=list)
    tag_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class ExclusionRules(PropertyType):
    amis: DslValue[AmiExclusionRules] | None = None
    tag_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class Filter(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None
    retain_at_least: DslValue[int] | None = None
    unit: DslValue[str] | None = None


@dataclass
class IncludeResources(PropertyType):
    amis: DslValue[bool] | None = None
    containers: DslValue[bool] | None = None
    snapshots: DslValue[bool] | None = None


@dataclass
class LastLaunched(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class PolicyDetail(PropertyType):
    action: DslValue[Action] | None = None
    filter: DslValue[Filter] | None = None
    exclusion_rules: DslValue[ExclusionRules] | None = None


@dataclass
class RecipeSelection(PropertyType):
    name: DslValue[str] | None = None
    semantic_version: DslValue[str] | None = None


@dataclass
class ResourceSelection(PropertyType):
    recipes: list[DslValue[RecipeSelection]] = field(default_factory=list)
    tag_map: dict[str, DslValue[str]] = field(default_factory=dict)
