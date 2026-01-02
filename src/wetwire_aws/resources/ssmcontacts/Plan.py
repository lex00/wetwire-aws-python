"""PropertyTypes for AWS::SSMContacts::Plan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ChannelTargetInfo(PropertyType):
    channel_id: str | None = None
    retry_interval_in_minutes: int | None = None


@dataclass
class ContactTargetInfo(PropertyType):
    contact_id: str | None = None
    is_essential: bool | None = None


@dataclass
class Stage(PropertyType):
    duration_in_minutes: int | None = None
    targets: list[Targets] = field(default_factory=list)


@dataclass
class Targets(PropertyType):
    channel_target_info: ChannelTargetInfo | None = None
    contact_target_info: ContactTargetInfo | None = None
