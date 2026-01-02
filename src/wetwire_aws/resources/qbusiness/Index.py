"""PropertyTypes for AWS::QBusiness::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DocumentAttributeConfiguration(PropertyType):
    name: str | None = None
    search: str | None = None
    type_: str | None = None


@dataclass
class IndexCapacityConfiguration(PropertyType):
    units: float | None = None


@dataclass
class IndexStatistics(PropertyType):
    text_document_statistics: TextDocumentStatistics | None = None


@dataclass
class TextDocumentStatistics(PropertyType):
    indexed_text_bytes: float | None = None
    indexed_text_document_count: float | None = None
