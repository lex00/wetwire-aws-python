"""PropertyTypes for AWS::FSx::StorageVirtualMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActiveDirectoryConfiguration(PropertyType):
    net_bios_name: DslValue[str] | None = None
    self_managed_active_directory_configuration: (
        DslValue[SelfManagedActiveDirectoryConfiguration] | None
    ) = None


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    dns_ips: list[DslValue[str]] = field(default_factory=list)
    domain_join_service_account_secret: DslValue[str] | None = None
    domain_name: DslValue[str] | None = None
    file_system_administrators_group: DslValue[str] | None = None
    organizational_unit_distinguished_name: DslValue[str] | None = None
    password: DslValue[str] | None = None
    user_name: DslValue[str] | None = None
