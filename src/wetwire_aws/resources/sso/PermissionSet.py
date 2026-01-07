"""PropertyTypes for AWS::SSO::PermissionSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomerManagedPolicyReference(PropertyType):
    name: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class PermissionsBoundary(PropertyType):
    customer_managed_policy_reference: (
        DslValue[CustomerManagedPolicyReference] | None
    ) = None
    managed_policy_arn: DslValue[str] | None = None
