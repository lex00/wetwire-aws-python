"""PropertyTypes for AWS::MediaLive::Multiplex."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MultiplexMediaConnectOutputDestinationSettings(PropertyType):
    entitlement_arn: DslValue[str] | None = None


@dataclass
class MultiplexOutputDestination(PropertyType):
    multiplex_media_connect_output_destination_settings: (
        DslValue[MultiplexMediaConnectOutputDestinationSettings] | None
    ) = None


@dataclass
class MultiplexSettings(PropertyType):
    transport_stream_bitrate: DslValue[int] | None = None
    transport_stream_id: DslValue[int] | None = None
    maximum_video_buffer_delay_milliseconds: DslValue[int] | None = None
    transport_stream_reserved_bitrate: DslValue[int] | None = None


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
