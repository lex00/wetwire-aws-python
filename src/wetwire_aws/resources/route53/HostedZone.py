"""PropertyTypes for AWS::Route53::HostedZone."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HostedZoneConfig(PropertyType):
    comment: DslValue[str] | None = None


@dataclass
class HostedZoneFeatures(PropertyType):
    enable_accelerated_recovery: DslValue[bool] | None = None


@dataclass
class HostedZoneTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class QueryLoggingConfig(PropertyType):
    cloud_watch_logs_log_group_arn: DslValue[str] | None = None


@dataclass
class VPC(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VPCId",
        "vpc_region": "VPCRegion",
    }

    vpc_id: DslValue[str] | None = None
    vpc_region: DslValue[str] | None = None
