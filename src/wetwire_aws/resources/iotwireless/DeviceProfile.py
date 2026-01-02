"""PropertyTypes for AWS::IoTWireless::DeviceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWANDeviceProfile(PropertyType):
    class_b_timeout: int | None = None
    class_c_timeout: int | None = None
    factory_preset_freqs_list: list[Integer] = field(default_factory=list)
    mac_version: str | None = None
    max_duty_cycle: int | None = None
    max_eirp: int | None = None
    ping_slot_dr: int | None = None
    ping_slot_freq: int | None = None
    ping_slot_period: int | None = None
    reg_params_revision: str | None = None
    rf_region: str | None = None
    rx_data_rate2: int | None = None
    rx_delay1: int | None = None
    rx_dr_offset1: int | None = None
    rx_freq2: int | None = None
    supports32_bit_f_cnt: bool | None = None
    supports_class_b: bool | None = None
    supports_class_c: bool | None = None
    supports_join: bool | None = None
