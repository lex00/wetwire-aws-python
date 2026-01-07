"""PropertyTypes for AWS::IoTFleetWise::DecoderManifest."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CanInterface(PropertyType):
    name: DslValue[str] | None = None
    protocol_name: DslValue[str] | None = None
    protocol_version: DslValue[str] | None = None


@dataclass
class CanSignal(PropertyType):
    factor: DslValue[str] | None = None
    is_big_endian: DslValue[str] | None = None
    is_signed: DslValue[str] | None = None
    length: DslValue[str] | None = None
    message_id: DslValue[str] | None = None
    offset: DslValue[str] | None = None
    start_bit: DslValue[str] | None = None
    name: DslValue[str] | None = None
    signal_value_type: DslValue[str] | None = None


@dataclass
class CustomDecodingInterface(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class CustomDecodingSignal(PropertyType):
    id: DslValue[str] | None = None


@dataclass
class NetworkInterfacesItems(PropertyType):
    interface_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    can_interface: DslValue[CanInterface] | None = None
    custom_decoding_interface: DslValue[CustomDecodingInterface] | None = None
    obd_interface: DslValue[ObdInterface] | None = None


@dataclass
class ObdInterface(PropertyType):
    name: DslValue[str] | None = None
    request_message_id: DslValue[str] | None = None
    dtc_request_interval_seconds: DslValue[str] | None = None
    has_transmission_ecu: DslValue[str] | None = None
    obd_standard: DslValue[str] | None = None
    pid_request_interval_seconds: DslValue[str] | None = None
    use_extended_ids: DslValue[str] | None = None


@dataclass
class ObdSignal(PropertyType):
    byte_length: DslValue[str] | None = None
    offset: DslValue[str] | None = None
    pid: DslValue[str] | None = None
    pid_response_length: DslValue[str] | None = None
    scaling: DslValue[str] | None = None
    service_mode: DslValue[str] | None = None
    start_byte: DslValue[str] | None = None
    bit_mask_length: DslValue[str] | None = None
    bit_right_shift: DslValue[str] | None = None
    is_signed: DslValue[str] | None = None
    signal_value_type: DslValue[str] | None = None


@dataclass
class SignalDecodersItems(PropertyType):
    fully_qualified_name: DslValue[str] | None = None
    interface_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    can_signal: DslValue[CanSignal] | None = None
    custom_decoding_signal: DslValue[CustomDecodingSignal] | None = None
    obd_signal: DslValue[ObdSignal] | None = None
