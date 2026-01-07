"""PropertyTypes for AWS::MediaPackageV2::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DashBaseUrl(PropertyType):
    url: DslValue[str] | None = None
    dvb_priority: DslValue[int] | None = None
    dvb_weight: DslValue[int] | None = None
    service_location: DslValue[str] | None = None


@dataclass
class DashDvbFontDownload(PropertyType):
    font_family: DslValue[str] | None = None
    mime_type: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class DashDvbMetricsReporting(PropertyType):
    reporting_url: DslValue[str] | None = None
    probability: DslValue[int] | None = None


@dataclass
class DashDvbSettings(PropertyType):
    error_metrics: list[DslValue[DashDvbMetricsReporting]] = field(default_factory=list)
    font_download: DslValue[DashDvbFontDownload] | None = None


@dataclass
class DashManifestConfiguration(PropertyType):
    manifest_name: DslValue[str] | None = None
    base_urls: list[DslValue[DashBaseUrl]] = field(default_factory=list)
    compactness: DslValue[str] | None = None
    drm_signaling: DslValue[str] | None = None
    dvb_settings: DslValue[DashDvbSettings] | None = None
    filter_configuration: DslValue[FilterConfiguration] | None = None
    manifest_window_seconds: DslValue[int] | None = None
    min_buffer_time_seconds: DslValue[int] | None = None
    min_update_period_seconds: DslValue[int] | None = None
    period_triggers: list[DslValue[str]] = field(default_factory=list)
    profiles: list[DslValue[str]] = field(default_factory=list)
    program_information: DslValue[DashProgramInformation] | None = None
    scte_dash: DslValue[ScteDash] | None = None
    segment_template_format: DslValue[str] | None = None
    subtitle_configuration: DslValue[DashSubtitleConfiguration] | None = None
    suggested_presentation_delay_seconds: DslValue[int] | None = None
    utc_timing: DslValue[DashUtcTiming] | None = None


@dataclass
class DashProgramInformation(PropertyType):
    copyright: DslValue[str] | None = None
    language_code: DslValue[str] | None = None
    more_information_url: DslValue[str] | None = None
    source: DslValue[str] | None = None
    title: DslValue[str] | None = None


@dataclass
class DashSubtitleConfiguration(PropertyType):
    ttml_configuration: DslValue[DashTtmlConfiguration] | None = None


@dataclass
class DashTtmlConfiguration(PropertyType):
    ttml_profile: DslValue[str] | None = None


@dataclass
class DashUtcTiming(PropertyType):
    timing_mode: DslValue[str] | None = None
    timing_source: DslValue[str] | None = None


@dataclass
class Encryption(PropertyType):
    encryption_method: DslValue[EncryptionMethod] | None = None
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None
    cmaf_exclude_segment_drm_metadata: DslValue[bool] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    key_rotation_interval_seconds: DslValue[int] | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    preset_speke20_audio: DslValue[str] | None = None
    preset_speke20_video: DslValue[str] | None = None


@dataclass
class EncryptionMethod(PropertyType):
    cmaf_encryption_method: DslValue[str] | None = None
    ism_encryption_method: DslValue[str] | None = None
    ts_encryption_method: DslValue[str] | None = None


@dataclass
class FilterConfiguration(PropertyType):
    clip_start_time: DslValue[str] | None = None
    end: DslValue[str] | None = None
    manifest_filter: DslValue[str] | None = None
    start: DslValue[str] | None = None
    time_delay_seconds: DslValue[int] | None = None


@dataclass
class ForceEndpointErrorConfiguration(PropertyType):
    endpoint_error_conditions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HlsManifestConfiguration(PropertyType):
    manifest_name: DslValue[str] | None = None
    child_manifest_name: DslValue[str] | None = None
    filter_configuration: DslValue[FilterConfiguration] | None = None
    manifest_window_seconds: DslValue[int] | None = None
    program_date_time_interval_seconds: DslValue[int] | None = None
    scte_hls: DslValue[ScteHls] | None = None
    start_tag: DslValue[StartTag] | None = None
    url: DslValue[str] | None = None
    url_encode_child_manifest: DslValue[bool] | None = None


@dataclass
class LowLatencyHlsManifestConfiguration(PropertyType):
    manifest_name: DslValue[str] | None = None
    child_manifest_name: DslValue[str] | None = None
    filter_configuration: DslValue[FilterConfiguration] | None = None
    manifest_window_seconds: DslValue[int] | None = None
    program_date_time_interval_seconds: DslValue[int] | None = None
    scte_hls: DslValue[ScteHls] | None = None
    start_tag: DslValue[StartTag] | None = None
    url: DslValue[str] | None = None
    url_encode_child_manifest: DslValue[bool] | None = None


@dataclass
class MssManifestConfiguration(PropertyType):
    manifest_name: DslValue[str] | None = None
    filter_configuration: DslValue[FilterConfiguration] | None = None
    manifest_layout: DslValue[str] | None = None
    manifest_window_seconds: DslValue[int] | None = None


@dataclass
class Scte(PropertyType):
    scte_filter: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ScteDash(PropertyType):
    ad_marker_dash: DslValue[str] | None = None


@dataclass
class ScteHls(PropertyType):
    ad_marker_hls: DslValue[str] | None = None


@dataclass
class Segment(PropertyType):
    encryption: DslValue[Encryption] | None = None
    include_iframe_only_streams: DslValue[bool] | None = None
    scte: DslValue[Scte] | None = None
    segment_duration_seconds: DslValue[int] | None = None
    segment_name: DslValue[str] | None = None
    ts_include_dvb_subtitles: DslValue[bool] | None = None
    ts_use_audio_rendition_group: DslValue[bool] | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    drm_systems: list[DslValue[str]] = field(default_factory=list)
    encryption_contract_configuration: (
        DslValue[EncryptionContractConfiguration] | None
    ) = None
    resource_id: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class StartTag(PropertyType):
    time_offset: DslValue[float] | None = None
    precise: DslValue[bool] | None = None
