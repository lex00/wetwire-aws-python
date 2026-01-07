"""PropertyTypes for AWS::AppStream::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeCapacity(PropertyType):
    desired_instances: DslValue[int] | None = None
    desired_sessions: DslValue[int] | None = None


@dataclass
class DomainJoinInfo(PropertyType):
    directory_name: DslValue[str] | None = None
    organizational_unit_distinguished_name: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
