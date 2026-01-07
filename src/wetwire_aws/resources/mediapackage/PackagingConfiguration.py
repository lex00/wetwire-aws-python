"""PropertyTypes for AWS::MediaPackage::PackagingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CmafEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None


@dataclass
class CmafPackage(PropertyType):
    hls_manifests: list[DslValue[HlsManifest]] = field(default_factory=list)
    encryption: DslValue[CmafEncryption] | None = None
    include_encoder_configuration_in_segments: DslValue[bool] | None = None
    segment_duration_seconds: DslValue[int] | None = None


@dataclass
class DashEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None


@dataclass
class DashManifest(PropertyType):
    manifest_layout: DslValue[str] | None = None
    manifest_name: DslValue[str] | None = None
    min_buffer_time_seconds: DslValue[int] | None = None
    profile: DslValue[str] | None = None
    scte_markers_source: DslValue[str] | None = None
    stream_selection: DslValue[StreamSelection] | None = None


@dataclass
class DashPackage(PropertyType):
    dash_manifests: list[DslValue[DashManifest]] = field(default_factory=list)
    encryption: DslValue[DashEncryption] | None = None
    include_encoder_configuration_in_segments: DslValue[bool] | None = None
    include_iframe_only_stream: DslValue[bool] | None = None
    period_triggers: list[DslValue[str]] = field(default_factory=list)
    segment_duration_seconds: DslValue[int] | None = None
    segment_template_format: DslValue[str] | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    preset_speke20_audio: DslValue[str] | None = None
    preset_speke20_video: DslValue[str] | None = None


@dataclass
class HlsEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    encryption_method: DslValue[str] | None = None


@dataclass
class HlsManifest(PropertyType):
    ad_markers: DslValue[str] | None = None
    include_iframe_only_stream: DslValue[bool] | None = None
    manifest_name: DslValue[str] | None = None
    program_date_time_interval_seconds: DslValue[int] | None = None
    repeat_ext_x_key: DslValue[bool] | None = None
    stream_selection: DslValue[StreamSelection] | None = None


@dataclass
class HlsPackage(PropertyType):
    hls_manifests: list[DslValue[HlsManifest]] = field(default_factory=list)
    encryption: DslValue[HlsEncryption] | None = None
    include_dvb_subtitles: DslValue[bool] | None = None
    segment_duration_seconds: DslValue[int] | None = None
    use_audio_rendition_group: DslValue[bool] | None = None


@dataclass
class MssEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None


@dataclass
class MssManifest(PropertyType):
    manifest_name: DslValue[str] | None = None
    stream_selection: DslValue[StreamSelection] | None = None


@dataclass
class MssPackage(PropertyType):
    mss_manifests: list[DslValue[MssManifest]] = field(default_factory=list)
    encryption: DslValue[MssEncryption] | None = None
    segment_duration_seconds: DslValue[int] | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    role_arn: DslValue[str] | None = None
    system_ids: list[DslValue[str]] = field(default_factory=list)
    url: DslValue[str] | None = None
    encryption_contract_configuration: (
        DslValue[EncryptionContractConfiguration] | None
    ) = None


@dataclass
class StreamSelection(PropertyType):
    max_video_bits_per_second: DslValue[int] | None = None
    min_video_bits_per_second: DslValue[int] | None = None
    stream_order: DslValue[str] | None = None
