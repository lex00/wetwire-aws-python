"""PropertyTypes for AWS::Route53RecoveryControl::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ClusterEndpoint(PropertyType):
    endpoint: DslValue[str] | None = None
    region: DslValue[str] | None = None
