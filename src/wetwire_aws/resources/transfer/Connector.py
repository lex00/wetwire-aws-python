"""PropertyTypes for AWS::Transfer::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class As2Config(PropertyType):
    basic_auth_secret_id: str | None = None
    compression: str | None = None
    encryption_algorithm: str | None = None
    local_profile_id: str | None = None
    mdn_response: str | None = None
    mdn_signing_algorithm: str | None = None
    message_subject: str | None = None
    partner_profile_id: str | None = None
    preserve_content_type: str | None = None
    signing_algorithm: str | None = None


@dataclass
class ConnectorEgressConfig(PropertyType):
    vpc_lattice: ConnectorVpcLatticeEgressConfig | None = None


@dataclass
class ConnectorVpcLatticeEgressConfig(PropertyType):
    resource_configuration_arn: str | None = None
    port_number: int | None = None


@dataclass
class SftpConfig(PropertyType):
    max_concurrent_connections: int | None = None
    trusted_host_keys: list[String] = field(default_factory=list)
    user_secret_id: str | None = None
