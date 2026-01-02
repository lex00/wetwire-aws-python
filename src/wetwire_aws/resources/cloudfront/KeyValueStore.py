"""PropertyTypes for AWS::CloudFront::KeyValueStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ImportSource(PropertyType):
    source_arn: str | None = None
    source_type: str | None = None
