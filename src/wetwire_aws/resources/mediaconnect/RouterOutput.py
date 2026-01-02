"""PropertyTypes for AWS::MediaConnect::RouterOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FlowTransitEncryption(PropertyType):
    encryption_key_configuration: FlowTransitEncryptionKeyConfiguration | None = None
    encryption_key_type: str | None = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    automatic: dict[str, Any] | None = None
    secrets_manager: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class MaintenanceConfiguration(PropertyType):
    default: dict[str, Any] | None = None
    preferred_day_time: PreferredDayTimeMaintenanceConfiguration | None = None


@dataclass
class MediaConnectFlowRouterOutputConfiguration(PropertyType):
    destination_transit_encryption: FlowTransitEncryption | None = None
    flow_arn: str | None = None
    flow_source_arn: str | None = None


@dataclass
class MediaLiveInputRouterOutputConfiguration(PropertyType):
    destination_transit_encryption: MediaLiveTransitEncryption | None = None
    media_live_input_arn: str | None = None
    media_live_pipeline_id: str | None = None


@dataclass
class MediaLiveTransitEncryption(PropertyType):
    encryption_key_configuration: MediaLiveTransitEncryptionKeyConfiguration | None = (
        None
    )
    encryption_key_type: str | None = None


@dataclass
class MediaLiveTransitEncryptionKeyConfiguration(PropertyType):
    automatic: dict[str, Any] | None = None
    secrets_manager: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    day: str | None = None
    time: str | None = None


@dataclass
class RistRouterOutputConfiguration(PropertyType):
    destination_address: str | None = None
    destination_port: int | None = None


@dataclass
class RouterOutputConfiguration(PropertyType):
    media_connect_flow: MediaConnectFlowRouterOutputConfiguration | None = None
    media_live_input: MediaLiveInputRouterOutputConfiguration | None = None
    standard: StandardRouterOutputConfiguration | None = None


@dataclass
class RouterOutputProtocolConfiguration(PropertyType):
    rist: RistRouterOutputConfiguration | None = None
    rtp: RtpRouterOutputConfiguration | None = None
    srt_caller: SrtCallerRouterOutputConfiguration | None = None
    srt_listener: SrtListenerRouterOutputConfiguration | None = None


@dataclass
class RtpRouterOutputConfiguration(PropertyType):
    destination_address: str | None = None
    destination_port: int | None = None
    forward_error_correction: str | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class SrtCallerRouterOutputConfiguration(PropertyType):
    destination_address: str | None = None
    destination_port: int | None = None
    minimum_latency_milliseconds: int | None = None
    encryption_configuration: SrtEncryptionConfiguration | None = None
    stream_id: str | None = None


@dataclass
class SrtEncryptionConfiguration(PropertyType):
    encryption_key: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class SrtListenerRouterOutputConfiguration(PropertyType):
    minimum_latency_milliseconds: int | None = None
    port: int | None = None
    encryption_configuration: SrtEncryptionConfiguration | None = None


@dataclass
class StandardRouterOutputConfiguration(PropertyType):
    network_interface_arn: str | None = None
    protocol_configuration: RouterOutputProtocolConfiguration | None = None
    protocol: str | None = None
