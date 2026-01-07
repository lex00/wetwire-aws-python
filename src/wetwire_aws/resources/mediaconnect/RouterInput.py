"""PropertyTypes for AWS::MediaConnect::RouterInput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FailoverRouterInputConfiguration(PropertyType):
    network_interface_arn: DslValue[str] | None = None
    protocol_configurations: list[
        DslValue[FailoverRouterInputProtocolConfiguration]
    ] = field(default_factory=list)
    source_priority_mode: DslValue[str] | None = None
    primary_source_index: DslValue[int] | None = None


@dataclass
class FailoverRouterInputProtocolConfiguration(PropertyType):
    rist: DslValue[RistRouterInputConfiguration] | None = None
    rtp: DslValue[RtpRouterInputConfiguration] | None = None
    srt_caller: DslValue[SrtCallerRouterInputConfiguration] | None = None
    srt_listener: DslValue[SrtListenerRouterInputConfiguration] | None = None


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
class MediaConnectFlowRouterInputConfiguration(PropertyType):
    source_transit_decryption: DslValue[FlowTransitEncryption] | None = None
    flow_arn: DslValue[str] | None = None
    flow_output_arn: DslValue[str] | None = None


@dataclass
class MergeRouterInputConfiguration(PropertyType):
    merge_recovery_window_milliseconds: DslValue[int] | None = None
    network_interface_arn: DslValue[str] | None = None
    protocol_configurations: list[DslValue[MergeRouterInputProtocolConfiguration]] = (
        field(default_factory=list)
    )


@dataclass
class MergeRouterInputProtocolConfiguration(PropertyType):
    rist: DslValue[RistRouterInputConfiguration] | None = None
    rtp: DslValue[RtpRouterInputConfiguration] | None = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    day: DslValue[str] | None = None
    time: DslValue[str] | None = None


@dataclass
class RistRouterInputConfiguration(PropertyType):
    port: DslValue[int] | None = None
    recovery_latency_milliseconds: DslValue[int] | None = None


@dataclass
class RouterInputConfiguration(PropertyType):
    failover: DslValue[FailoverRouterInputConfiguration] | None = None
    media_connect_flow: DslValue[MediaConnectFlowRouterInputConfiguration] | None = None
    merge: DslValue[MergeRouterInputConfiguration] | None = None
    standard: DslValue[StandardRouterInputConfiguration] | None = None


@dataclass
class RouterInputProtocolConfiguration(PropertyType):
    rist: DslValue[RistRouterInputConfiguration] | None = None
    rtp: DslValue[RtpRouterInputConfiguration] | None = None
    srt_caller: DslValue[SrtCallerRouterInputConfiguration] | None = None
    srt_listener: DslValue[SrtListenerRouterInputConfiguration] | None = None


@dataclass
class RouterInputTransitEncryption(PropertyType):
    encryption_key_configuration: (
        DslValue[RouterInputTransitEncryptionKeyConfiguration] | None
    ) = None
    encryption_key_type: DslValue[str] | None = None


@dataclass
class RouterInputTransitEncryptionKeyConfiguration(PropertyType):
    automatic: DslValue[dict[str, Any]] | None = None
    secrets_manager: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class RtpRouterInputConfiguration(PropertyType):
    port: DslValue[int] | None = None
    forward_error_correction: DslValue[str] | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class SrtCallerRouterInputConfiguration(PropertyType):
    minimum_latency_milliseconds: DslValue[int] | None = None
    source_address: DslValue[str] | None = None
    source_port: DslValue[int] | None = None
    decryption_configuration: DslValue[SrtDecryptionConfiguration] | None = None
    stream_id: DslValue[str] | None = None


@dataclass
class SrtDecryptionConfiguration(PropertyType):
    encryption_key: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class SrtListenerRouterInputConfiguration(PropertyType):
    minimum_latency_milliseconds: DslValue[int] | None = None
    port: DslValue[int] | None = None
    decryption_configuration: DslValue[SrtDecryptionConfiguration] | None = None


@dataclass
class StandardRouterInputConfiguration(PropertyType):
    network_interface_arn: DslValue[str] | None = None
    protocol_configuration: DslValue[RouterInputProtocolConfiguration] | None = None
    protocol: DslValue[str] | None = None
