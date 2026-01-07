"""PropertyTypes for AWS::AppRunner::VpcIngressConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IngressVpcConfiguration(PropertyType):
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_id: DslValue[str] | None = None
