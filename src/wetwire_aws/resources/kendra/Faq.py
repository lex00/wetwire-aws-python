"""PropertyTypes for AWS::Kendra::Faq."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Path(PropertyType):
    bucket: str | None = None
    key: str | None = None
