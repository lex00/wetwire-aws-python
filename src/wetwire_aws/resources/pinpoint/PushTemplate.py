"""PropertyTypes for AWS::Pinpoint::PushTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class APNSPushNotificationTemplate(PropertyType):
    action: str | None = None
    body: str | None = None
    media_url: str | None = None
    sound: str | None = None
    title: str | None = None
    url: str | None = None


@dataclass
class AndroidPushNotificationTemplate(PropertyType):
    action: str | None = None
    body: str | None = None
    image_icon_url: str | None = None
    image_url: str | None = None
    small_image_icon_url: str | None = None
    sound: str | None = None
    title: str | None = None
    url: str | None = None


@dataclass
class DefaultPushNotificationTemplate(PropertyType):
    action: str | None = None
    body: str | None = None
    sound: str | None = None
    title: str | None = None
    url: str | None = None
