"""PropertyTypes for AWS::WorkSpacesWeb::SessionLogger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EventFilter(PropertyType):
    all: dict[str, Any] | None = None
    include: list[String] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    s3: S3LogConfiguration | None = None


@dataclass
class S3LogConfiguration(PropertyType):
    bucket: str | None = None
    folder_structure: str | None = None
    log_file_format: str | None = None
    bucket_owner: str | None = None
    key_prefix: str | None = None
