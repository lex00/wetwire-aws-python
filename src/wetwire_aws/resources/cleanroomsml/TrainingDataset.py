"""PropertyTypes for AWS::CleanRoomsML::TrainingDataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ColumnSchema(PropertyType):
    column_name: DslValue[str] | None = None
    column_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataSource(PropertyType):
    glue_data_source: DslValue[GlueDataSource] | None = None


@dataclass
class Dataset(PropertyType):
    input_config: DslValue[DatasetInputConfig] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DatasetInputConfig(PropertyType):
    data_source: DslValue[DataSource] | None = None
    schema: list[DslValue[ColumnSchema]] = field(default_factory=list)


@dataclass
class GlueDataSource(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    catalog_id: DslValue[str] | None = None
