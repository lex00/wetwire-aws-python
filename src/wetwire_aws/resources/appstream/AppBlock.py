"""PropertyTypes for AWS::AppStream::AppBlock."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Location(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None


@dataclass
class ScriptDetails(PropertyType):
    executable_path: str | None = None
    script_s3_location: S3Location | None = None
    timeout_in_seconds: int | None = None
    executable_parameters: str | None = None
