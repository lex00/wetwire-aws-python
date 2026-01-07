"""PropertyTypes for AWS::Pinpoint::Segment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeDimension(PropertyType):
    attribute_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Behavior(PropertyType):
    recency: DslValue[Recency] | None = None


@dataclass
class Coordinates(PropertyType):
    latitude: DslValue[float] | None = None
    longitude: DslValue[float] | None = None


@dataclass
class Demographic(PropertyType):
    app_version: DslValue[SetDimension] | None = None
    channel: DslValue[SetDimension] | None = None
    device_type: DslValue[SetDimension] | None = None
    make: DslValue[SetDimension] | None = None
    model: DslValue[SetDimension] | None = None
    platform: DslValue[SetDimension] | None = None


@dataclass
class GPSPoint(PropertyType):
    coordinates: DslValue[Coordinates] | None = None
    range_in_kilometers: DslValue[float] | None = None


@dataclass
class Groups(PropertyType):
    dimensions: list[DslValue[SegmentDimensions]] = field(default_factory=list)
    source_segments: list[DslValue[SourceSegments]] = field(default_factory=list)
    source_type: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gps_point": "GPSPoint",
    }

    country: DslValue[SetDimension] | None = None
    gps_point: DslValue[GPSPoint] | None = None


@dataclass
class Recency(PropertyType):
    duration: DslValue[str] | None = None
    recency_type: DslValue[str] | None = None


@dataclass
class SegmentDimensions(PropertyType):
    attributes: DslValue[dict[str, Any]] | None = None
    behavior: DslValue[Behavior] | None = None
    demographic: DslValue[Demographic] | None = None
    location: DslValue[Location] | None = None
    metrics: DslValue[dict[str, Any]] | None = None
    user_attributes: DslValue[dict[str, Any]] | None = None


@dataclass
class SegmentGroups(PropertyType):
    groups: list[DslValue[Groups]] = field(default_factory=list)
    include: DslValue[str] | None = None


@dataclass
class SetDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SourceSegments(PropertyType):
    id: DslValue[str] | None = None
    version: DslValue[int] | None = None
