"""PropertyTypes for AWS::EKS::Capability."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ArgoCd(PropertyType):
    aws_idc: AwsIdc | None = None
    namespace: str | None = None
    network_access: NetworkAccess | None = None
    rbac_role_mappings: list[ArgoCdRoleMapping] = field(default_factory=list)
    server_url: str | None = None


@dataclass
class ArgoCdRoleMapping(PropertyType):
    identities: list[SsoIdentity] = field(default_factory=list)
    role: str | None = None


@dataclass
class AwsIdc(PropertyType):
    idc_instance_arn: str | None = None
    idc_managed_application_arn: str | None = None
    idc_region: str | None = None


@dataclass
class CapabilityConfiguration(PropertyType):
    argo_cd: ArgoCd | None = None


@dataclass
class NetworkAccess(PropertyType):
    vpce_ids: list[String] = field(default_factory=list)


@dataclass
class SsoIdentity(PropertyType):
    id: str | None = None
    type_: str | None = None
