"""PropertyTypes for AWS::MPA::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IamIdentityCenter(PropertyType):
    instance_arn: DslValue[str] | None = None
    region: DslValue[str] | None = None
    approval_portal_url: DslValue[str] | None = None


@dataclass
class IdentitySourceParameters(PropertyType):
    iam_identity_center: DslValue[IamIdentityCenter] | None = None
