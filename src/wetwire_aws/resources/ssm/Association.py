"""PropertyTypes for AWS::SSM::Association."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InstanceAssociationOutputLocation(PropertyType):
    s3_location: S3OutputLocation | None = None


@dataclass
class S3OutputLocation(PropertyType):
    output_s3_bucket_name: str | None = None
    output_s3_key_prefix: str | None = None
    output_s3_region: str | None = None


@dataclass
class Target(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)
