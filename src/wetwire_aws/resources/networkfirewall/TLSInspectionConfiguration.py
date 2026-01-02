"""PropertyTypes for AWS::NetworkFirewall::TLSInspectionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Address(PropertyType):
    address_definition: str | None = None


@dataclass
class CheckCertificateRevocationStatus(PropertyType):
    revoked_status_action: str | None = None
    unknown_status_action: str | None = None


@dataclass
class PortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class ServerCertificate(PropertyType):
    resource_arn: str | None = None


@dataclass
class ServerCertificateConfiguration(PropertyType):
    certificate_authority_arn: str | None = None
    check_certificate_revocation_status: CheckCertificateRevocationStatus | None = None
    scopes: list[ServerCertificateScope] = field(default_factory=list)
    server_certificates: list[ServerCertificate] = field(default_factory=list)


@dataclass
class ServerCertificateScope(PropertyType):
    destination_ports: list[PortRange] = field(default_factory=list)
    destinations: list[Address] = field(default_factory=list)
    protocols: list[Integer] = field(default_factory=list)
    source_ports: list[PortRange] = field(default_factory=list)
    sources: list[Address] = field(default_factory=list)


@dataclass
class TLSInspectionConfiguration(PropertyType):
    server_certificate_configurations: list[ServerCertificateConfiguration] = field(
        default_factory=list
    )
