"""PropertyTypes for AWS::Route53::HostedZone."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HostedZoneConfig(PropertyType):
    comment: str | None = None


@dataclass
class HostedZoneFeatures(PropertyType):
    enable_accelerated_recovery: bool | None = None


@dataclass
class HostedZoneTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class QueryLoggingConfig(PropertyType):
    cloud_watch_logs_log_group_arn: str | None = None


@dataclass
class VPC(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VPCId",
        "vpc_region": "VPCRegion",
    }

    vpc_id: str | None = None
    vpc_region: str | None = None
