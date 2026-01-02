"""PropertyTypes for AWS::AppStream::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Location(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None
