"""PropertyTypes for AWS::MediaLive::Multiplexprogram."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MultiplexProgramPacketIdentifiersMap(PropertyType):
    audio_pids: list[DslValue[int]] = field(default_factory=list)
    dvb_sub_pids: list[DslValue[int]] = field(default_factory=list)
    dvb_teletext_pid: DslValue[int] | None = None
    etv_platform_pid: DslValue[int] | None = None
    etv_signal_pid: DslValue[int] | None = None
    klv_data_pids: list[DslValue[int]] = field(default_factory=list)
    pcr_pid: DslValue[int] | None = None
    pmt_pid: DslValue[int] | None = None
    private_metadata_pid: DslValue[int] | None = None
    scte27_pids: list[DslValue[int]] = field(default_factory=list)
    scte35_pid: DslValue[int] | None = None
    timed_metadata_pid: DslValue[int] | None = None
    video_pid: DslValue[int] | None = None


@dataclass
class MultiplexProgramPipelineDetail(PropertyType):
    active_channel_pipeline: DslValue[str] | None = None
    pipeline_id: DslValue[str] | None = None


@dataclass
class MultiplexProgramServiceDescriptor(PropertyType):
    provider_name: DslValue[str] | None = None
    service_name: DslValue[str] | None = None


@dataclass
class MultiplexProgramSettings(PropertyType):
    program_number: DslValue[int] | None = None
    preferred_channel_pipeline: DslValue[str] | None = None
    service_descriptor: DslValue[MultiplexProgramServiceDescriptor] | None = None
    video_settings: DslValue[MultiplexVideoSettings] | None = None


@dataclass
class MultiplexStatmuxVideoSettings(PropertyType):
    maximum_bitrate: DslValue[int] | None = None
    minimum_bitrate: DslValue[int] | None = None
    priority: DslValue[int] | None = None


@dataclass
class MultiplexVideoSettings(PropertyType):
    constant_bitrate: DslValue[int] | None = None
    statmux_settings: DslValue[MultiplexStatmuxVideoSettings] | None = None
