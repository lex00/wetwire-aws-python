"""PropertyTypes for AWS::SSMContacts::Plan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ChannelTargetInfo(PropertyType):
    channel_id: DslValue[str] | None = None
    retry_interval_in_minutes: DslValue[int] | None = None


@dataclass
class ContactTargetInfo(PropertyType):
    contact_id: DslValue[str] | None = None
    is_essential: DslValue[bool] | None = None


@dataclass
class Stage(PropertyType):
    duration_in_minutes: DslValue[int] | None = None
    targets: list[DslValue[Targets]] = field(default_factory=list)


@dataclass
class Targets(PropertyType):
    channel_target_info: DslValue[ChannelTargetInfo] | None = None
    contact_target_info: DslValue[ContactTargetInfo] | None = None
