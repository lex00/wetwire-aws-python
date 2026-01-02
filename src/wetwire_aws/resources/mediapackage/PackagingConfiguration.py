"""PropertyTypes for AWS::MediaPackage::PackagingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CmafEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None


@dataclass
class CmafPackage(PropertyType):
    hls_manifests: list[HlsManifest] = field(default_factory=list)
    encryption: CmafEncryption | None = None
    include_encoder_configuration_in_segments: bool | None = None
    segment_duration_seconds: int | None = None


@dataclass
class DashEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None


@dataclass
class DashManifest(PropertyType):
    manifest_layout: str | None = None
    manifest_name: str | None = None
    min_buffer_time_seconds: int | None = None
    profile: str | None = None
    scte_markers_source: str | None = None
    stream_selection: StreamSelection | None = None


@dataclass
class DashPackage(PropertyType):
    dash_manifests: list[DashManifest] = field(default_factory=list)
    encryption: DashEncryption | None = None
    include_encoder_configuration_in_segments: bool | None = None
    include_iframe_only_stream: bool | None = None
    period_triggers: list[String] = field(default_factory=list)
    segment_duration_seconds: int | None = None
    segment_template_format: str | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    preset_speke20_audio: str | None = None
    preset_speke20_video: str | None = None


@dataclass
class HlsEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None
    constant_initialization_vector: str | None = None
    encryption_method: str | None = None


@dataclass
class HlsManifest(PropertyType):
    ad_markers: str | None = None
    include_iframe_only_stream: bool | None = None
    manifest_name: str | None = None
    program_date_time_interval_seconds: int | None = None
    repeat_ext_x_key: bool | None = None
    stream_selection: StreamSelection | None = None


@dataclass
class HlsPackage(PropertyType):
    hls_manifests: list[HlsManifest] = field(default_factory=list)
    encryption: HlsEncryption | None = None
    include_dvb_subtitles: bool | None = None
    segment_duration_seconds: int | None = None
    use_audio_rendition_group: bool | None = None


@dataclass
class MssEncryption(PropertyType):
    speke_key_provider: SpekeKeyProvider | None = None


@dataclass
class MssManifest(PropertyType):
    manifest_name: str | None = None
    stream_selection: StreamSelection | None = None


@dataclass
class MssPackage(PropertyType):
    mss_manifests: list[MssManifest] = field(default_factory=list)
    encryption: MssEncryption | None = None
    segment_duration_seconds: int | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    role_arn: str | None = None
    system_ids: list[String] = field(default_factory=list)
    url: str | None = None
    encryption_contract_configuration: EncryptionContractConfiguration | None = None


@dataclass
class StreamSelection(PropertyType):
    max_video_bits_per_second: int | None = None
    min_video_bits_per_second: int | None = None
    stream_order: str | None = None
