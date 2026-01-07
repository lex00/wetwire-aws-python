"""PropertyTypes for AWS::AppMesh::Route."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Duration(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class GrpcRetryPolicy(PropertyType):
    max_retries: DslValue[int] | None = None
    per_retry_timeout: DslValue[Duration] | None = None
    grpc_retry_events: list[DslValue[str]] = field(default_factory=list)
    http_retry_events: list[DslValue[str]] = field(default_factory=list)
    tcp_retry_events: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GrpcRoute(PropertyType):
    action: DslValue[GrpcRouteAction] | None = None
    match: DslValue[GrpcRouteMatch] | None = None
    retry_policy: DslValue[GrpcRetryPolicy] | None = None
    timeout: DslValue[GrpcTimeout] | None = None


@dataclass
class GrpcRouteAction(PropertyType):
    weighted_targets: list[DslValue[WeightedTarget]] = field(default_factory=list)


@dataclass
class GrpcRouteMatch(PropertyType):
    metadata: list[DslValue[GrpcRouteMetadata]] = field(default_factory=list)
    method_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    service_name: DslValue[str] | None = None


@dataclass
class GrpcRouteMetadata(PropertyType):
    name: DslValue[str] | None = None
    invert: DslValue[bool] | None = None
    match: DslValue[GrpcRouteMetadataMatchMethod] | None = None


@dataclass
class GrpcRouteMetadataMatchMethod(PropertyType):
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    range: DslValue[MatchRange] | None = None
    regex: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class GrpcTimeout(PropertyType):
    idle: DslValue[Duration] | None = None
    per_request: DslValue[Duration] | None = None


@dataclass
class HeaderMatchMethod(PropertyType):
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    range: DslValue[MatchRange] | None = None
    regex: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class HttpPathMatch(PropertyType):
    exact: DslValue[str] | None = None
    regex: DslValue[str] | None = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    exact: DslValue[str] | None = None


@dataclass
class HttpRetryPolicy(PropertyType):
    max_retries: DslValue[int] | None = None
    per_retry_timeout: DslValue[Duration] | None = None
    http_retry_events: list[DslValue[str]] = field(default_factory=list)
    tcp_retry_events: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HttpRoute(PropertyType):
    action: DslValue[HttpRouteAction] | None = None
    match: DslValue[HttpRouteMatch] | None = None
    retry_policy: DslValue[HttpRetryPolicy] | None = None
    timeout: DslValue[HttpTimeout] | None = None


@dataclass
class HttpRouteAction(PropertyType):
    weighted_targets: list[DslValue[WeightedTarget]] = field(default_factory=list)


@dataclass
class HttpRouteHeader(PropertyType):
    name: DslValue[str] | None = None
    invert: DslValue[bool] | None = None
    match: DslValue[HeaderMatchMethod] | None = None


@dataclass
class HttpRouteMatch(PropertyType):
    headers: list[DslValue[HttpRouteHeader]] = field(default_factory=list)
    method: DslValue[str] | None = None
    path: DslValue[HttpPathMatch] | None = None
    port: DslValue[int] | None = None
    prefix: DslValue[str] | None = None
    query_parameters: list[DslValue[QueryParameter]] = field(default_factory=list)
    scheme: DslValue[str] | None = None


@dataclass
class HttpTimeout(PropertyType):
    idle: DslValue[Duration] | None = None
    per_request: DslValue[Duration] | None = None


@dataclass
class MatchRange(PropertyType):
    end: DslValue[int] | None = None
    start: DslValue[int] | None = None


@dataclass
class QueryParameter(PropertyType):
    name: DslValue[str] | None = None
    match: DslValue[HttpQueryParameterMatch] | None = None


@dataclass
class RouteSpec(PropertyType):
    grpc_route: DslValue[GrpcRoute] | None = None
    http2_route: DslValue[HttpRoute] | None = None
    http_route: DslValue[HttpRoute] | None = None
    priority: DslValue[int] | None = None
    tcp_route: DslValue[TcpRoute] | None = None


@dataclass
class TcpRoute(PropertyType):
    action: DslValue[TcpRouteAction] | None = None
    match: DslValue[TcpRouteMatch] | None = None
    timeout: DslValue[TcpTimeout] | None = None


@dataclass
class TcpRouteAction(PropertyType):
    weighted_targets: list[DslValue[WeightedTarget]] = field(default_factory=list)


@dataclass
class TcpRouteMatch(PropertyType):
    port: DslValue[int] | None = None


@dataclass
class TcpTimeout(PropertyType):
    idle: DslValue[Duration] | None = None


@dataclass
class WeightedTarget(PropertyType):
    virtual_node: DslValue[str] | None = None
    weight: DslValue[int] | None = None
    port: DslValue[int] | None = None
