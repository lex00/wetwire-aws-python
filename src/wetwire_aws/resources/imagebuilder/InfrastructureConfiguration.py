"""PropertyTypes for AWS::ImageBuilder::InfrastructureConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InstanceMetadataOptions(PropertyType):
    http_put_response_hop_limit: int | None = None
    http_tokens: str | None = None


@dataclass
class Logging(PropertyType):
    s3_logs: S3Logs | None = None


@dataclass
class Placement(PropertyType):
    availability_zone: str | None = None
    host_id: str | None = None
    host_resource_group_arn: str | None = None
    tenancy: str | None = None


@dataclass
class S3Logs(PropertyType):
    s3_bucket_name: str | None = None
    s3_key_prefix: str | None = None
