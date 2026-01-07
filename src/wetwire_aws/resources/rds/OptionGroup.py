"""PropertyTypes for AWS::RDS::OptionGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "db_security_group_memberships": "DBSecurityGroupMemberships",
    }

    option_name: DslValue[str] | None = None
    db_security_group_memberships: list[DslValue[str]] = field(default_factory=list)
    option_settings: list[DslValue[OptionSetting]] = field(default_factory=list)
    option_version: DslValue[str] | None = None
    port: DslValue[int] | None = None
    vpc_security_group_memberships: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OptionSetting(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
