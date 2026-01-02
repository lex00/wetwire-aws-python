"""PropertyTypes for AWS::MediaConnect::FlowSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Encryption(PropertyType):
    role_arn: str | None = None
    algorithm: str | None = None
    constant_initialization_vector: str | None = None
    device_id: str | None = None
    key_type: str | None = None
    region: str | None = None
    resource_id: str | None = None
    secret_arn: str | None = None
    url: str | None = None


@dataclass
class GatewayBridgeSource(PropertyType):
    bridge_arn: str | None = None
    vpc_interface_attachment: VpcInterfaceAttachment | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: str | None = None
