"""PropertyTypes for AWS::CodeGuruProfiler::ProfilingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentPermissions(PropertyType):
    principals: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Channel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_id": "channelId",
        "channel_uri": "channelUri",
    }

    channel_uri: DslValue[str] | None = None
    channel_id: DslValue[str] | None = None
