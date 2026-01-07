"""PropertyTypes for AWS::DataPipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Field(PropertyType):
    key: DslValue[str] | None = None
    ref_value: DslValue[str] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class ParameterAttribute(PropertyType):
    key: DslValue[str] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class ParameterObject(PropertyType):
    attributes: list[DslValue[ParameterAttribute]] = field(default_factory=list)
    id: DslValue[str] | None = None


@dataclass
class ParameterValue(PropertyType):
    id: DslValue[str] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class PipelineObject(PropertyType):
    fields: list[DslValue[Field]] = field(default_factory=list)
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class PipelineTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
