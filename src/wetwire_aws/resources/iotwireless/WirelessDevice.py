"""PropertyTypes for AWS::IoTWireless::WirelessDevice."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AbpV10x(PropertyType):
    dev_addr: str | None = None
    session_keys: SessionKeysAbpV10x | None = None


@dataclass
class AbpV11(PropertyType):
    dev_addr: str | None = None
    session_keys: SessionKeysAbpV11 | None = None


@dataclass
class Application(PropertyType):
    destination_name: str | None = None
    f_port: int | None = None
    type_: str | None = None


@dataclass
class FPorts(PropertyType):
    applications: list[Application] = field(default_factory=list)


@dataclass
class LoRaWANDevice(PropertyType):
    abp_v10x: AbpV10x | None = None
    abp_v11: AbpV11 | None = None
    dev_eui: str | None = None
    device_profile_id: str | None = None
    f_ports: FPorts | None = None
    otaa_v10x: OtaaV10x | None = None
    otaa_v11: OtaaV11 | None = None
    service_profile_id: str | None = None


@dataclass
class OtaaV10x(PropertyType):
    app_eui: str | None = None
    app_key: str | None = None


@dataclass
class OtaaV11(PropertyType):
    app_key: str | None = None
    join_eui: str | None = None
    nwk_key: str | None = None


@dataclass
class SessionKeysAbpV10x(PropertyType):
    app_s_key: str | None = None
    nwk_s_key: str | None = None


@dataclass
class SessionKeysAbpV11(PropertyType):
    app_s_key: str | None = None
    f_nwk_s_int_key: str | None = None
    nwk_s_enc_key: str | None = None
    s_nwk_s_int_key: str | None = None
