"""PropertyTypes for AWS::CloudFront::KeyValueStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ImportSource(PropertyType):
    source_arn: DslValue[str] | None = None
    source_type: DslValue[str] | None = None
