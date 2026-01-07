"""PropertyTypes for AWS::ApiGatewayV2::RoutingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    invoke_api: DslValue[ActionInvokeApi] | None = None


@dataclass
class ActionInvokeApi(PropertyType):
    api_id: DslValue[str] | None = None
    stage: DslValue[str] | None = None
    strip_base_path: DslValue[bool] | None = None


@dataclass
class Condition(PropertyType):
    match_base_paths: DslValue[MatchBasePaths] | None = None
    match_headers: DslValue[MatchHeaders] | None = None


@dataclass
class MatchBasePaths(PropertyType):
    any_of: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MatchHeaderValue(PropertyType):
    header: DslValue[str] | None = None
    value_glob: DslValue[str] | None = None


@dataclass
class MatchHeaders(PropertyType):
    any_of: list[DslValue[MatchHeaderValue]] = field(default_factory=list)
