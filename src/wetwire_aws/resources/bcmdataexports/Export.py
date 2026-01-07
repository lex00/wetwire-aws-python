"""PropertyTypes for AWS::BCMDataExports::Export."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataQuery(PropertyType):
    query_statement: DslValue[str] | None = None
    table_configurations: DslValue[dict[str, Any]] | None = None


@dataclass
class DestinationConfigurations(PropertyType):
    s3_destination: DslValue[S3Destination] | None = None


@dataclass
class Export(PropertyType):
    data_query: DslValue[DataQuery] | None = None
    destination_configurations: DslValue[DestinationConfigurations] | None = None
    name: DslValue[str] | None = None
    refresh_cadence: DslValue[RefreshCadence] | None = None
    description: DslValue[str] | None = None
    export_arn: DslValue[str] | None = None


@dataclass
class RefreshCadence(PropertyType):
    frequency: DslValue[str] | None = None


@dataclass
class ResourceTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class S3Destination(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_output_configurations: DslValue[S3OutputConfigurations] | None = None
    s3_prefix: DslValue[str] | None = None
    s3_region: DslValue[str] | None = None


@dataclass
class S3OutputConfigurations(PropertyType):
    compression: DslValue[str] | None = None
    format: DslValue[str] | None = None
    output_type: DslValue[str] | None = None
    overwrite: DslValue[str] | None = None
