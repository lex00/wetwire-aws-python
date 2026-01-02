"""PropertyTypes for AWS::MediaLive::Multiplexprogram."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MultiplexProgramPacketIdentifiersMap(PropertyType):
    audio_pids: list[Integer] = field(default_factory=list)
    dvb_sub_pids: list[Integer] = field(default_factory=list)
    dvb_teletext_pid: int | None = None
    etv_platform_pid: int | None = None
    etv_signal_pid: int | None = None
    klv_data_pids: list[Integer] = field(default_factory=list)
    pcr_pid: int | None = None
    pmt_pid: int | None = None
    private_metadata_pid: int | None = None
    scte27_pids: list[Integer] = field(default_factory=list)
    scte35_pid: int | None = None
    timed_metadata_pid: int | None = None
    video_pid: int | None = None


@dataclass
class MultiplexProgramPipelineDetail(PropertyType):
    active_channel_pipeline: str | None = None
    pipeline_id: str | None = None


@dataclass
class MultiplexProgramServiceDescriptor(PropertyType):
    provider_name: str | None = None
    service_name: str | None = None


@dataclass
class MultiplexProgramSettings(PropertyType):
    program_number: int | None = None
    preferred_channel_pipeline: str | None = None
    service_descriptor: MultiplexProgramServiceDescriptor | None = None
    video_settings: MultiplexVideoSettings | None = None


@dataclass
class MultiplexStatmuxVideoSettings(PropertyType):
    maximum_bitrate: int | None = None
    minimum_bitrate: int | None = None
    priority: int | None = None


@dataclass
class MultiplexVideoSettings(PropertyType):
    constant_bitrate: int | None = None
    statmux_settings: MultiplexStatmuxVideoSettings | None = None
