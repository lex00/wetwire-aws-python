"""PropertyTypes for AWS::M2::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Definition(PropertyType):
    content: str | None = None
    s3_location: str | None = None
