"""PropertyTypes for AWS::ElasticLoadBalancingV2::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Matcher(PropertyType):
    grpc_code: str | None = None
    http_code: str | None = None


@dataclass
class TargetDescription(PropertyType):
    id: str | None = None
    availability_zone: str | None = None
    port: int | None = None
    quic_server_id: str | None = None


@dataclass
class TargetGroupAttribute(PropertyType):
    key: str | None = None
    value: str | None = None
