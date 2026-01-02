"""PropertyTypes for AWS::IVS::RecordingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationConfiguration(PropertyType):
    s3: S3DestinationConfiguration | None = None


@dataclass
class RenditionConfiguration(PropertyType):
    rendition_selection: str | None = None
    renditions: list[String] = field(default_factory=list)


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket_name: str | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    recording_mode: str | None = None
    resolution: str | None = None
    storage: list[String] = field(default_factory=list)
    target_interval_seconds: int | None = None
