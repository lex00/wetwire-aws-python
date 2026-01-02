"""PropertyTypes for AWS::IoTFleetWise::DecoderManifest."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CanInterface(PropertyType):
    name: str | None = None
    protocol_name: str | None = None
    protocol_version: str | None = None


@dataclass
class CanSignal(PropertyType):
    factor: str | None = None
    is_big_endian: str | None = None
    is_signed: str | None = None
    length: str | None = None
    message_id: str | None = None
    offset: str | None = None
    start_bit: str | None = None
    name: str | None = None
    signal_value_type: str | None = None


@dataclass
class CustomDecodingInterface(PropertyType):
    name: str | None = None


@dataclass
class CustomDecodingSignal(PropertyType):
    id: str | None = None


@dataclass
class NetworkInterfacesItems(PropertyType):
    interface_id: str | None = None
    type_: str | None = None
    can_interface: CanInterface | None = None
    custom_decoding_interface: CustomDecodingInterface | None = None
    obd_interface: ObdInterface | None = None


@dataclass
class ObdInterface(PropertyType):
    name: str | None = None
    request_message_id: str | None = None
    dtc_request_interval_seconds: str | None = None
    has_transmission_ecu: str | None = None
    obd_standard: str | None = None
    pid_request_interval_seconds: str | None = None
    use_extended_ids: str | None = None


@dataclass
class ObdSignal(PropertyType):
    byte_length: str | None = None
    offset: str | None = None
    pid: str | None = None
    pid_response_length: str | None = None
    scaling: str | None = None
    service_mode: str | None = None
    start_byte: str | None = None
    bit_mask_length: str | None = None
    bit_right_shift: str | None = None
    is_signed: str | None = None
    signal_value_type: str | None = None


@dataclass
class SignalDecodersItems(PropertyType):
    fully_qualified_name: str | None = None
    interface_id: str | None = None
    type_: str | None = None
    can_signal: CanSignal | None = None
    custom_decoding_signal: CustomDecodingSignal | None = None
    obd_signal: ObdSignal | None = None
