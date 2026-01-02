"""PropertyTypes for AWS::MediaConnect::FlowEntitlement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Encryption(PropertyType):
    algorithm: str | None = None
    role_arn: str | None = None
    constant_initialization_vector: str | None = None
    device_id: str | None = None
    key_type: str | None = None
    region: str | None = None
    resource_id: str | None = None
    secret_arn: str | None = None
    url: str | None = None
