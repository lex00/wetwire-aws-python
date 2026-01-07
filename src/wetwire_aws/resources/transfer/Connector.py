"""PropertyTypes for AWS::Transfer::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class As2Config(PropertyType):
    basic_auth_secret_id: DslValue[str] | None = None
    compression: DslValue[str] | None = None
    encryption_algorithm: DslValue[str] | None = None
    local_profile_id: DslValue[str] | None = None
    mdn_response: DslValue[str] | None = None
    mdn_signing_algorithm: DslValue[str] | None = None
    message_subject: DslValue[str] | None = None
    partner_profile_id: DslValue[str] | None = None
    preserve_content_type: DslValue[str] | None = None
    signing_algorithm: DslValue[str] | None = None


@dataclass
class ConnectorEgressConfig(PropertyType):
    vpc_lattice: DslValue[ConnectorVpcLatticeEgressConfig] | None = None


@dataclass
class ConnectorVpcLatticeEgressConfig(PropertyType):
    resource_configuration_arn: DslValue[str] | None = None
    port_number: DslValue[int] | None = None


@dataclass
class SftpConfig(PropertyType):
    max_concurrent_connections: DslValue[int] | None = None
    trusted_host_keys: list[DslValue[str]] = field(default_factory=list)
    user_secret_id: DslValue[str] | None = None
