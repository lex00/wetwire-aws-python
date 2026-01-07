"""PropertyTypes for AWS::AppStream::AppBlock."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class S3Location(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None


@dataclass
class ScriptDetails(PropertyType):
    executable_path: DslValue[str] | None = None
    script_s3_location: DslValue[S3Location] | None = None
    timeout_in_seconds: DslValue[int] | None = None
    executable_parameters: DslValue[str] | None = None
