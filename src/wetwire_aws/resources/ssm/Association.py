"""PropertyTypes for AWS::SSM::Association."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InstanceAssociationOutputLocation(PropertyType):
    s3_location: DslValue[S3OutputLocation] | None = None


@dataclass
class S3OutputLocation(PropertyType):
    output_s3_bucket_name: DslValue[str] | None = None
    output_s3_key_prefix: DslValue[str] | None = None
    output_s3_region: DslValue[str] | None = None


@dataclass
class Target(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
