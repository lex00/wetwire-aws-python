"""PropertyTypes for AWS::IVS::Stage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoParticipantRecordingConfiguration(PropertyType):
    storage_configuration_arn: str | None = None
    hls_configuration: HlsConfiguration | None = None
    media_types: list[String] = field(default_factory=list)
    recording_reconnect_window_seconds: int | None = None
    thumbnail_configuration: ThumbnailConfiguration | None = None


@dataclass
class HlsConfiguration(PropertyType):
    participant_recording_hls_configuration: (
        ParticipantRecordingHlsConfiguration | None
    ) = None


@dataclass
class ParticipantRecordingHlsConfiguration(PropertyType):
    target_segment_duration_seconds: int | None = None


@dataclass
class ParticipantThumbnailConfiguration(PropertyType):
    recording_mode: str | None = None
    storage: list[String] = field(default_factory=list)
    target_interval_seconds: int | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    participant_thumbnail_configuration: ParticipantThumbnailConfiguration | None = None
