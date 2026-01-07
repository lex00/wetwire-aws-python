"""PropertyTypes for AWS::CodeCommit::Repository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Code(PropertyType):
    s3: DslValue[S3] | None = None
    branch_name: DslValue[str] | None = None


@dataclass
class RepositoryTrigger(PropertyType):
    destination_arn: DslValue[str] | None = None
    events: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    branches: list[DslValue[str]] = field(default_factory=list)
    custom_data: DslValue[str] | None = None


@dataclass
class S3(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    object_version: DslValue[str] | None = None
