"""PropertyTypes for AWS::Connect::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FontFamily(PropertyType):
    default: DslValue[str] | None = None


@dataclass
class MediaItem(PropertyType):
    type_: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class PaletteCanvas(PropertyType):
    active_background: DslValue[str] | None = None
    container_background: DslValue[str] | None = None
    page_background: DslValue[str] | None = None


@dataclass
class PaletteHeader(PropertyType):
    background: DslValue[str] | None = None
    invert_actions_colors: DslValue[bool] | None = None
    text: DslValue[str] | None = None
    text_hover: DslValue[str] | None = None


@dataclass
class PaletteNavigation(PropertyType):
    background: DslValue[str] | None = None
    invert_actions_colors: DslValue[bool] | None = None
    text: DslValue[str] | None = None
    text_active: DslValue[str] | None = None
    text_background_active: DslValue[str] | None = None
    text_background_hover: DslValue[str] | None = None
    text_hover: DslValue[str] | None = None


@dataclass
class PalettePrimary(PropertyType):
    active: DslValue[str] | None = None
    contrast_text: DslValue[str] | None = None
    default: DslValue[str] | None = None


@dataclass
class WorkspacePage(PropertyType):
    page: DslValue[str] | None = None
    resource_arn: DslValue[str] | None = None
    input_data: DslValue[str] | None = None
    slug: DslValue[str] | None = None


@dataclass
class WorkspaceTheme(PropertyType):
    dark: DslValue[WorkspaceThemeConfig] | None = None
    light: DslValue[WorkspaceThemeConfig] | None = None


@dataclass
class WorkspaceThemeConfig(PropertyType):
    palette: DslValue[WorkspaceThemePalette] | None = None
    typography: DslValue[WorkspaceThemeTypography] | None = None


@dataclass
class WorkspaceThemePalette(PropertyType):
    canvas: DslValue[PaletteCanvas] | None = None
    header: DslValue[PaletteHeader] | None = None
    navigation: DslValue[PaletteNavigation] | None = None
    primary: DslValue[PalettePrimary] | None = None


@dataclass
class WorkspaceThemeTypography(PropertyType):
    font_family: DslValue[FontFamily] | None = None
