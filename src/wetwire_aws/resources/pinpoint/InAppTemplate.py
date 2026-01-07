"""PropertyTypes for AWS::Pinpoint::InAppTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BodyConfig(PropertyType):
    alignment: DslValue[str] | None = None
    body: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class ButtonConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ios": "IOS",
    }

    android: DslValue[OverrideButtonConfiguration] | None = None
    default_config: DslValue[DefaultButtonConfiguration] | None = None
    ios: DslValue[OverrideButtonConfiguration] | None = None
    web: DslValue[OverrideButtonConfiguration] | None = None


@dataclass
class DefaultButtonConfiguration(PropertyType):
    background_color: DslValue[str] | None = None
    border_radius: DslValue[int] | None = None
    button_action: DslValue[str] | None = None
    link: DslValue[str] | None = None
    text: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class HeaderConfig(PropertyType):
    alignment: DslValue[str] | None = None
    header: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class InAppMessageContent(PropertyType):
    background_color: DslValue[str] | None = None
    body_config: DslValue[BodyConfig] | None = None
    header_config: DslValue[HeaderConfig] | None = None
    image_url: DslValue[str] | None = None
    primary_btn: DslValue[ButtonConfig] | None = None
    secondary_btn: DslValue[ButtonConfig] | None = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    button_action: DslValue[str] | None = None
    link: DslValue[str] | None = None
