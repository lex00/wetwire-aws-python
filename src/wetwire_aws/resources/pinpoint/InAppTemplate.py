"""PropertyTypes for AWS::Pinpoint::InAppTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BodyConfig(PropertyType):
    alignment: str | None = None
    body: str | None = None
    text_color: str | None = None


@dataclass
class ButtonConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ios": "IOS",
    }

    android: OverrideButtonConfiguration | None = None
    default_config: DefaultButtonConfiguration | None = None
    ios: OverrideButtonConfiguration | None = None
    web: OverrideButtonConfiguration | None = None


@dataclass
class DefaultButtonConfiguration(PropertyType):
    background_color: str | None = None
    border_radius: int | None = None
    button_action: str | None = None
    link: str | None = None
    text: str | None = None
    text_color: str | None = None


@dataclass
class HeaderConfig(PropertyType):
    alignment: str | None = None
    header: str | None = None
    text_color: str | None = None


@dataclass
class InAppMessageContent(PropertyType):
    background_color: str | None = None
    body_config: BodyConfig | None = None
    header_config: HeaderConfig | None = None
    image_url: str | None = None
    primary_btn: ButtonConfig | None = None
    secondary_btn: ButtonConfig | None = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    button_action: str | None = None
    link: str | None = None
