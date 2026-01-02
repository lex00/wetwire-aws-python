"""PropertyTypes for AWS::AppStream::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeCapacity(PropertyType):
    desired_instances: int | None = None
    desired_sessions: int | None = None


@dataclass
class DomainJoinInfo(PropertyType):
    directory_name: str | None = None
    organizational_unit_distinguished_name: str | None = None


@dataclass
class S3Location(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
