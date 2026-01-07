"""PropertyTypes for AWS::EC2::RouteServerPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BgpOptions(PropertyType):
    peer_asn: DslValue[int] | None = None
    peer_liveness_detection: DslValue[str] | None = None
