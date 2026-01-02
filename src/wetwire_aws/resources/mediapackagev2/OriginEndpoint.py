"""PropertyTypes for AWS::MediaPackageV2::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DashBaseUrl(PropertyType):
    url: str | None = None
    dvb_priority: int | None = None
    dvb_weight: int | None = None
    service_location: str | None = None


@dataclass
class DashDvbFontDownload(PropertyType):
    font_family: str | None = None
    mime_type: str | None = None
    url: str | None = None


@dataclass
class DashDvbMetricsReporting(PropertyType):
    reporting_url: str | None = None
    probability: int | None = None


@dataclass
class DashDvbSettings(PropertyType):
    error_metrics: list[DashDvbMetricsReporting] = field(default_factory=list)
    font_download: DashDvbFontDownload | None = None


@dataclass
class DashManifestConfiguration(PropertyType):
    manifest_name: str | None = None
    base_urls: list[DashBaseUrl] = field(default_factory=list)
    compactness: str | None = None
    drm_signaling: str | None = None
    dvb_settings: DashDvbSettings | None = None
    filter_configuration: FilterConfiguration | None = None
    manifest_window_seconds: int | None = None
    min_buffer_time_seconds: int | None = None
    min_update_period_seconds: int | None = None
    period_triggers: list[String] = field(default_factory=list)
    profiles: list[String] = field(default_factory=list)
    program_information: DashProgramInformation | None = None
    scte_dash: ScteDash | None = None
    segment_template_format: str | None = None
    subtitle_configuration: DashSubtitleConfiguration | None = None
    suggested_presentation_delay_seconds: int | None = None
    utc_timing: DashUtcTiming | None = None


@dataclass
class DashProgramInformation(PropertyType):
    copyright: str | None = None
    language_code: str | None = None
    more_information_url: str | None = None
    source: str | None = None
    title: str | None = None


@dataclass
class DashSubtitleConfiguration(PropertyType):
    ttml_configuration: DashTtmlConfiguration | None = None


@dataclass
class DashTtmlConfiguration(PropertyType):
    ttml_profile: str | None = None


@dataclass
class DashUtcTiming(PropertyType):
    timing_mode: str | None = None
    timing_source: str | None = None


@dataclass
class Encryption(PropertyType):
    encryption_method: EncryptionMethod | None = None
    speke_key_provider: SpekeKeyProvider | None = None
    cmaf_exclude_segment_drm_metadata: bool | None = None
    constant_initialization_vector: str | None = None
    key_rotation_interval_seconds: int | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    preset_speke20_audio: str | None = None
    preset_speke20_video: str | None = None


@dataclass
class EncryptionMethod(PropertyType):
    cmaf_encryption_method: str | None = None
    ism_encryption_method: str | None = None
    ts_encryption_method: str | None = None


@dataclass
class FilterConfiguration(PropertyType):
    clip_start_time: str | None = None
    end: str | None = None
    manifest_filter: str | None = None
    start: str | None = None
    time_delay_seconds: int | None = None


@dataclass
class ForceEndpointErrorConfiguration(PropertyType):
    endpoint_error_conditions: list[String] = field(default_factory=list)


@dataclass
class HlsManifestConfiguration(PropertyType):
    manifest_name: str | None = None
    child_manifest_name: str | None = None
    filter_configuration: FilterConfiguration | None = None
    manifest_window_seconds: int | None = None
    program_date_time_interval_seconds: int | None = None
    scte_hls: ScteHls | None = None
    start_tag: StartTag | None = None
    url: str | None = None
    url_encode_child_manifest: bool | None = None


@dataclass
class LowLatencyHlsManifestConfiguration(PropertyType):
    manifest_name: str | None = None
    child_manifest_name: str | None = None
    filter_configuration: FilterConfiguration | None = None
    manifest_window_seconds: int | None = None
    program_date_time_interval_seconds: int | None = None
    scte_hls: ScteHls | None = None
    start_tag: StartTag | None = None
    url: str | None = None
    url_encode_child_manifest: bool | None = None


@dataclass
class MssManifestConfiguration(PropertyType):
    manifest_name: str | None = None
    filter_configuration: FilterConfiguration | None = None
    manifest_layout: str | None = None
    manifest_window_seconds: int | None = None


@dataclass
class Scte(PropertyType):
    scte_filter: list[String] = field(default_factory=list)


@dataclass
class ScteDash(PropertyType):
    ad_marker_dash: str | None = None


@dataclass
class ScteHls(PropertyType):
    ad_marker_hls: str | None = None


@dataclass
class Segment(PropertyType):
    encryption: Encryption | None = None
    include_iframe_only_streams: bool | None = None
    scte: Scte | None = None
    segment_duration_seconds: int | None = None
    segment_name: str | None = None
    ts_include_dvb_subtitles: bool | None = None
    ts_use_audio_rendition_group: bool | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    drm_systems: list[String] = field(default_factory=list)
    encryption_contract_configuration: EncryptionContractConfiguration | None = None
    resource_id: str | None = None
    role_arn: str | None = None
    url: str | None = None


@dataclass
class StartTag(PropertyType):
    time_offset: float | None = None
    precise: bool | None = None
