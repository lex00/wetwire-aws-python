"""PropertyTypes for AWS::OpenSearchServerless::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Index(PropertyType):
    knn: bool | None = None
    knn_algo_param_ef_search: int | None = None
    refresh_interval: str | None = None


@dataclass
class IndexSettings(PropertyType):
    index: Index | None = None


@dataclass
class Mappings(PropertyType):
    properties: dict[str, PropertyMapping] = field(default_factory=dict)


@dataclass
class Method(PropertyType):
    name: str | None = None
    engine: str | None = None
    parameters: Parameters | None = None
    space_type: str | None = None


@dataclass
class Parameters(PropertyType):
    ef_construction: int | None = None
    m: int | None = None


@dataclass
class PropertyMapping(PropertyType):
    type_: str | None = None
    dimension: int | None = None
    index: bool | None = None
    method: Method | None = None
    properties: dict[str, PropertyMapping] = field(default_factory=dict)
    value: str | None = None
