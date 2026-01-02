"""PropertyTypes for AWS::MediaPackageV2::OriginEndpointPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CdnAuthConfiguration(PropertyType):
    cdn_identifier_secret_arns: list[String] = field(default_factory=list)
    secrets_role_arn: str | None = None
