"""PropertyTypes for AWS::ElasticLoadBalancingV2::ListenerCertificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Certificate(PropertyType):
    certificate_arn: str | None = None
