"""PropertyTypes for AWS::MediaLive::Input."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InputDestinationRequest(PropertyType):
    network: str | None = None
    network_routes: list[InputRequestDestinationRoute] = field(default_factory=list)
    static_ip_address: str | None = None
    stream_name: str | None = None


@dataclass
class InputDeviceRequest(PropertyType):
    id: str | None = None


@dataclass
class InputDeviceSettings(PropertyType):
    id: str | None = None


@dataclass
class InputRequestDestinationRoute(PropertyType):
    cidr: str | None = None
    gateway: str | None = None


@dataclass
class InputSdpLocation(PropertyType):
    media_index: int | None = None
    sdp_url: str | None = None


@dataclass
class InputSourceRequest(PropertyType):
    password_param: str | None = None
    url: str | None = None
    username: str | None = None


@dataclass
class InputVpcRequest(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class MediaConnectFlowRequest(PropertyType):
    flow_arn: str | None = None


@dataclass
class MulticastSettingsCreateRequest(PropertyType):
    sources: list[MulticastSourceCreateRequest] = field(default_factory=list)


@dataclass
class MulticastSettingsUpdateRequest(PropertyType):
    sources: list[MulticastSourceUpdateRequest] = field(default_factory=list)


@dataclass
class MulticastSourceCreateRequest(PropertyType):
    source_ip: str | None = None
    url: str | None = None


@dataclass
class MulticastSourceUpdateRequest(PropertyType):
    source_ip: str | None = None
    url: str | None = None


@dataclass
class RouterDestinationSettings(PropertyType):
    availability_zone_name: str | None = None


@dataclass
class RouterSettings(PropertyType):
    destinations: list[RouterDestinationSettings] = field(default_factory=list)
    encryption_type: str | None = None
    secret_arn: str | None = None


@dataclass
class Smpte2110ReceiverGroup(PropertyType):
    sdp_settings: Smpte2110ReceiverGroupSdpSettings | None = None


@dataclass
class Smpte2110ReceiverGroupSdpSettings(PropertyType):
    ancillary_sdps: list[InputSdpLocation] = field(default_factory=list)
    audio_sdps: list[InputSdpLocation] = field(default_factory=list)
    video_sdp: InputSdpLocation | None = None


@dataclass
class Smpte2110ReceiverGroupSettings(PropertyType):
    smpte2110_receiver_groups: list[Smpte2110ReceiverGroup] = field(
        default_factory=list
    )


@dataclass
class SpecialRouterSettings(PropertyType):
    router_arn: str | None = None


@dataclass
class SrtCallerDecryptionRequest(PropertyType):
    algorithm: str | None = None
    passphrase_secret_arn: str | None = None


@dataclass
class SrtCallerSourceRequest(PropertyType):
    decryption: SrtCallerDecryptionRequest | None = None
    minimum_latency: int | None = None
    srt_listener_address: str | None = None
    srt_listener_port: str | None = None
    stream_id: str | None = None


@dataclass
class SrtSettingsRequest(PropertyType):
    srt_caller_sources: list[SrtCallerSourceRequest] = field(default_factory=list)
