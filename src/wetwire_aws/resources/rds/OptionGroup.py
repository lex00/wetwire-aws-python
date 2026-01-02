"""PropertyTypes for AWS::RDS::OptionGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "db_security_group_memberships": "DBSecurityGroupMemberships",
    }

    option_name: str | None = None
    db_security_group_memberships: list[String] = field(default_factory=list)
    option_settings: list[OptionSetting] = field(default_factory=list)
    option_version: str | None = None
    port: int | None = None
    vpc_security_group_memberships: list[String] = field(default_factory=list)


@dataclass
class OptionSetting(PropertyType):
    name: str | None = None
    value: str | None = None
