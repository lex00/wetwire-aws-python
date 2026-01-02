"""PropertyTypes for AWS::VpcLattice::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    fixed_response: FixedResponse | None = None
    forward: Forward | None = None


@dataclass
class FixedResponse(PropertyType):
    status_code: int | None = None


@dataclass
class Forward(PropertyType):
    target_groups: list[WeightedTargetGroup] = field(default_factory=list)


@dataclass
class HeaderMatch(PropertyType):
    match: HeaderMatchType | None = None
    name: str | None = None
    case_sensitive: bool | None = None


@dataclass
class HeaderMatchType(PropertyType):
    contains: str | None = None
    exact: str | None = None
    prefix: str | None = None


@dataclass
class HttpMatch(PropertyType):
    header_matches: list[HeaderMatch] = field(default_factory=list)
    method: str | None = None
    path_match: PathMatch | None = None


@dataclass
class Match(PropertyType):
    http_match: HttpMatch | None = None


@dataclass
class PathMatch(PropertyType):
    match: PathMatchType | None = None
    case_sensitive: bool | None = None


@dataclass
class PathMatchType(PropertyType):
    exact: str | None = None
    prefix: str | None = None


@dataclass
class WeightedTargetGroup(PropertyType):
    target_group_identifier: str | None = None
    weight: int | None = None
