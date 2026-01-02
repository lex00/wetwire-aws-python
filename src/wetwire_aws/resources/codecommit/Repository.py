"""PropertyTypes for AWS::CodeCommit::Repository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Code(PropertyType):
    s3: S3 | None = None
    branch_name: str | None = None


@dataclass
class RepositoryTrigger(PropertyType):
    destination_arn: str | None = None
    events: list[String] = field(default_factory=list)
    name: str | None = None
    branches: list[String] = field(default_factory=list)
    custom_data: str | None = None


@dataclass
class S3(PropertyType):
    bucket: str | None = None
    key: str | None = None
    object_version: str | None = None
