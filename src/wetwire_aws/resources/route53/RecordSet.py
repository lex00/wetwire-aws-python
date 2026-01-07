"""PropertyTypes for AWS::Route53::RecordSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AliasTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
    }

    dns_name: DslValue[str] | None = None
    hosted_zone_id: DslValue[str] | None = None
    evaluate_target_health: DslValue[bool] | None = None


@dataclass
class CidrRoutingConfig(PropertyType):
    collection_id: DslValue[str] | None = None
    location_name: DslValue[str] | None = None


@dataclass
class Coordinates(PropertyType):
    latitude: DslValue[str] | None = None
    longitude: DslValue[str] | None = None


@dataclass
class GeoLocation(PropertyType):
    continent_code: DslValue[str] | None = None
    country_code: DslValue[str] | None = None
    subdivision_code: DslValue[str] | None = None


@dataclass
class GeoProximityLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AWSRegion",
    }

    aws_region: DslValue[str] | None = None
    bias: DslValue[int] | None = None
    coordinates: DslValue[Coordinates] | None = None
    local_zone_group: DslValue[str] | None = None
