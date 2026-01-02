"""PropertyTypes for AWS::Omics::AnnotationStore."""

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


@dataclass
class StoreOptions(PropertyType):
    tsv_store_options: TsvStoreOptions | None = None


@dataclass
class TsvStoreOptions(PropertyType):
    annotation_type: str | None = None
    format_to_header: dict[str, String] = field(default_factory=dict)
    schema: dict[str, Any] | None = None
