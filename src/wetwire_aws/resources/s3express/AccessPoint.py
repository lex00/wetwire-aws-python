"""PropertyTypes for AWS::S3Express::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: DslValue[bool] | None = None
    block_public_policy: DslValue[bool] | None = None
    ignore_public_acls: DslValue[bool] | None = None
    restrict_public_buckets: DslValue[bool] | None = None


@dataclass
class Scope(PropertyType):
    permissions: list[DslValue[str]] = field(default_factory=list)
    prefixes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VpcConfiguration(PropertyType):
    vpc_id: DslValue[str] | None = None
