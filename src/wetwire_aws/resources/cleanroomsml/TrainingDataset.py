"""PropertyTypes for AWS::CleanRoomsML::TrainingDataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ColumnSchema(PropertyType):
    column_name: str | None = None
    column_types: list[String] = field(default_factory=list)


@dataclass
class DataSource(PropertyType):
    glue_data_source: GlueDataSource | None = None


@dataclass
class Dataset(PropertyType):
    input_config: DatasetInputConfig | None = None
    type_: str | None = None


@dataclass
class DatasetInputConfig(PropertyType):
    data_source: DataSource | None = None
    schema: list[ColumnSchema] = field(default_factory=list)


@dataclass
class GlueDataSource(PropertyType):
    database_name: str | None = None
    table_name: str | None = None
    catalog_id: str | None = None
