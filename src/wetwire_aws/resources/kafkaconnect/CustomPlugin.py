"""PropertyTypes for AWS::KafkaConnect::CustomPlugin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomPluginFileDescription(PropertyType):
    file_md5: str | None = None
    file_size: int | None = None


@dataclass
class CustomPluginLocation(PropertyType):
    s3_location: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    bucket_arn: str | None = None
    file_key: str | None = None
    object_version: str | None = None
