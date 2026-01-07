"""PropertyTypes for AWS::EKS::Capability."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ArgoCd(PropertyType):
    aws_idc: DslValue[AwsIdc] | None = None
    namespace: DslValue[str] | None = None
    network_access: DslValue[NetworkAccess] | None = None
    rbac_role_mappings: list[DslValue[ArgoCdRoleMapping]] = field(default_factory=list)
    server_url: DslValue[str] | None = None


@dataclass
class ArgoCdRoleMapping(PropertyType):
    identities: list[DslValue[SsoIdentity]] = field(default_factory=list)
    role: DslValue[str] | None = None


@dataclass
class AwsIdc(PropertyType):
    idc_instance_arn: DslValue[str] | None = None
    idc_managed_application_arn: DslValue[str] | None = None
    idc_region: DslValue[str] | None = None


@dataclass
class CapabilityConfiguration(PropertyType):
    argo_cd: DslValue[ArgoCd] | None = None


@dataclass
class NetworkAccess(PropertyType):
    vpce_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SsoIdentity(PropertyType):
    id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
