"""PropertyTypes for AWS::S3::AccessGrant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessGrantsLocationConfiguration(PropertyType):
    s3_sub_prefix: str | None = None


@dataclass
class Grantee(PropertyType):
    grantee_identifier: str | None = None
    grantee_type: str | None = None
