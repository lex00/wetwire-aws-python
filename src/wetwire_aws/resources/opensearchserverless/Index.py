"""PropertyTypes for AWS::OpenSearchServerless::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Index(PropertyType):
    knn: DslValue[bool] | None = None
    knn_algo_param_ef_search: DslValue[int] | None = None
    refresh_interval: DslValue[str] | None = None


@dataclass
class IndexSettings(PropertyType):
    index: DslValue[Index] | None = None


@dataclass
class Mappings(PropertyType):
    properties: dict[str, DslValue[PropertyMapping]] = field(default_factory=dict)


@dataclass
class Method(PropertyType):
    name: DslValue[str] | None = None
    engine: DslValue[str] | None = None
    parameters: DslValue[Parameters] | None = None
    space_type: DslValue[str] | None = None


@dataclass
class Parameters(PropertyType):
    ef_construction: DslValue[int] | None = None
    m: DslValue[int] | None = None


@dataclass
class PropertyMapping(PropertyType):
    type_: DslValue[str] | None = None
    dimension: DslValue[int] | None = None
    index: DslValue[bool] | None = None
    method: DslValue[Method] | None = None
    properties: dict[str, DslValue[PropertyMapping]] = field(default_factory=dict)
    value: DslValue[str] | None = None
