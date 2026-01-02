"""PropertyTypes for AWS::WorkSpacesWeb::UserSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BrandingConfiguration(PropertyType):
    color_theme: str | None = None
    favicon: str | None = None
    favicon_metadata: ImageMetadata | None = None
    localized_strings: dict[str, LocalizedBrandingStrings] = field(default_factory=dict)
    logo: str | None = None
    logo_metadata: ImageMetadata | None = None
    terms_of_service: str | None = None
    wallpaper: str | None = None
    wallpaper_metadata: ImageMetadata | None = None


@dataclass
class CookieSpecification(PropertyType):
    domain: str | None = None
    name: str | None = None
    path: str | None = None


@dataclass
class CookieSynchronizationConfiguration(PropertyType):
    allowlist: list[CookieSpecification] = field(default_factory=list)
    blocklist: list[CookieSpecification] = field(default_factory=list)


@dataclass
class ImageMetadata(PropertyType):
    file_extension: str | None = None
    last_upload_timestamp: str | None = None
    mime_type: str | None = None


@dataclass
class LocalizedBrandingStrings(PropertyType):
    browser_tab_title: str | None = None
    welcome_text: str | None = None
    contact_button_text: str | None = None
    contact_link: str | None = None
    loading_text: str | None = None
    login_button_text: str | None = None
    login_description: str | None = None
    login_title: str | None = None


@dataclass
class ToolbarConfiguration(PropertyType):
    hidden_toolbar_items: list[String] = field(default_factory=list)
    max_display_resolution: str | None = None
    toolbar_type: str | None = None
    visual_mode: str | None = None
