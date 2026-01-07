"""PropertyTypes for AWS::CodeStar::GitHubRepository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Code(PropertyType):
    s3: DslValue[S3] | None = None


@dataclass
class S3(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    object_version: DslValue[str] | None = None
