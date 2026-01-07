"""PropertyTypes for AWS::MediaPackage::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Authorization(PropertyType):
    cdn_identifier_secret: DslValue[str] | None = None
    secrets_role_arn: DslValue[str] | None = None


@dataclass
class CmafEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    encryption_method: DslValue[str] | None = None
    key_rotation_interval_seconds: DslValue[int] | None = None


@dataclass
class CmafPackage(PropertyType):
    encryption: DslValue[CmafEncryption] | None = None
    hls_manifests: list[DslValue[HlsManifest]] = field(default_factory=list)
    segment_duration_seconds: DslValue[int] | None = None
    segment_prefix: DslValue[str] | None = None
    stream_selection: DslValue[StreamSelection] | None = None


@dataclass
class DashEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None
    key_rotation_interval_seconds: DslValue[int] | None = None


@dataclass
class DashPackage(PropertyType):
    ad_triggers: list[DslValue[str]] = field(default_factory=list)
    ads_on_delivery_restrictions: DslValue[str] | None = None
    encryption: DslValue[DashEncryption] | None = None
    include_iframe_only_stream: DslValue[bool] | None = None
    manifest_layout: DslValue[str] | None = None
    manifest_window_seconds: DslValue[int] | None = None
    min_buffer_time_seconds: DslValue[int] | None = None
    min_update_period_seconds: DslValue[int] | None = None
    period_triggers: list[DslValue[str]] = field(default_factory=list)
    profile: DslValue[str] | None = None
    segment_duration_seconds: DslValue[int] | None = None
    segment_template_format: DslValue[str] | None = None
    stream_selection: DslValue[StreamSelection] | None = None
    suggested_presentation_delay_seconds: DslValue[int] | None = None
    utc_timing: DslValue[str] | None = None
    utc_timing_uri: DslValue[str] | None = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    pass


@dataclass
class HlsEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    encryption_method: DslValue[str] | None = None
    key_rotation_interval_seconds: DslValue[int] | None = None
    repeat_ext_x_key: DslValue[bool] | None = None


@dataclass
class HlsManifest(PropertyType):
    id: DslValue[str] | None = None
    ad_markers: DslValue[str] | None = None
    ad_triggers: list[DslValue[str]] = field(default_factory=list)
    ads_on_delivery_restrictions: DslValue[str] | None = None
    include_iframe_only_stream: DslValue[bool] | None = None
    manifest_name: DslValue[str] | None = None
    playlist_type: DslValue[str] | None = None
    playlist_window_seconds: DslValue[int] | None = None
    program_date_time_interval_seconds: DslValue[int] | None = None
    url: DslValue[str] | None = None


@dataclass
class HlsPackage(PropertyType):
    ad_markers: DslValue[str] | None = None
    ad_triggers: list[DslValue[str]] = field(default_factory=list)
    ads_on_delivery_restrictions: DslValue[str] | None = None
    encryption: DslValue[HlsEncryption] | None = None
    include_dvb_subtitles: DslValue[bool] | None = None
    include_iframe_only_stream: DslValue[bool] | None = None
    playlist_type: DslValue[str] | None = None
    playlist_window_seconds: DslValue[int] | None = None
    program_date_time_interval_seconds: DslValue[int] | None = None
    segment_duration_seconds: DslValue[int] | None = None
    stream_selection: DslValue[StreamSelection] | None = None
    use_audio_rendition_group: DslValue[bool] | None = None


@dataclass
class MssEncryption(PropertyType):
    speke_key_provider: DslValue[SpekeKeyProvider] | None = None


@dataclass
class MssPackage(PropertyType):
    encryption: DslValue[MssEncryption] | None = None
    manifest_window_seconds: DslValue[int] | None = None
    segment_duration_seconds: DslValue[int] | None = None
    stream_selection: DslValue[StreamSelection] | None = None


@dataclass
class SpekeKeyProvider(PropertyType):
    resource_id: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    system_ids: list[DslValue[str]] = field(default_factory=list)
    url: DslValue[str] | None = None
    certificate_arn: DslValue[str] | None = None
    encryption_contract_configuration: (
        DslValue[EncryptionContractConfiguration] | None
    ) = None


@dataclass
class StreamSelection(PropertyType):
    max_video_bits_per_second: DslValue[int] | None = None
    min_video_bits_per_second: DslValue[int] | None = None
    stream_order: DslValue[str] | None = None
