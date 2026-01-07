"""PropertyTypes for AWS::CloudFormation::LambdaHook."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HookTarget(PropertyType):
    action: DslValue[str] | None = None
    invocation_point: DslValue[str] | None = None
    target_name: DslValue[str] | None = None


@dataclass
class StackFilters(PropertyType):
    filtering_criteria: DslValue[str] | None = None
    stack_names: DslValue[StackNames] | None = None
    stack_roles: DslValue[StackRoles] | None = None


@dataclass
class StackNames(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StackRoles(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TargetFilters(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    invocation_points: list[DslValue[str]] = field(default_factory=list)
    target_names: list[DslValue[str]] = field(default_factory=list)
    targets: list[DslValue[HookTarget]] = field(default_factory=list)
