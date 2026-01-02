"""PropertyTypes for AWS::MediaLive::Multiplex."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MultiplexMediaConnectOutputDestinationSettings(PropertyType):
    entitlement_arn: str | None = None


@dataclass
class MultiplexOutputDestination(PropertyType):
    multiplex_media_connect_output_destination_settings: (
        MultiplexMediaConnectOutputDestinationSettings | None
    ) = None


@dataclass
class MultiplexSettings(PropertyType):
    transport_stream_bitrate: int | None = None
    transport_stream_id: int | None = None
    maximum_video_buffer_delay_milliseconds: int | None = None
    transport_stream_reserved_bitrate: int | None = None


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None
