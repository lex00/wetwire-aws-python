"""PropertyTypes for AWS::GlobalAccelerator::EndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EndpointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_ip_preservation_enabled": "ClientIPPreservationEnabled",
    }

    endpoint_id: DslValue[str] | None = None
    attachment_arn: DslValue[str] | None = None
    client_ip_preservation_enabled: DslValue[bool] | None = None
    weight: DslValue[int] | None = None


@dataclass
class PortOverride(PropertyType):
    endpoint_port: DslValue[int] | None = None
    listener_port: DslValue[int] | None = None
