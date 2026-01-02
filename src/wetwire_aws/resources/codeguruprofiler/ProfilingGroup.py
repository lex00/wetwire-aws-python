"""PropertyTypes for AWS::CodeGuruProfiler::ProfilingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentPermissions(PropertyType):
    principals: list[String] = field(default_factory=list)


@dataclass
class Channel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_id": "channelId",
        "channel_uri": "channelUri",
    }

    channel_uri: str | None = None
    channel_id: str | None = None
