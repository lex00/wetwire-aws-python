"""PropertyTypes for AWS::IoTWireless::DeviceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWANDeviceProfile(PropertyType):
    class_b_timeout: DslValue[int] | None = None
    class_c_timeout: DslValue[int] | None = None
    factory_preset_freqs_list: list[DslValue[int]] = field(default_factory=list)
    mac_version: DslValue[str] | None = None
    max_duty_cycle: DslValue[int] | None = None
    max_eirp: DslValue[int] | None = None
    ping_slot_dr: DslValue[int] | None = None
    ping_slot_freq: DslValue[int] | None = None
    ping_slot_period: DslValue[int] | None = None
    reg_params_revision: DslValue[str] | None = None
    rf_region: DslValue[str] | None = None
    rx_data_rate2: DslValue[int] | None = None
    rx_delay1: DslValue[int] | None = None
    rx_dr_offset1: DslValue[int] | None = None
    rx_freq2: DslValue[int] | None = None
    supports32_bit_f_cnt: DslValue[bool] | None = None
    supports_class_b: DslValue[bool] | None = None
    supports_class_c: DslValue[bool] | None = None
    supports_join: DslValue[bool] | None = None
