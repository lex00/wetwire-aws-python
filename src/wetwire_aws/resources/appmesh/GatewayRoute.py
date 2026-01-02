"""PropertyTypes for AWS::AppMesh::GatewayRoute."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GatewayRouteHostnameMatch(PropertyType):
    exact: str | None = None
    suffix: str | None = None


@dataclass
class GatewayRouteHostnameRewrite(PropertyType):
    default_target_hostname: str | None = None


@dataclass
class GatewayRouteMetadataMatch(PropertyType):
    exact: str | None = None
    prefix: str | None = None
    range: GatewayRouteRangeMatch | None = None
    regex: str | None = None
    suffix: str | None = None


@dataclass
class GatewayRouteRangeMatch(PropertyType):
    end: int | None = None
    start: int | None = None


@dataclass
class GatewayRouteSpec(PropertyType):
    grpc_route: GrpcGatewayRoute | None = None
    http2_route: HttpGatewayRoute | None = None
    http_route: HttpGatewayRoute | None = None
    priority: int | None = None


@dataclass
class GatewayRouteTarget(PropertyType):
    virtual_service: GatewayRouteVirtualService | None = None
    port: int | None = None


@dataclass
class GatewayRouteVirtualService(PropertyType):
    virtual_service_name: str | None = None


@dataclass
class GrpcGatewayRoute(PropertyType):
    action: GrpcGatewayRouteAction | None = None
    match: GrpcGatewayRouteMatch | None = None


@dataclass
class GrpcGatewayRouteAction(PropertyType):
    target: GatewayRouteTarget | None = None
    rewrite: GrpcGatewayRouteRewrite | None = None


@dataclass
class GrpcGatewayRouteMatch(PropertyType):
    hostname: GatewayRouteHostnameMatch | None = None
    metadata: list[GrpcGatewayRouteMetadata] = field(default_factory=list)
    port: int | None = None
    service_name: str | None = None


@dataclass
class GrpcGatewayRouteMetadata(PropertyType):
    name: str | None = None
    invert: bool | None = None
    match: GatewayRouteMetadataMatch | None = None


@dataclass
class GrpcGatewayRouteRewrite(PropertyType):
    hostname: GatewayRouteHostnameRewrite | None = None


@dataclass
class HttpGatewayRoute(PropertyType):
    action: HttpGatewayRouteAction | None = None
    match: HttpGatewayRouteMatch | None = None


@dataclass
class HttpGatewayRouteAction(PropertyType):
    target: GatewayRouteTarget | None = None
    rewrite: HttpGatewayRouteRewrite | None = None


@dataclass
class HttpGatewayRouteHeader(PropertyType):
    name: str | None = None
    invert: bool | None = None
    match: HttpGatewayRouteHeaderMatch | None = None


@dataclass
class HttpGatewayRouteHeaderMatch(PropertyType):
    exact: str | None = None
    prefix: str | None = None
    range: GatewayRouteRangeMatch | None = None
    regex: str | None = None
    suffix: str | None = None


@dataclass
class HttpGatewayRouteMatch(PropertyType):
    headers: list[HttpGatewayRouteHeader] = field(default_factory=list)
    hostname: GatewayRouteHostnameMatch | None = None
    method: str | None = None
    path: HttpPathMatch | None = None
    port: int | None = None
    prefix: str | None = None
    query_parameters: list[QueryParameter] = field(default_factory=list)


@dataclass
class HttpGatewayRoutePathRewrite(PropertyType):
    exact: str | None = None


@dataclass
class HttpGatewayRoutePrefixRewrite(PropertyType):
    default_prefix: str | None = None
    value: str | None = None


@dataclass
class HttpGatewayRouteRewrite(PropertyType):
    hostname: GatewayRouteHostnameRewrite | None = None
    path: HttpGatewayRoutePathRewrite | None = None
    prefix: HttpGatewayRoutePrefixRewrite | None = None


@dataclass
class HttpPathMatch(PropertyType):
    exact: str | None = None
    regex: str | None = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    exact: str | None = None


@dataclass
class QueryParameter(PropertyType):
    name: str | None = None
    match: HttpQueryParameterMatch | None = None
