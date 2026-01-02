"""PropertyTypes for AWS::Pinpoint::Segment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeDimension(PropertyType):
    attribute_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Behavior(PropertyType):
    recency: Recency | None = None


@dataclass
class Coordinates(PropertyType):
    latitude: float | None = None
    longitude: float | None = None


@dataclass
class Demographic(PropertyType):
    app_version: SetDimension | None = None
    channel: SetDimension | None = None
    device_type: SetDimension | None = None
    make: SetDimension | None = None
    model: SetDimension | None = None
    platform: SetDimension | None = None


@dataclass
class GPSPoint(PropertyType):
    coordinates: Coordinates | None = None
    range_in_kilometers: float | None = None


@dataclass
class Groups(PropertyType):
    dimensions: list[SegmentDimensions] = field(default_factory=list)
    source_segments: list[SourceSegments] = field(default_factory=list)
    source_type: str | None = None
    type_: str | None = None


@dataclass
class Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gps_point": "GPSPoint",
    }

    country: SetDimension | None = None
    gps_point: GPSPoint | None = None


@dataclass
class Recency(PropertyType):
    duration: str | None = None
    recency_type: str | None = None


@dataclass
class SegmentDimensions(PropertyType):
    attributes: dict[str, Any] | None = None
    behavior: Behavior | None = None
    demographic: Demographic | None = None
    location: Location | None = None
    metrics: dict[str, Any] | None = None
    user_attributes: dict[str, Any] | None = None


@dataclass
class SegmentGroups(PropertyType):
    groups: list[Groups] = field(default_factory=list)
    include: str | None = None


@dataclass
class SetDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class SourceSegments(PropertyType):
    id: str | None = None
    version: int | None = None
