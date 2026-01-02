"""PropertyTypes for AWS::EKS::Addon."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NamespaceConfig(PropertyType):
    namespace: str | None = None


@dataclass
class PodIdentityAssociation(PropertyType):
    role_arn: str | None = None
    service_account: str | None = None
