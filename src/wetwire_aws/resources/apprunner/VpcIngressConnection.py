"""PropertyTypes for AWS::AppRunner::VpcIngressConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IngressVpcConfiguration(PropertyType):
    vpc_endpoint_id: str | None = None
    vpc_id: str | None = None
