"""PropertyTypes for AWS::Timestream::InfluxDBInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LogDeliveryConfiguration(PropertyType):
    s3_configuration: DslValue[S3Configuration] | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
