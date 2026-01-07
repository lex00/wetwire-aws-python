"""PropertyTypes for AWS::MediaConnect::RouterOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


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
class MaintenanceConfiguration(PropertyType):
    default: DslValue[dict[str, Any]] | None = None
    preferred_day_time: DslValue[PreferredDayTimeMaintenanceConfiguration] | None = None


@dataclass
class MediaConnectFlowRouterOutputConfiguration(PropertyType):
    destination_transit_encryption: DslValue[FlowTransitEncryption] | None = None
    flow_arn: DslValue[str] | None = None
    flow_source_arn: DslValue[str] | None = None


@dataclass
class MediaLiveInputRouterOutputConfiguration(PropertyType):
    destination_transit_encryption: DslValue[MediaLiveTransitEncryption] | None = None
    media_live_input_arn: DslValue[str] | None = None
    media_live_pipeline_id: DslValue[str] | None = None


@dataclass
class MediaLiveTransitEncryption(PropertyType):
    encryption_key_configuration: (
        DslValue[MediaLiveTransitEncryptionKeyConfiguration] | None
    ) = None
    encryption_key_type: DslValue[str] | None = None


@dataclass
class MediaLiveTransitEncryptionKeyConfiguration(PropertyType):
    automatic: DslValue[dict[str, Any]] | None = None
    secrets_manager: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    day: DslValue[str] | None = None
    time: DslValue[str] | None = None


@dataclass
class RistRouterOutputConfiguration(PropertyType):
    destination_address: DslValue[str] | None = None
    destination_port: DslValue[int] | None = None


@dataclass
class RouterOutputConfiguration(PropertyType):
    media_connect_flow: DslValue[MediaConnectFlowRouterOutputConfiguration] | None = (
        None
    )
    media_live_input: DslValue[MediaLiveInputRouterOutputConfiguration] | None = None
    standard: DslValue[StandardRouterOutputConfiguration] | None = None


@dataclass
class RouterOutputProtocolConfiguration(PropertyType):
    rist: DslValue[RistRouterOutputConfiguration] | None = None
    rtp: DslValue[RtpRouterOutputConfiguration] | None = None
    srt_caller: DslValue[SrtCallerRouterOutputConfiguration] | None = None
    srt_listener: DslValue[SrtListenerRouterOutputConfiguration] | None = None


@dataclass
class RtpRouterOutputConfiguration(PropertyType):
    destination_address: DslValue[str] | None = None
    destination_port: DslValue[int] | None = None
    forward_error_correction: DslValue[str] | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class SrtCallerRouterOutputConfiguration(PropertyType):
    destination_address: DslValue[str] | None = None
    destination_port: DslValue[int] | None = None
    minimum_latency_milliseconds: DslValue[int] | None = None
    encryption_configuration: DslValue[SrtEncryptionConfiguration] | None = None
    stream_id: DslValue[str] | None = None


@dataclass
class SrtEncryptionConfiguration(PropertyType):
    encryption_key: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class SrtListenerRouterOutputConfiguration(PropertyType):
    minimum_latency_milliseconds: DslValue[int] | None = None
    port: DslValue[int] | None = None
    encryption_configuration: DslValue[SrtEncryptionConfiguration] | None = None


@dataclass
class StandardRouterOutputConfiguration(PropertyType):
    network_interface_arn: DslValue[str] | None = None
    protocol_configuration: DslValue[RouterOutputProtocolConfiguration] | None = None
    protocol: DslValue[str] | None = None
