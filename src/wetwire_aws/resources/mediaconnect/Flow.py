"""PropertyTypes for AWS::MediaConnect::Flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AudioMonitoringSetting(PropertyType):
    silent_audio: SilentAudio | None = None


@dataclass
class BlackFrames(PropertyType):
    state: str | None = None
    threshold_seconds: int | None = None


@dataclass
class Encryption(PropertyType):
    role_arn: str | None = None
    algorithm: str | None = None
    constant_initialization_vector: str | None = None
    device_id: str | None = None
    key_type: str | None = None
    region: str | None = None
    resource_id: str | None = None
    secret_arn: str | None = None
    url: str | None = None


@dataclass
class FailoverConfig(PropertyType):
    failover_mode: str | None = None
    recovery_window: int | None = None
    source_priority: SourcePriority | None = None
    state: str | None = None


@dataclass
class FlowTransitEncryption(PropertyType):
    encryption_key_configuration: FlowTransitEncryptionKeyConfiguration | None = None
    encryption_key_type: str | None = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    automatic: dict[str, Any] | None = None
    secrets_manager: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class Fmtp(PropertyType):
    channel_order: str | None = None
    colorimetry: str | None = None
    exact_framerate: str | None = None
    par: str | None = None
    range: str | None = None
    scan_mode: str | None = None
    tcs: str | None = None


@dataclass
class FrozenFrames(PropertyType):
    state: str | None = None
    threshold_seconds: int | None = None


@dataclass
class GatewayBridgeSource(PropertyType):
    bridge_arn: str | None = None
    vpc_interface_attachment: VpcInterfaceAttachment | None = None


@dataclass
class InputConfiguration(PropertyType):
    input_port: int | None = None
    interface: Interface | None = None


@dataclass
class Interface(PropertyType):
    name: str | None = None


@dataclass
class Maintenance(PropertyType):
    maintenance_day: str | None = None
    maintenance_start_hour: str | None = None


@dataclass
class MediaStream(PropertyType):
    media_stream_id: int | None = None
    media_stream_name: str | None = None
    media_stream_type: str | None = None
    attributes: MediaStreamAttributes | None = None
    clock_rate: int | None = None
    description: str | None = None
    fmt: int | None = None
    video_format: str | None = None


@dataclass
class MediaStreamAttributes(PropertyType):
    fmtp: Fmtp | None = None
    lang: str | None = None


@dataclass
class MediaStreamSourceConfiguration(PropertyType):
    encoding_name: str | None = None
    media_stream_name: str | None = None
    input_configurations: list[InputConfiguration] = field(default_factory=list)


@dataclass
class NdiConfig(PropertyType):
    machine_name: str | None = None
    ndi_discovery_servers: list[NdiDiscoveryServerConfig] = field(default_factory=list)
    ndi_state: str | None = None


@dataclass
class NdiDiscoveryServerConfig(PropertyType):
    discovery_server_address: str | None = None
    vpc_interface_adapter: str | None = None
    discovery_server_port: int | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class SilentAudio(PropertyType):
    state: str | None = None
    threshold_seconds: int | None = None


@dataclass
class Source(PropertyType):
    decryption: Encryption | None = None
    description: str | None = None
    entitlement_arn: str | None = None
    gateway_bridge_source: GatewayBridgeSource | None = None
    ingest_ip: str | None = None
    ingest_port: int | None = None
    max_bitrate: int | None = None
    max_latency: int | None = None
    max_sync_buffer: int | None = None
    media_stream_source_configurations: list[MediaStreamSourceConfiguration] = field(
        default_factory=list
    )
    min_latency: int | None = None
    name: str | None = None
    protocol: str | None = None
    router_integration_state: str | None = None
    router_integration_transit_decryption: FlowTransitEncryption | None = None
    sender_control_port: int | None = None
    sender_ip_address: str | None = None
    source_arn: str | None = None
    source_ingest_port: str | None = None
    source_listener_address: str | None = None
    source_listener_port: int | None = None
    stream_id: str | None = None
    vpc_interface_name: str | None = None
    whitelist_cidr: str | None = None


@dataclass
class SourceMonitoringConfig(PropertyType):
    audio_monitoring_settings: list[AudioMonitoringSetting] = field(
        default_factory=list
    )
    content_quality_analysis_state: str | None = None
    thumbnail_state: str | None = None
    video_monitoring_settings: list[VideoMonitoringSetting] = field(
        default_factory=list
    )


@dataclass
class SourcePriority(PropertyType):
    primary_source: str | None = None


@dataclass
class VideoMonitoringSetting(PropertyType):
    black_frames: BlackFrames | None = None
    frozen_frames: FrozenFrames | None = None


@dataclass
class VpcInterface(PropertyType):
    name: str | None = None
    role_arn: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    subnet_id: str | None = None
    network_interface_ids: list[String] = field(default_factory=list)
    network_interface_type: str | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: str | None = None
