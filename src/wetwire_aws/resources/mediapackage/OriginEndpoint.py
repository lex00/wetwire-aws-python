"""PropertyTypes for AWS::MediaPackage::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Authorization(PropertyType):
    cdn_identifier_secret: str | None = None
    secrets_role_arn: str | None = None


@dataclass
class CmafEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None
    constant_initialization_vector: str | None = None
    encryption_method: str | None = None
    key_rotation_interval_seconds: int | None = None


@dataclass
class CmafPackage(PropertyType):
    encryption: CmafEncryption | None = None
    hls_manifests: list[HlsManifest] = field(default_factory=list)
    segment_duration_seconds: int | None = None
    segment_prefix: str | None = None
    stream_selection: StreamSelection | None = None


@dataclass
class DashEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None
    key_rotation_interval_seconds: int | None = None


@dataclass
class DashPackage(PropertyType):
    ad_triggers: list[String] = field(default_factory=list)
    ads_on_delivery_restrictions: str | None = None
    encryption: DashEncryption | None = None
    include_iframe_only_stream: bool | None = None
    manifest_layout: str | None = None
    manifest_window_seconds: int | None = None
    min_buffer_time_seconds: int | None = None
    min_update_period_seconds: int | None = None
    period_triggers: list[String] = field(default_factory=list)
    profile: str | None = None
    segment_duration_seconds: int | None = None
    segment_template_format: str | None = None
    stream_selection: StreamSelection | None = None
    suggested_presentation_delay_seconds: int | None = None
    utc_timing: str | None = None
    utc_timing_uri: str | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    pass


@dataclass
class HlsEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None
    constant_initialization_vector: str | None = None
    encryption_method: str | None = None
    key_rotation_interval_seconds: int | None = None
    repeat_ext_x_key: bool | None = None


@dataclass
class HlsManifest(PropertyType):
    id: str | None = None
    ad_markers: str | None = None
    ad_triggers: list[String] = field(default_factory=list)
    ads_on_delivery_restrictions: str | None = None
    include_iframe_only_stream: bool | None = None
    manifest_name: str | None = None
    playlist_type: str | None = None
    playlist_window_seconds: int | None = None
    program_date_time_interval_seconds: int | None = None
    url: str | None = None


@dataclass
class HlsPackage(PropertyType):
    ad_markers: str | None = None
    ad_triggers: list[String] = field(default_factory=list)
    ads_on_delivery_restrictions: str | None = None
    encryption: HlsEncryption | None = None
    include_dvb_subtitles: bool | None = None
    include_iframe_only_stream: bool | None = None
    playlist_type: str | None = None
    playlist_window_seconds: int | None = None
    program_date_time_interval_seconds: int | None = None
    segment_duration_seconds: int | None = None
    stream_selection: StreamSelection | None = None
    use_audio_rendition_group: bool | None = None


@dataclass
class MssEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None


@dataclass
class MssPackage(PropertyType):
    encryption: MssEncryption | None = None
    manifest_window_seconds: int | None = None
    segment_duration_seconds: int | None = None
    stream_selection: StreamSelection | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    resource_id: str | None = None
    role_arn: str | None = None
    system_ids: list[String] = field(default_factory=list)
    url: str | None = None
    certificate_arn: str | None = None
    encryption_contract_configuration: EncryptionContractConfiguration | None = None


@dataclass
class StreamSelection(PropertyType):
    max_video_bits_per_second: int | None = None
    min_video_bits_per_second: int | None = None
    stream_order: str | None = None
