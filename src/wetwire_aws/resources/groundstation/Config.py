"""PropertyTypes for AWS::GroundStation::Config."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AntennaDownlinkConfig(PropertyType):
    spectrum_config: DslValue[SpectrumConfig] | None = None


@dataclass
class AntennaDownlinkDemodDecodeConfig(PropertyType):
    decode_config: DslValue[DecodeConfig] | None = None
    demodulation_config: DslValue[DemodulationConfig] | None = None
    spectrum_config: DslValue[SpectrumConfig] | None = None


@dataclass
class AntennaUplinkConfig(PropertyType):
    spectrum_config: DslValue[UplinkSpectrumConfig] | None = None
    target_eirp: DslValue[Eirp] | None = None
    transmit_disabled: DslValue[bool] | None = None


@dataclass
class ConfigData(PropertyType):
    antenna_downlink_config: DslValue[AntennaDownlinkConfig] | None = None
    antenna_downlink_demod_decode_config: (
        DslValue[AntennaDownlinkDemodDecodeConfig] | None
    ) = None
    antenna_uplink_config: DslValue[AntennaUplinkConfig] | None = None
    dataflow_endpoint_config: DslValue[DataflowEndpointConfig] | None = None
    s3_recording_config: DslValue[S3RecordingConfig] | None = None
    tracking_config: DslValue[TrackingConfig] | None = None
    uplink_echo_config: DslValue[UplinkEchoConfig] | None = None


@dataclass
class DataflowEndpointConfig(PropertyType):
    dataflow_endpoint_name: DslValue[str] | None = None
    dataflow_endpoint_region: DslValue[str] | None = None


@dataclass
class DecodeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: DslValue[str] | None = None


@dataclass
class DemodulationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: DslValue[str] | None = None


@dataclass
class Eirp(PropertyType):
    units: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class Frequency(PropertyType):
    units: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class FrequencyBandwidth(PropertyType):
    units: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class S3RecordingConfig(PropertyType):
    bucket_arn: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class SpectrumConfig(PropertyType):
    bandwidth: DslValue[FrequencyBandwidth] | None = None
    center_frequency: DslValue[Frequency] | None = None
    polarization: DslValue[str] | None = None


@dataclass
class TrackingConfig(PropertyType):
    autotrack: DslValue[str] | None = None


@dataclass
class UplinkEchoConfig(PropertyType):
    antenna_uplink_config_arn: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class UplinkSpectrumConfig(PropertyType):
    center_frequency: DslValue[Frequency] | None = None
    polarization: DslValue[str] | None = None
