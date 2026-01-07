"""PropertyTypes for AWS::ImageBuilder::InfrastructureConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InstanceMetadataOptions(PropertyType):
    http_put_response_hop_limit: DslValue[int] | None = None
    http_tokens: DslValue[str] | None = None


@dataclass
class Logging(PropertyType):
    s3_logs: DslValue[S3Logs] | None = None


@dataclass
class Placement(PropertyType):
    availability_zone: DslValue[str] | None = None
    host_id: DslValue[str] | None = None
    host_resource_group_arn: DslValue[str] | None = None
    tenancy: DslValue[str] | None = None


@dataclass
class S3Logs(PropertyType):
    s3_bucket_name: DslValue[str] | None = None
    s3_key_prefix: DslValue[str] | None = None
