"""PropertyTypes for AWS::MPA::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IamIdentityCenter(PropertyType):
    instance_arn: str | None = None
    region: str | None = None
    approval_portal_url: str | None = None


@dataclass
class IdentitySourceParameters(PropertyType):
    iam_identity_center: IamIdentityCenter | None = None
