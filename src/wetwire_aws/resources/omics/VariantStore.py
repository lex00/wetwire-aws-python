"""PropertyTypes for AWS::Omics::VariantStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ReferenceItem(PropertyType):
    reference_arn: str | None = None


@dataclass
class SseConfig(PropertyType):
    type_: str | None = None
    key_arn: str | None = None
