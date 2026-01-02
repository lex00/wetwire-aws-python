"""PropertyTypes for AWS::EC2::RouteServerPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BgpOptions(PropertyType):
    peer_asn: int | None = None
    peer_liveness_detection: str | None = None
