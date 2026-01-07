"""PropertyTypes for AWS::SES::MailManagerIngressPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IngressPointConfiguration(PropertyType):
    secret_arn: DslValue[str] | None = None
    smtp_password: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    private_network_configuration: DslValue[PrivateNetworkConfiguration] | None = None
    public_network_configuration: DslValue[PublicNetworkConfiguration] | None = None


@dataclass
class PrivateNetworkConfiguration(PropertyType):
    vpc_endpoint_id: DslValue[str] | None = None


@dataclass
class PublicNetworkConfiguration(PropertyType):
    ip_type: DslValue[dict[str, Any]] | None = None
