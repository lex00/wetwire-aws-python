"""PropertyTypes for AWS::BCMDataExports::Export."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataQuery(PropertyType):
    query_statement: str | None = None
    table_configurations: dict[str, Any] | None = None


@dataclass
class DestinationConfigurations(PropertyType):
    s3_destination: S3Destination | None = None


@dataclass
class Export(PropertyType):
    data_query: DataQuery | None = None
    destination_configurations: DestinationConfigurations | None = None
    name: str | None = None
    refresh_cadence: RefreshCadence | None = None
    description: str | None = None
    export_arn: str | None = None


@dataclass
class RefreshCadence(PropertyType):
    frequency: str | None = None


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class S3Destination(PropertyType):
    s3_bucket: str | None = None
    s3_output_configurations: S3OutputConfigurations | None = None
    s3_prefix: str | None = None
    s3_region: str | None = None


@dataclass
class S3OutputConfigurations(PropertyType):
    compression: str | None = None
    format: str | None = None
    output_type: str | None = None
    overwrite: str | None = None
