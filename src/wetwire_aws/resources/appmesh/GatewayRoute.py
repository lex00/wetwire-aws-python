"""PropertyTypes for AWS::AppMesh::GatewayRoute."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GatewayRouteHostnameMatch(PropertyType):
    exact: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class GatewayRouteHostnameRewrite(PropertyType):
    default_target_hostname: DslValue[str] | None = None


@dataclass
class GatewayRouteMetadataMatch(PropertyType):
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    range: DslValue[GatewayRouteRangeMatch] | None = None
    regex: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class GatewayRouteRangeMatch(PropertyType):
    end: DslValue[int] | None = None
    start: DslValue[int] | None = None


@dataclass
class GatewayRouteSpec(PropertyType):
    grpc_route: DslValue[GrpcGatewayRoute] | None = None
    http2_route: DslValue[HttpGatewayRoute] | None = None
    http_route: DslValue[HttpGatewayRoute] | None = None
    priority: DslValue[int] | None = None


@dataclass
class GatewayRouteTarget(PropertyType):
    virtual_service: DslValue[GatewayRouteVirtualService] | None = None
    port: DslValue[int] | None = None


@dataclass
class GatewayRouteVirtualService(PropertyType):
    virtual_service_name: DslValue[str] | None = None


@dataclass
class GrpcGatewayRoute(PropertyType):
    action: DslValue[GrpcGatewayRouteAction] | None = None
    match: DslValue[GrpcGatewayRouteMatch] | None = None


@dataclass
class GrpcGatewayRouteAction(PropertyType):
    target: DslValue[GatewayRouteTarget] | None = None
    rewrite: DslValue[GrpcGatewayRouteRewrite] | None = None


@dataclass
class GrpcGatewayRouteMatch(PropertyType):
    hostname: DslValue[GatewayRouteHostnameMatch] | None = None
    metadata: list[DslValue[GrpcGatewayRouteMetadata]] = field(default_factory=list)
    port: DslValue[int] | None = None
    service_name: DslValue[str] | None = None


@dataclass
class GrpcGatewayRouteMetadata(PropertyType):
    name: DslValue[str] | None = None
    invert: DslValue[bool] | None = None
    match: DslValue[GatewayRouteMetadataMatch] | None = None


@dataclass
class GrpcGatewayRouteRewrite(PropertyType):
    hostname: DslValue[GatewayRouteHostnameRewrite] | None = None


@dataclass
class HttpGatewayRoute(PropertyType):
    action: DslValue[HttpGatewayRouteAction] | None = None
    match: DslValue[HttpGatewayRouteMatch] | None = None


@dataclass
class HttpGatewayRouteAction(PropertyType):
    target: DslValue[GatewayRouteTarget] | None = None
    rewrite: DslValue[HttpGatewayRouteRewrite] | None = None


@dataclass
class HttpGatewayRouteHeader(PropertyType):
    name: DslValue[str] | None = None
    invert: DslValue[bool] | None = None
    match: DslValue[HttpGatewayRouteHeaderMatch] | None = None


@dataclass
class HttpGatewayRouteHeaderMatch(PropertyType):
    exact: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    range: DslValue[GatewayRouteRangeMatch] | None = None
    regex: DslValue[str] | None = None
    suffix: DslValue[str] | None = None


@dataclass
class HttpGatewayRouteMatch(PropertyType):
    headers: list[DslValue[HttpGatewayRouteHeader]] = field(default_factory=list)
    hostname: DslValue[GatewayRouteHostnameMatch] | None = None
    method: DslValue[str] | None = None
    path: DslValue[HttpPathMatch] | None = None
    port: DslValue[int] | None = None
    prefix: DslValue[str] | None = None
    query_parameters: list[DslValue[QueryParameter]] = field(default_factory=list)


@dataclass
class HttpGatewayRoutePathRewrite(PropertyType):
    exact: DslValue[str] | None = None


@dataclass
class HttpGatewayRoutePrefixRewrite(PropertyType):
    default_prefix: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class HttpGatewayRouteRewrite(PropertyType):
    hostname: DslValue[GatewayRouteHostnameRewrite] | None = None
    path: DslValue[HttpGatewayRoutePathRewrite] | None = None
    prefix: DslValue[HttpGatewayRoutePrefixRewrite] | None = None


@dataclass
class HttpPathMatch(PropertyType):
    exact: DslValue[str] | None = None
    regex: DslValue[str] | None = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    exact: DslValue[str] | None = None


@dataclass
class QueryParameter(PropertyType):
    name: DslValue[str] | None = None
    match: DslValue[HttpQueryParameterMatch] | None = None
