"""PropertyTypes for AWS::ApiGatewayV2::RoutingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    invoke_api: ActionInvokeApi | None = None


@dataclass
class ActionInvokeApi(PropertyType):
    api_id: str | None = None
    stage: str | None = None
    strip_base_path: bool | None = None


@dataclass
class Condition(PropertyType):
    match_base_paths: MatchBasePaths | None = None
    match_headers: MatchHeaders | None = None


@dataclass
class MatchBasePaths(PropertyType):
    any_of: list[String] = field(default_factory=list)


@dataclass
class MatchHeaderValue(PropertyType):
    header: str | None = None
    value_glob: str | None = None


@dataclass
class MatchHeaders(PropertyType):
    any_of: list[MatchHeaderValue] = field(default_factory=list)
