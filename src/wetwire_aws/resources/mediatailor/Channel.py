"""PropertyTypes for AWS::MediaTailor::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DashPlaylistSettings(PropertyType):
    manifest_window_seconds: float | None = None
    min_buffer_time_seconds: float | None = None
    min_update_period_seconds: float | None = None
    suggested_presentation_delay_seconds: float | None = None


@dataclass
class HlsPlaylistSettings(PropertyType):
    ad_markup_type: list[String] = field(default_factory=list)
    manifest_window_seconds: float | None = None


@dataclass
class LogConfigurationForChannel(PropertyType):
    log_types: list[String] = field(default_factory=list)


@dataclass
class RequestOutputItem(PropertyType):
    manifest_name: str | None = None
    source_group: str | None = None
    dash_playlist_settings: DashPlaylistSettings | None = None
    hls_playlist_settings: HlsPlaylistSettings | None = None


@dataclass
class SlateSource(PropertyType):
    source_location_name: str | None = None
    vod_source_name: str | None = None


@dataclass
class TimeShiftConfiguration(PropertyType):
    max_time_delay_seconds: float | None = None
