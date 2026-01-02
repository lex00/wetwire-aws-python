"""PropertyTypes for AWS::Grafana::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssertionAttributes(PropertyType):
    email: str | None = None
    groups: str | None = None
    login: str | None = None
    name: str | None = None
    org: str | None = None
    role: str | None = None


@dataclass
class IdpMetadata(PropertyType):
    url: str | None = None
    xml: str | None = None


@dataclass
class NetworkAccessControl(PropertyType):
    prefix_list_ids: list[String] = field(default_factory=list)
    vpce_ids: list[String] = field(default_factory=list)


@dataclass
class RoleValues(PropertyType):
    admin: list[String] = field(default_factory=list)
    editor: list[String] = field(default_factory=list)


@dataclass
class SamlConfiguration(PropertyType):
    idp_metadata: IdpMetadata | None = None
    allowed_organizations: list[String] = field(default_factory=list)
    assertion_attributes: AssertionAttributes | None = None
    login_validity_duration: float | None = None
    role_values: RoleValues | None = None


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
