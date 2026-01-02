"""PropertyTypes for AWS::DataPipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Field(PropertyType):
    key: str | None = None
    ref_value: str | None = None
    string_value: str | None = None


@dataclass
class ParameterAttribute(PropertyType):
    key: str | None = None
    string_value: str | None = None


@dataclass
class ParameterObject(PropertyType):
    attributes: list[ParameterAttribute] = field(default_factory=list)
    id: str | None = None


@dataclass
class ParameterValue(PropertyType):
    id: str | None = None
    string_value: str | None = None


@dataclass
class PipelineObject(PropertyType):
    fields: list[Field] = field(default_factory=list)
    id: str | None = None
    name: str | None = None


@dataclass
class PipelineTag(PropertyType):
    key: str | None = None
    value: str | None = None
