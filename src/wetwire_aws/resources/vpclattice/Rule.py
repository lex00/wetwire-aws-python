"""PropertyTypes for AWS::VpcLattice::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    fixed_response: DslValue[FixedResponse] | None = None
    forward: DslValue[Forward] | None = None


@dataclass
class FixedResponse(PropertyType):
    status_code: DslValue[int] | None = None


@dataclass
class Forward(PropertyType):
    target_groups: list[DslValue[WeightedTargetGroup]] = field(default_factory=list)


@dataclass
class HeaderMatch(PropertyType):
    match: DslValue[HeaderMatchType] | None = None
    name: DslValue[str] | None = None
    case_sensitive: DslValue[bool] | None = None


@dataclass
class HeaderMatchType(PropertyType):
    contains: DslValue[str] | None = None
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class HttpMatch(PropertyType):
    header_matches: list[DslValue[HeaderMatch]] = field(default_factory=list)
    method: DslValue[str] | None = None
    path_match: DslValue[PathMatch] | None = None


@dataclass
class Match(PropertyType):
    http_match: DslValue[HttpMatch] | None = None


@dataclass
class PathMatch(PropertyType):
    match: DslValue[PathMatchType] | None = None
    case_sensitive: DslValue[bool] | None = None


@dataclass
class PathMatchType(PropertyType):
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class WeightedTargetGroup(PropertyType):
    target_group_identifier: DslValue[str] | None = None
    weight: DslValue[int] | None = None
