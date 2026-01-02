"""PropertyTypes for AWS::Glue::Classifier."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CsvClassifier(PropertyType):
    allow_single_column: bool | None = None
    contains_custom_datatype: list[String] = field(default_factory=list)
    contains_header: str | None = None
    custom_datatype_configured: bool | None = None
    delimiter: str | None = None
    disable_value_trimming: bool | None = None
    header: list[String] = field(default_factory=list)
    name: str | None = None
    quote_symbol: str | None = None


@dataclass
class GrokClassifier(PropertyType):
    classification: str | None = None
    grok_pattern: str | None = None
    custom_patterns: str | None = None
    name: str | None = None


@dataclass
class JsonClassifier(PropertyType):
    json_path: str | None = None
    name: str | None = None


@dataclass
class XMLClassifier(PropertyType):
    classification: str | None = None
    row_tag: str | None = None
    name: str | None = None
