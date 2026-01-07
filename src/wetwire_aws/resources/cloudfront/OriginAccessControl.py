"""PropertyTypes for AWS::CloudFront::OriginAccessControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OriginAccessControlConfig(PropertyType):
    name: DslValue[str] | None = None
    origin_access_control_origin_type: DslValue[str] | None = None
    signing_behavior: DslValue[str] | None = None
    signing_protocol: DslValue[str] | None = None
    description: DslValue[str] | None = None
