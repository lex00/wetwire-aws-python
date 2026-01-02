"""PropertyTypes for AWS::FSx::StorageVirtualMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActiveDirectoryConfiguration(PropertyType):
    net_bios_name: str | None = None
    self_managed_active_directory_configuration: (
        SelfManagedActiveDirectoryConfiguration | None
    ) = None


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    dns_ips: list[String] = field(default_factory=list)
    domain_join_service_account_secret: str | None = None
    domain_name: str | None = None
    file_system_administrators_group: str | None = None
    organizational_unit_distinguished_name: str | None = None
    password: str | None = None
    user_name: str | None = None
