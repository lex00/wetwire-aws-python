"""PropertyTypes for AWS::Lambda::LayerVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Content(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None
