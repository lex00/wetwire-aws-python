"""PropertyTypes for AWS::GlobalAccelerator::EndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndpointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_ip_preservation_enabled": "ClientIPPreservationEnabled",
    }

    endpoint_id: str | None = None
    attachment_arn: str | None = None
    client_ip_preservation_enabled: bool | None = None
    weight: int | None = None


@dataclass
class PortOverride(PropertyType):
    endpoint_port: int | None = None
    listener_port: int | None = None
