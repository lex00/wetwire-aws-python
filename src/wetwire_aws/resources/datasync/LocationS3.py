"""PropertyTypes for AWS::DataSync::LocationS3."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Config(PropertyType):
    bucket_access_role_arn: str | None = None
