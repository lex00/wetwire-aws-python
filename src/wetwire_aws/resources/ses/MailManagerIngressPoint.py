"""PropertyTypes for AWS::SES::MailManagerIngressPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IngressPointConfiguration(PropertyType):
    secret_arn: str | None = None
    smtp_password: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    private_network_configuration: PrivateNetworkConfiguration | None = None
    public_network_configuration: PublicNetworkConfiguration | None = None


@dataclass
class PrivateNetworkConfiguration(PropertyType):
    vpc_endpoint_id: str | None = None


@dataclass
class PublicNetworkConfiguration(PropertyType):
    ip_type: dict[str, Any] | None = None
