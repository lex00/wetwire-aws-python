"""PropertyTypes for AWS::Grafana::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssertionAttributes(PropertyType):
    email: DslValue[str] | None = None
    groups: DslValue[str] | None = None
    login: DslValue[str] | None = None
    name: DslValue[str] | None = None
    org: DslValue[str] | None = None
    role: DslValue[str] | None = None


@dataclass
class IdpMetadata(PropertyType):
    url: DslValue[str] | None = None
    xml: DslValue[str] | None = None


@dataclass
class NetworkAccessControl(PropertyType):
    prefix_list_ids: list[DslValue[str]] = field(default_factory=list)
    vpce_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RoleValues(PropertyType):
    admin: list[DslValue[str]] = field(default_factory=list)
    editor: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SamlConfiguration(PropertyType):
    idp_metadata: DslValue[IdpMetadata] | None = None
    allowed_organizations: list[DslValue[str]] = field(default_factory=list)
    assertion_attributes: DslValue[AssertionAttributes] | None = None
    login_validity_duration: DslValue[float] | None = None
    role_values: DslValue[RoleValues] | None = None


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
