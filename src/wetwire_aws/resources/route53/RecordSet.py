"""PropertyTypes for AWS::Route53::RecordSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AliasTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
    }

    dns_name: str | None = None
    hosted_zone_id: str | None = None
    evaluate_target_health: bool | None = None


@dataclass
class CidrRoutingConfig(PropertyType):
    collection_id: str | None = None
    location_name: str | None = None


@dataclass
class Coordinates(PropertyType):
    latitude: str | None = None
    longitude: str | None = None


@dataclass
class GeoLocation(PropertyType):
    continent_code: str | None = None
    country_code: str | None = None
    subdivision_code: str | None = None


@dataclass
class GeoProximityLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AWSRegion",
    }

    aws_region: str | None = None
    bias: int | None = None
    coordinates: Coordinates | None = None
    local_zone_group: str | None = None
