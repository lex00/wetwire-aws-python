"""PropertyTypes for AWS::QBusiness::Retriever."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class KendraIndexConfiguration(PropertyType):
    index_id: DslValue[str] | None = None


@dataclass
class NativeIndexConfiguration(PropertyType):
    index_id: DslValue[str] | None = None


@dataclass
class RetrieverConfiguration(PropertyType):
    kendra_index_configuration: DslValue[KendraIndexConfiguration] | None = None
    native_index_configuration: DslValue[NativeIndexConfiguration] | None = None
