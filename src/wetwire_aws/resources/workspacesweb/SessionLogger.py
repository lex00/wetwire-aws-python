"""PropertyTypes for AWS::WorkSpacesWeb::SessionLogger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EventFilter(PropertyType):
    all: DslValue[dict[str, Any]] | None = None
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    s3: DslValue[S3LogConfiguration] | None = None


@dataclass
class S3LogConfiguration(PropertyType):
    bucket: DslValue[str] | None = None
    folder_structure: DslValue[str] | None = None
    log_file_format: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None
