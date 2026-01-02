"""PropertyTypes for AWS::CloudFormation::GuardHook."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HookTarget(PropertyType):
    action: str | None = None
    invocation_point: str | None = None
    target_name: str | None = None


@dataclass
class Options(PropertyType):
    input_params: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    uri: str | None = None
    version_id: str | None = None


@dataclass
class StackFilters(PropertyType):
    filtering_criteria: str | None = None
    stack_names: StackNames | None = None
    stack_roles: StackRoles | None = None


@dataclass
class StackNames(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class StackRoles(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class TargetFilters(PropertyType):
    actions: list[String] = field(default_factory=list)
    invocation_points: list[String] = field(default_factory=list)
    target_names: list[String] = field(default_factory=list)
    targets: list[HookTarget] = field(default_factory=list)
