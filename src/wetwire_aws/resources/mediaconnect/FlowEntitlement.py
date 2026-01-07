"""PropertyTypes for AWS::MediaConnect::FlowEntitlement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Encryption(PropertyType):
    algorithm: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    device_id: DslValue[str] | None = None
    key_type: DslValue[str] | None = None
    region: DslValue[str] | None = None
    resource_id: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    url: DslValue[str] | None = None
