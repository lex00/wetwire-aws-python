"""PropertyTypes for AWS::MediaLive::Input."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InputDestinationRequest(PropertyType):
    network: DslValue[str] | None = None
    network_routes: list[DslValue[InputRequestDestinationRoute]] = field(
        default_factory=list
    )
    static_ip_address: DslValue[str] | None = None
    stream_name: DslValue[str] | None = None


@dataclass
class InputDeviceRequest(PropertyType):
    id: DslValue[str] | None = None


@dataclass
class InputDeviceSettings(PropertyType):
    id: DslValue[str] | None = None


@dataclass
class InputRequestDestinationRoute(PropertyType):
    cidr: DslValue[str] | None = None
    gateway: DslValue[str] | None = None


@dataclass
class InputSdpLocation(PropertyType):
    media_index: DslValue[int] | None = None
    sdp_url: DslValue[str] | None = None


@dataclass
class InputSourceRequest(PropertyType):
    password_param: DslValue[str] | None = None
    url: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class InputVpcRequest(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MediaConnectFlowRequest(PropertyType):
    flow_arn: DslValue[str] | None = None


@dataclass
class MulticastSettingsCreateRequest(PropertyType):
    sources: list[DslValue[MulticastSourceCreateRequest]] = field(default_factory=list)


@dataclass
class MulticastSettingsUpdateRequest(PropertyType):
    sources: list[DslValue[MulticastSourceUpdateRequest]] = field(default_factory=list)


@dataclass
class MulticastSourceCreateRequest(PropertyType):
    source_ip: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class MulticastSourceUpdateRequest(PropertyType):
    source_ip: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class RouterDestinationSettings(PropertyType):
    availability_zone_name: DslValue[str] | None = None


@dataclass
class RouterSettings(PropertyType):
    destinations: list[DslValue[RouterDestinationSettings]] = field(
        default_factory=list
    )
    encryption_type: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class Smpte2110ReceiverGroup(PropertyType):
    sdp_settings: DslValue[Smpte2110ReceiverGroupSdpSettings] | None = None


@dataclass
class Smpte2110ReceiverGroupSdpSettings(PropertyType):
    ancillary_sdps: list[DslValue[InputSdpLocation]] = field(default_factory=list)
    audio_sdps: list[DslValue[InputSdpLocation]] = field(default_factory=list)
    video_sdp: DslValue[InputSdpLocation] | None = None


@dataclass
class Smpte2110ReceiverGroupSettings(PropertyType):
    smpte2110_receiver_groups: list[DslValue[Smpte2110ReceiverGroup]] = field(
        default_factory=list
    )


@dataclass
class SpecialRouterSettings(PropertyType):
    router_arn: DslValue[str] | None = None


@dataclass
class SrtCallerDecryptionRequest(PropertyType):
    algorithm: DslValue[str] | None = None
    passphrase_secret_arn: DslValue[str] | None = None


@dataclass
class SrtCallerSourceRequest(PropertyType):
    decryption: DslValue[SrtCallerDecryptionRequest] | None = None
    minimum_latency: DslValue[int] | None = None
    srt_listener_address: DslValue[str] | None = None
    srt_listener_port: DslValue[str] | None = None
    stream_id: DslValue[str] | None = None


@dataclass
class SrtSettingsRequest(PropertyType):
    srt_caller_sources: list[DslValue[SrtCallerSourceRequest]] = field(
        default_factory=list
    )
