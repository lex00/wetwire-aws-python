"""PropertyTypes for AWS::Omics::VariantStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ReferenceItem(PropertyType):
    reference_arn: DslValue[str] | None = None


@dataclass
class SseConfig(PropertyType):
    type_: DslValue[str] | None = None
    key_arn: DslValue[str] | None = None
