"""PropertyTypes for AWS::QBusiness::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DocumentAttributeConfiguration(PropertyType):
    name: DslValue[str] | None = None
    search: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class IndexCapacityConfiguration(PropertyType):
    units: DslValue[float] | None = None


@dataclass
class IndexStatistics(PropertyType):
    text_document_statistics: DslValue[TextDocumentStatistics] | None = None


@dataclass
class TextDocumentStatistics(PropertyType):
    indexed_text_bytes: DslValue[float] | None = None
    indexed_text_document_count: DslValue[float] | None = None
