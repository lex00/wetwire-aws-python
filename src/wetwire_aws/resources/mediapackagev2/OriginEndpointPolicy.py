"""PropertyTypes for AWS::MediaPackageV2::OriginEndpointPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CdnAuthConfiguration(PropertyType):
    cdn_identifier_secret_arns: list[DslValue[str]] = field(default_factory=list)
    secrets_role_arn: DslValue[str] | None = None
