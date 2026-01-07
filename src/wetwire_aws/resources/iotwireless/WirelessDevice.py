"""PropertyTypes for AWS::IoTWireless::WirelessDevice."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AbpV10x(PropertyType):
    dev_addr: DslValue[str] | None = None
    session_keys: DslValue[SessionKeysAbpV10x] | None = None


@dataclass
class AbpV11(PropertyType):
    dev_addr: DslValue[str] | None = None
    session_keys: DslValue[SessionKeysAbpV11] | None = None


@dataclass
class Application(PropertyType):
    destination_name: DslValue[str] | None = None
    f_port: DslValue[int] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FPorts(PropertyType):
    applications: list[DslValue[Application]] = field(default_factory=list)


@dataclass
class LoRaWANDevice(PropertyType):
    abp_v10x: DslValue[AbpV10x] | None = None
    abp_v11: DslValue[AbpV11] | None = None
    dev_eui: DslValue[str] | None = None
    device_profile_id: DslValue[str] | None = None
    f_ports: DslValue[FPorts] | None = None
    otaa_v10x: DslValue[OtaaV10x] | None = None
    otaa_v11: DslValue[OtaaV11] | None = None
    service_profile_id: DslValue[str] | None = None


@dataclass
class OtaaV10x(PropertyType):
    app_eui: DslValue[str] | None = None
    app_key: DslValue[str] | None = None


@dataclass
class OtaaV11(PropertyType):
    app_key: DslValue[str] | None = None
    join_eui: DslValue[str] | None = None
    nwk_key: DslValue[str] | None = None


@dataclass
class SessionKeysAbpV10x(PropertyType):
    app_s_key: DslValue[str] | None = None
    nwk_s_key: DslValue[str] | None = None


@dataclass
class SessionKeysAbpV11(PropertyType):
    app_s_key: DslValue[str] | None = None
    f_nwk_s_int_key: DslValue[str] | None = None
    nwk_s_enc_key: DslValue[str] | None = None
    s_nwk_s_int_key: DslValue[str] | None = None
