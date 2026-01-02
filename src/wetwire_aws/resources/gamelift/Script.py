"""PropertyTypes for AWS::GameLift::Script."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    role_arn: str | None = None
    object_version: str | None = None
