"""PropertyTypes for AWS::KafkaConnect::CustomPlugin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomPluginFileDescription(PropertyType):
    file_md5: DslValue[str] | None = None
    file_size: DslValue[int] | None = None


@dataclass
class CustomPluginLocation(PropertyType):
    s3_location: DslValue[S3Location] | None = None


@dataclass
class S3Location(PropertyType):
    bucket_arn: DslValue[str] | None = None
    file_key: DslValue[str] | None = None
    object_version: DslValue[str] | None = None
