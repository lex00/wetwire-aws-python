"""PropertyTypes for AWS::S3::AccessPoint."""

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
class VpcConfiguration(PropertyType):
    vpc_id: str | None = None
