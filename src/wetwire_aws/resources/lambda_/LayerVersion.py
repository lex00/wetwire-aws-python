"""PropertyTypes for AWS::Lambda::LayerVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Content(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None
    s3_object_version: str | None = None
