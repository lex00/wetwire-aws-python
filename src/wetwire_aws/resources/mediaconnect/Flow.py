"""PropertyTypes for AWS::MediaConnect::Flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AudioMonitoringSetting(PropertyType):
    silent_audio: DslValue[SilentAudio] | None = None


@dataclass
class BlackFrames(PropertyType):
    state: DslValue[str] | None = None
    threshold_seconds: DslValue[int] | None = None


@dataclass
class Encryption(PropertyType):
    role_arn: DslValue[str] | None = None
    algorithm: DslValue[str] | None = None
    constant_initialization_vector: DslValue[str] | None = None
    device_id: DslValue[str] | None = None
    key_type: DslValue[str] | None = None
    region: DslValue[str] | None = None
    resource_id: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class FailoverConfig(PropertyType):
    failover_mode: DslValue[str] | None = None
    recovery_window: DslValue[int] | None = None
    source_priority: DslValue[SourcePriority] | None = None
    state: DslValue[str] | None = None


@dataclass
class FlowTransitEncryption(PropertyType):
    encryption_key_configuration: (
        DslValue[FlowTransitEncryptionKeyConfiguration] | None
    ) = None
    encryption_key_type: DslValue[str] | None = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    automatic: DslValue[dict[str, Any]] | None = None
    secrets_manager: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class Fmtp(PropertyType):
    channel_order: DslValue[str] | None = None
    colorimetry: DslValue[str] | None = None
    exact_framerate: DslValue[str] | None = None
    par: DslValue[str] | None = None
    range: DslValue[str] | None = None
    scan_mode: DslValue[str] | None = None
    tcs: DslValue[str] | None = None


@dataclass
class FrozenFrames(PropertyType):
    state: DslValue[str] | None = None
    threshold_seconds: DslValue[int] | None = None


@dataclass
class GatewayBridgeSource(PropertyType):
    bridge_arn: DslValue[str] | None = None
    vpc_interface_attachment: DslValue[VpcInterfaceAttachment] | None = None


@dataclass
class InputConfiguration(PropertyType):
    input_port: DslValue[int] | None = None
    interface: DslValue[Interface] | None = None


@dataclass
class Interface(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class Maintenance(PropertyType):
    maintenance_day: DslValue[str] | None = None
    maintenance_start_hour: DslValue[str] | None = None


@dataclass
class MediaStream(PropertyType):
    media_stream_id: DslValue[int] | None = None
    media_stream_name: DslValue[str] | None = None
    media_stream_type: DslValue[str] | None = None
    attributes: DslValue[MediaStreamAttributes] | None = None
    clock_rate: DslValue[int] | None = None
    description: DslValue[str] | None = None
    fmt: DslValue[int] | None = None
    video_format: DslValue[str] | None = None


@dataclass
class MediaStreamAttributes(PropertyType):
    fmtp: DslValue[Fmtp] | None = None
    lang: DslValue[str] | None = None


@dataclass
class MediaStreamSourceConfiguration(PropertyType):
    encoding_name: DslValue[str] | None = None
    media_stream_name: DslValue[str] | None = None
    input_configurations: list[DslValue[InputConfiguration]] = field(
        default_factory=list
    )


@dataclass
class NdiConfig(PropertyType):
    machine_name: DslValue[str] | None = None
    ndi_discovery_servers: list[DslValue[NdiDiscoveryServerConfig]] = field(
        default_factory=list
    )
    ndi_state: DslValue[str] | None = None


@dataclass
class NdiDiscoveryServerConfig(PropertyType):
    discovery_server_address: DslValue[str] | None = None
    vpc_interface_adapter: DslValue[str] | None = None
    discovery_server_port: DslValue[int] | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class SilentAudio(PropertyType):
    state: DslValue[str] | None = None
    threshold_seconds: DslValue[int] | None = None


@dataclass
class Source(PropertyType):
    decryption: DslValue[Encryption] | None = None
    description: DslValue[str] | None = None
    entitlement_arn: DslValue[str] | None = None
    gateway_bridge_source: DslValue[GatewayBridgeSource] | None = None
    ingest_ip: DslValue[str] | None = None
    ingest_port: DslValue[int] | None = None
    max_bitrate: DslValue[int] | None = None
    max_latency: DslValue[int] | None = None
    max_sync_buffer: DslValue[int] | None = None
    media_stream_source_configurations: list[
        DslValue[MediaStreamSourceConfiguration]
    ] = field(default_factory=list)
    min_latency: DslValue[int] | None = None
    name: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    router_integration_state: DslValue[str] | None = None
    router_integration_transit_decryption: DslValue[FlowTransitEncryption] | None = None
    sender_control_port: DslValue[int] | None = None
    sender_ip_address: DslValue[str] | None = None
    source_arn: DslValue[str] | None = None
    source_ingest_port: DslValue[str] | None = None
    source_listener_address: DslValue[str] | None = None
    source_listener_port: DslValue[int] | None = None
    stream_id: DslValue[str] | None = None
    vpc_interface_name: DslValue[str] | None = None
    whitelist_cidr: DslValue[str] | None = None


@dataclass
class SourceMonitoringConfig(PropertyType):
    audio_monitoring_settings: list[DslValue[AudioMonitoringSetting]] = field(
        default_factory=list
    )
    content_quality_analysis_state: DslValue[str] | None = None
    thumbnail_state: DslValue[str] | None = None
    video_monitoring_settings: list[DslValue[VideoMonitoringSetting]] = field(
        default_factory=list
    )


@dataclass
class SourcePriority(PropertyType):
    primary_source: DslValue[str] | None = None


@dataclass
class VideoMonitoringSetting(PropertyType):
    black_frames: DslValue[BlackFrames] | None = None
    frozen_frames: DslValue[FrozenFrames] | None = None


@dataclass
class VpcInterface(PropertyType):
    name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_id: DslValue[str] | None = None
    network_interface_ids: list[DslValue[str]] = field(default_factory=list)
    network_interface_type: DslValue[str] | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: DslValue[str] | None = None
