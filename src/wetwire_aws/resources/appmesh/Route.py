"""PropertyTypes for AWS::AppMesh::Route."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Duration(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class GrpcRetryPolicy(PropertyType):
    max_retries: int | None = None
    per_retry_timeout: Duration | None = None
    grpc_retry_events: list[String] = field(default_factory=list)
    http_retry_events: list[String] = field(default_factory=list)
    tcp_retry_events: list[String] = field(default_factory=list)


@dataclass
class GrpcRoute(PropertyType):
    action: GrpcRouteAction | None = None
    match: GrpcRouteMatch | None = None
    retry_policy: GrpcRetryPolicy | None = None
    timeout: GrpcTimeout | None = None


@dataclass
class GrpcRouteAction(PropertyType):
    weighted_targets: list[WeightedTarget] = field(default_factory=list)


@dataclass
class GrpcRouteMatch(PropertyType):
    metadata: list[GrpcRouteMetadata] = field(default_factory=list)
    method_name: str | None = None
    port: int | None = None
    service_name: str | None = None


@dataclass
class GrpcRouteMetadata(PropertyType):
    name: str | None = None
    invert: bool | None = None
    match: GrpcRouteMetadataMatchMethod | None = None


@dataclass
class GrpcRouteMetadataMatchMethod(PropertyType):
    exact: str | None = None
    prefix: str | None = None
    range: MatchRange | None = None
    regex: str | None = None
    suffix: str | None = None


@dataclass
class GrpcTimeout(PropertyType):
    idle: Duration | None = None
    per_request: Duration | None = None


@dataclass
class HeaderMatchMethod(PropertyType):
    exact: str | None = None
    prefix: str | None = None
    range: MatchRange | None = None
    regex: str | None = None
    suffix: str | None = None


@dataclass
class HttpPathMatch(PropertyType):
    exact: str | None = None
    regex: str | None = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    exact: str | None = None


@dataclass
class HttpRetryPolicy(PropertyType):
    max_retries: int | None = None
    per_retry_timeout: Duration | None = None
    http_retry_events: list[String] = field(default_factory=list)
    tcp_retry_events: list[String] = field(default_factory=list)


@dataclass
class HttpRoute(PropertyType):
    action: HttpRouteAction | None = None
    match: HttpRouteMatch | None = None
    retry_policy: HttpRetryPolicy | None = None
    timeout: HttpTimeout | None = None


@dataclass
class HttpRouteAction(PropertyType):
    weighted_targets: list[WeightedTarget] = field(default_factory=list)


@dataclass
class HttpRouteHeader(PropertyType):
    name: str | None = None
    invert: bool | None = None
    match: HeaderMatchMethod | None = None


@dataclass
class HttpRouteMatch(PropertyType):
    headers: list[HttpRouteHeader] = field(default_factory=list)
    method: str | None = None
    path: HttpPathMatch | None = None
    port: int | None = None
    prefix: str | None = None
    query_parameters: list[QueryParameter] = field(default_factory=list)
    scheme: str | None = None


@dataclass
class HttpTimeout(PropertyType):
    idle: Duration | None = None
    per_request: Duration | None = None


@dataclass
class MatchRange(PropertyType):
    end: int | None = None
    start: int | None = None


@dataclass
class QueryParameter(PropertyType):
    name: str | None = None
    match: HttpQueryParameterMatch | None = None


@dataclass
class RouteSpec(PropertyType):
    grpc_route: GrpcRoute | None = None
    http2_route: HttpRoute | None = None
    http_route: HttpRoute | None = None
    priority: int | None = None
    tcp_route: TcpRoute | None = None


@dataclass
class TcpRoute(PropertyType):
    action: TcpRouteAction | None = None
    match: TcpRouteMatch | None = None
    timeout: TcpTimeout | None = None


@dataclass
class TcpRouteAction(PropertyType):
    weighted_targets: list[WeightedTarget] = field(default_factory=list)


@dataclass
class TcpRouteMatch(PropertyType):
    port: int | None = None


@dataclass
class TcpTimeout(PropertyType):
    idle: Duration | None = None


@dataclass
class WeightedTarget(PropertyType):
    virtual_node: str | None = None
    weight: int | None = None
    port: int | None = None
