"""PropertyTypes for AWS::SSO::PermissionSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomerManagedPolicyReference(PropertyType):
    name: str | None = None
    path: str | None = None


@dataclass
class PermissionsBoundary(PropertyType):
    customer_managed_policy_reference: CustomerManagedPolicyReference | None = None
    managed_policy_arn: str | None = None
