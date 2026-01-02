"""PropertyTypes for AWS::S3::MultiRegionAccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: bool | None = None
    block_public_policy: bool | None = None
    ignore_public_acls: bool | None = None
    restrict_public_buckets: bool | None = None


@dataclass
class Region(PropertyType):
    bucket: str | None = None
    bucket_account_id: str | None = None
