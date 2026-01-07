"""PropertyTypes for AWS::ElasticLoadBalancingV2::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Matcher(PropertyType):
    grpc_code: DslValue[str] | None = None
    http_code: DslValue[str] | None = None


@dataclass
class TargetDescription(PropertyType):
    id: DslValue[str] | None = None
    availability_zone: DslValue[str] | None = None
    port: DslValue[int] | None = None
    quic_server_id: DslValue[str] | None = None


@dataclass
class TargetGroupAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
