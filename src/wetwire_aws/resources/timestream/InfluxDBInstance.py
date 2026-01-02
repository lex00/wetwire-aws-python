"""PropertyTypes for AWS::Timestream::InfluxDBInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LogDeliveryConfiguration(PropertyType):
    s3_configuration: S3Configuration | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: str | None = None
    enabled: bool | None = None
