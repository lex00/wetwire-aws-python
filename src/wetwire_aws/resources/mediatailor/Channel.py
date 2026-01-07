"""PropertyTypes for AWS::MediaTailor::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DashPlaylistSettings(PropertyType):
    manifest_window_seconds: DslValue[float] | None = None
    min_buffer_time_seconds: DslValue[float] | None = None
    min_update_period_seconds: DslValue[float] | None = None
    suggested_presentation_delay_seconds: DslValue[float] | None = None


@dataclass
class HlsPlaylistSettings(PropertyType):
    ad_markup_type: list[DslValue[str]] = field(default_factory=list)
    manifest_window_seconds: DslValue[float] | None = None


@dataclass
class LogConfigurationForChannel(PropertyType):
    log_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RequestOutputItem(PropertyType):
    manifest_name: DslValue[str] | None = None
    source_group: DslValue[str] | None = None
    dash_playlist_settings: DslValue[DashPlaylistSettings] | None = None
    hls_playlist_settings: DslValue[HlsPlaylistSettings] | None = None


@dataclass
class SlateSource(PropertyType):
    source_location_name: DslValue[str] | None = None
    vod_source_name: DslValue[str] | None = None


@dataclass
class TimeShiftConfiguration(PropertyType):
    max_time_delay_seconds: DslValue[float] | None = None
