"""PropertyTypes for AWS::QBusiness::Retriever."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class KendraIndexConfiguration(PropertyType):
    index_id: str | None = None


@dataclass
class NativeIndexConfiguration(PropertyType):
    index_id: str | None = None


@dataclass
class RetrieverConfiguration(PropertyType):
    kendra_index_configuration: KendraIndexConfiguration | None = None
    native_index_configuration: NativeIndexConfiguration | None = None
