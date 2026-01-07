"""PropertyTypes for AWS::NetworkFirewall::TLSInspectionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Address(PropertyType):
    address_definition: DslValue[str] | None = None


@dataclass
class CheckCertificateRevocationStatus(PropertyType):
    revoked_status_action: DslValue[str] | None = None
    unknown_status_action: DslValue[str] | None = None


@dataclass
class PortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class ServerCertificate(PropertyType):
    resource_arn: DslValue[str] | None = None


@dataclass
class ServerCertificateConfiguration(PropertyType):
    certificate_authority_arn: DslValue[str] | None = None
    check_certificate_revocation_status: (
        DslValue[CheckCertificateRevocationStatus] | None
    ) = None
    scopes: list[DslValue[ServerCertificateScope]] = field(default_factory=list)
    server_certificates: list[DslValue[ServerCertificate]] = field(default_factory=list)


@dataclass
class ServerCertificateScope(PropertyType):
    destination_ports: list[DslValue[PortRange]] = field(default_factory=list)
    destinations: list[DslValue[Address]] = field(default_factory=list)
    protocols: list[DslValue[int]] = field(default_factory=list)
    source_ports: list[DslValue[PortRange]] = field(default_factory=list)
    sources: list[DslValue[Address]] = field(default_factory=list)


@dataclass
class TLSInspectionConfiguration(PropertyType):
    server_certificate_configurations: list[
        DslValue[ServerCertificateConfiguration]
    ] = field(default_factory=list)
