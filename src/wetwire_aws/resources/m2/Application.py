"""PropertyTypes for AWS::M2::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Definition(PropertyType):
    content: DslValue[str] | None = None
    s3_location: DslValue[str] | None = None
