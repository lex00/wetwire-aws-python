"""PropertyTypes for AWS::WorkSpacesWeb::UserSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BrandingConfiguration(PropertyType):
    color_theme: DslValue[str] | None = None
    favicon: DslValue[str] | None = None
    favicon_metadata: DslValue[ImageMetadata] | None = None
    localized_strings: dict[str, DslValue[LocalizedBrandingStrings]] = field(
        default_factory=dict
    )
    logo: DslValue[str] | None = None
    logo_metadata: DslValue[ImageMetadata] | None = None
    terms_of_service: DslValue[str] | None = None
    wallpaper: DslValue[str] | None = None
    wallpaper_metadata: DslValue[ImageMetadata] | None = None


@dataclass
class CookieSpecification(PropertyType):
    domain: DslValue[str] | None = None
    name: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class CookieSynchronizationConfiguration(PropertyType):
    allowlist: list[DslValue[CookieSpecification]] = field(default_factory=list)
    blocklist: list[DslValue[CookieSpecification]] = field(default_factory=list)


@dataclass
class ImageMetadata(PropertyType):
    file_extension: DslValue[str] | None = None
    last_upload_timestamp: DslValue[str] | None = None
    mime_type: DslValue[str] | None = None


@dataclass
class LocalizedBrandingStrings(PropertyType):
    browser_tab_title: DslValue[str] | None = None
    welcome_text: DslValue[str] | None = None
    contact_button_text: DslValue[str] | None = None
    contact_link: DslValue[str] | None = None
    loading_text: DslValue[str] | None = None
    login_button_text: DslValue[str] | None = None
    login_description: DslValue[str] | None = None
    login_title: DslValue[str] | None = None


@dataclass
class ToolbarConfiguration(PropertyType):
    hidden_toolbar_items: list[DslValue[str]] = field(default_factory=list)
    max_display_resolution: DslValue[str] | None = None
    toolbar_type: DslValue[str] | None = None
    visual_mode: DslValue[str] | None = None
