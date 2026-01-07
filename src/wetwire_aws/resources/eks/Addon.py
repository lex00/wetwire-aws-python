"""PropertyTypes for AWS::EKS::Addon."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NamespaceConfig(PropertyType):
    namespace: DslValue[str] | None = None


@dataclass
class PodIdentityAssociation(PropertyType):
    role_arn: DslValue[str] | None = None
    service_account: DslValue[str] | None = None
