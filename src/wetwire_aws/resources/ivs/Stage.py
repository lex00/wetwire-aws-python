"""PropertyTypes for AWS::IVS::Stage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoParticipantRecordingConfiguration(PropertyType):
    storage_configuration_arn: DslValue[str] | None = None
    hls_configuration: DslValue[HlsConfiguration] | None = None
    media_types: list[DslValue[str]] = field(default_factory=list)
    recording_reconnect_window_seconds: DslValue[int] | None = None
    thumbnail_configuration: DslValue[ThumbnailConfiguration] | None = None


@dataclass
class HlsConfiguration(PropertyType):
    participant_recording_hls_configuration: (
        DslValue[ParticipantRecordingHlsConfiguration] | None
    ) = None


@dataclass
class ParticipantRecordingHlsConfiguration(PropertyType):
    target_segment_duration_seconds: DslValue[int] | None = None


@dataclass
class ParticipantThumbnailConfiguration(PropertyType):
    recording_mode: DslValue[str] | None = None
    storage: list[DslValue[str]] = field(default_factory=list)
    target_interval_seconds: DslValue[int] | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    participant_thumbnail_configuration: (
        DslValue[ParticipantThumbnailConfiguration] | None
    ) = None
