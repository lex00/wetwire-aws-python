"""PropertyTypes for AWS::IVS::RecordingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationConfiguration(PropertyType):
    s3: DslValue[S3DestinationConfiguration] | None = None


@dataclass
class RenditionConfiguration(PropertyType):
    rendition_selection: DslValue[str] | None = None
    renditions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket_name: DslValue[str] | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    recording_mode: DslValue[str] | None = None
    resolution: DslValue[str] | None = None
    storage: list[DslValue[str]] = field(default_factory=list)
    target_interval_seconds: DslValue[int] | None = None
