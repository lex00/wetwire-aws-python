"""PropertyTypes for AWS::S3::AccessGrant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessGrantsLocationConfiguration(PropertyType):
    s3_sub_prefix: DslValue[str] | None = None


@dataclass
class Grantee(PropertyType):
    grantee_identifier: DslValue[str] | None = None
    grantee_type: DslValue[str] | None = None
