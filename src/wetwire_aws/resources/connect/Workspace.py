"""PropertyTypes for AWS::Connect::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FontFamily(PropertyType):
    default: str | None = None


@dataclass
class MediaItem(PropertyType):
    type_: str | None = None
    source: str | None = None


@dataclass
class PaletteCanvas(PropertyType):
    active_background: str | None = None
    container_background: str | None = None
    page_background: str | None = None


@dataclass
class PaletteHeader(PropertyType):
    background: str | None = None
    invert_actions_colors: bool | None = None
    text: str | None = None
    text_hover: str | None = None


@dataclass
class PaletteNavigation(PropertyType):
    background: str | None = None
    invert_actions_colors: bool | None = None
    text: str | None = None
    text_active: str | None = None
    text_background_active: str | None = None
    text_background_hover: str | None = None
    text_hover: str | None = None


@dataclass
class PalettePrimary(PropertyType):
    active: str | None = None
    contrast_text: str | None = None
    default: str | None = None


@dataclass
class WorkspacePage(PropertyType):
    page: str | None = None
    resource_arn: str | None = None
    input_data: str | None = None
    slug: str | None = None


@dataclass
class WorkspaceTheme(PropertyType):
    dark: WorkspaceThemeConfig | None = None
    light: WorkspaceThemeConfig | None = None


@dataclass
class WorkspaceThemeConfig(PropertyType):
    palette: WorkspaceThemePalette | None = None
    typography: WorkspaceThemeTypography | None = None


@dataclass
class WorkspaceThemePalette(PropertyType):
    canvas: PaletteCanvas | None = None
    header: PaletteHeader | None = None
    navigation: PaletteNavigation | None = None
    primary: PalettePrimary | None = None


@dataclass
class WorkspaceThemeTypography(PropertyType):
    font_family: FontFamily | None = None
