"""PropertyTypes for AWS::Glue::Classifier."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CsvClassifier(PropertyType):
    allow_single_column: DslValue[bool] | None = None
    contains_custom_datatype: list[DslValue[str]] = field(default_factory=list)
    contains_header: DslValue[str] | None = None
    custom_datatype_configured: DslValue[bool] | None = None
    delimiter: DslValue[str] | None = None
    disable_value_trimming: DslValue[bool] | None = None
    header: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    quote_symbol: DslValue[str] | None = None


@dataclass
class GrokClassifier(PropertyType):
    classification: DslValue[str] | None = None
    grok_pattern: DslValue[str] | None = None
    custom_patterns: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class JsonClassifier(PropertyType):
    json_path: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class XMLClassifier(PropertyType):
    classification: DslValue[str] | None = None
    row_tag: DslValue[str] | None = None
    name: DslValue[str] | None = None
