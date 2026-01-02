"""PropertyTypes for AWS::CodeStar::GitHubRepository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Code(PropertyType):
    s3: S3 | None = None


@dataclass
class S3(PropertyType):
    bucket: str | None = None
    key: str | None = None
    object_version: str | None = None
