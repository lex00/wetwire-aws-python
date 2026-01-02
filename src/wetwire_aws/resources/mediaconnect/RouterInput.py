"""PropertyTypes for AWS::MediaConnect::RouterInput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FailoverRouterInputConfiguration(PropertyType):
    network_interface_arn: str | None = None
    protocol_configurations: list[FailoverRouterInputProtocolConfiguration] = field(
        default_factory=list
    )
    source_priority_mode: str | None = None
    primary_source_index: int | None = None


@dataclass
class FailoverRouterInputProtocolConfiguration(PropertyType):
    rist: RistRouterInputConfiguration | None = None
    rtp: RtpRouterInputConfiguration | None = None
    srt_caller: SrtCallerRouterInputConfiguration | None = None
    srt_listener: SrtListenerRouterInputConfiguration | None = None


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
class MediaConnectFlowRouterInputConfiguration(PropertyType):
    source_transit_decryption: FlowTransitEncryption | None = None
    flow_arn: str | None = None
    flow_output_arn: str | None = None


@dataclass
class MergeRouterInputConfiguration(PropertyType):
    merge_recovery_window_milliseconds: int | None = None
    network_interface_arn: str | None = None
    protocol_configurations: list[MergeRouterInputProtocolConfiguration] = field(
        default_factory=list
    )


@dataclass
class MergeRouterInputProtocolConfiguration(PropertyType):
    rist: RistRouterInputConfiguration | None = None
    rtp: RtpRouterInputConfiguration | None = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    day: str | None = None
    time: str | None = None


@dataclass
class RistRouterInputConfiguration(PropertyType):
    port: int | None = None
    recovery_latency_milliseconds: int | None = None


@dataclass
class RouterInputConfiguration(PropertyType):
    failover: FailoverRouterInputConfiguration | None = None
    media_connect_flow: MediaConnectFlowRouterInputConfiguration | None = None
    merge: MergeRouterInputConfiguration | None = None
    standard: StandardRouterInputConfiguration | None = None


@dataclass
class RouterInputProtocolConfiguration(PropertyType):
    rist: RistRouterInputConfiguration | None = None
    rtp: RtpRouterInputConfiguration | None = None
    srt_caller: SrtCallerRouterInputConfiguration | None = None
    srt_listener: SrtListenerRouterInputConfiguration | None = None


@dataclass
class RouterInputTransitEncryption(PropertyType):
    encryption_key_configuration: (
        RouterInputTransitEncryptionKeyConfiguration | None
    ) = None
    encryption_key_type: str | None = None


@dataclass
class RouterInputTransitEncryptionKeyConfiguration(PropertyType):
    automatic: dict[str, Any] | None = None
    secrets_manager: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class RtpRouterInputConfiguration(PropertyType):
    port: int | None = None
    forward_error_correction: str | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class SrtCallerRouterInputConfiguration(PropertyType):
    minimum_latency_milliseconds: int | None = None
    source_address: str | None = None
    source_port: int | None = None
    decryption_configuration: SrtDecryptionConfiguration | None = None
    stream_id: str | None = None


@dataclass
class SrtDecryptionConfiguration(PropertyType):
    encryption_key: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class SrtListenerRouterInputConfiguration(PropertyType):
    minimum_latency_milliseconds: int | None = None
    port: int | None = None
    decryption_configuration: SrtDecryptionConfiguration | None = None


@dataclass
class StandardRouterInputConfiguration(PropertyType):
    network_interface_arn: str | None = None
    protocol_configuration: RouterInputProtocolConfiguration | None = None
    protocol: str | None = None
