"""PropertyTypes for AWS::Pinpoint::PushTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class APNSPushNotificationTemplate(PropertyType):
    action: DslValue[str] | None = None
    body: DslValue[str] | None = None
    media_url: DslValue[str] | None = None
    sound: DslValue[str] | None = None
    title: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class AndroidPushNotificationTemplate(PropertyType):
    action: DslValue[str] | None = None
    body: DslValue[str] | None = None
    image_icon_url: DslValue[str] | None = None
    image_url: DslValue[str] | None = None
    small_image_icon_url: DslValue[str] | None = None
    sound: DslValue[str] | None = None
    title: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class DefaultPushNotificationTemplate(PropertyType):
    action: DslValue[str] | None = None
    body: DslValue[str] | None = None
    sound: DslValue[str] | None = None
    title: DslValue[str] | None = None
    url: DslValue[str] | None = None
