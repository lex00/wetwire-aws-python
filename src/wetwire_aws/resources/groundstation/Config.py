"""PropertyTypes for AWS::GroundStation::Config."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AntennaDownlinkConfig(PropertyType):
    spectrum_config: SpectrumConfig | None = None


@dataclass
class AntennaDownlinkDemodDecodeConfig(PropertyType):
    decode_config: DecodeConfig | None = None
    demodulation_config: DemodulationConfig | None = None
    spectrum_config: SpectrumConfig | None = None


@dataclass
class AntennaUplinkConfig(PropertyType):
    spectrum_config: UplinkSpectrumConfig | None = None
    target_eirp: Eirp | None = None
    transmit_disabled: bool | None = None


@dataclass
class ConfigData(PropertyType):
    antenna_downlink_config: AntennaDownlinkConfig | None = None
    antenna_downlink_demod_decode_config: AntennaDownlinkDemodDecodeConfig | None = None
    antenna_uplink_config: AntennaUplinkConfig | None = None
    dataflow_endpoint_config: DataflowEndpointConfig | None = None
    s3_recording_config: S3RecordingConfig | None = None
    tracking_config: TrackingConfig | None = None
    uplink_echo_config: UplinkEchoConfig | None = None


@dataclass
class DataflowEndpointConfig(PropertyType):
    dataflow_endpoint_name: str | None = None
    dataflow_endpoint_region: str | None = None


@dataclass
class DecodeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: str | None = None


@dataclass
class DemodulationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: str | None = None


@dataclass
class Eirp(PropertyType):
    units: str | None = None
    value: float | None = None


@dataclass
class Frequency(PropertyType):
    units: str | None = None
    value: float | None = None


@dataclass
class FrequencyBandwidth(PropertyType):
    units: str | None = None
    value: float | None = None


@dataclass
class S3RecordingConfig(PropertyType):
    bucket_arn: str | None = None
    prefix: str | None = None
    role_arn: str | None = None


@dataclass
class SpectrumConfig(PropertyType):
    bandwidth: FrequencyBandwidth | None = None
    center_frequency: Frequency | None = None
    polarization: str | None = None


@dataclass
class TrackingConfig(PropertyType):
    autotrack: str | None = None


@dataclass
class UplinkEchoConfig(PropertyType):
    antenna_uplink_config_arn: str | None = None
    enabled: bool | None = None


@dataclass
class UplinkSpectrumConfig(PropertyType):
    center_frequency: Frequency | None = None
    polarization: str | None = None
