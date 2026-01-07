"""PropertyTypes for AWS::Kendra::Faq."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class S3Path(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
