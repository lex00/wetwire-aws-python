"""PropertyTypes for AWS::QuickSight::Theme."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BorderStyle(PropertyType):
    show: bool | None = None


@dataclass
class DataColorPalette(PropertyType):
    colors: list[String] = field(default_factory=list)
    empty_fill_color: str | None = None
    min_max_gradient: list[String] = field(default_factory=list)


@dataclass
class Font(PropertyType):
    font_family: str | None = None


@dataclass
class GutterStyle(PropertyType):
    show: bool | None = None


@dataclass
class MarginStyle(PropertyType):
    show: bool | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[String] = field(default_factory=list)
    principal: str | None = None


@dataclass
class SheetStyle(PropertyType):
    tile: TileStyle | None = None
    tile_layout: TileLayoutStyle | None = None


@dataclass
class ThemeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ui_color_palette": "UIColorPalette",
    }

    data_color_palette: DataColorPalette | None = None
    sheet: SheetStyle | None = None
    typography: Typography | None = None
    ui_color_palette: UIColorPalette | None = None


@dataclass
class ThemeError(PropertyType):
    message: str | None = None
    type_: str | None = None


@dataclass
class ThemeVersion(PropertyType):
    arn: str | None = None
    base_theme_id: str | None = None
    configuration: ThemeConfiguration | None = None
    created_time: str | None = None
    description: str | None = None
    errors: list[ThemeError] = field(default_factory=list)
    status: str | None = None
    version_number: float | None = None


@dataclass
class TileLayoutStyle(PropertyType):
    gutter: GutterStyle | None = None
    margin: MarginStyle | None = None


@dataclass
class TileStyle(PropertyType):
    border: BorderStyle | None = None


@dataclass
class Typography(PropertyType):
    font_families: list[Font] = field(default_factory=list)


@dataclass
class UIColorPalette(PropertyType):
    accent: str | None = None
    accent_foreground: str | None = None
    danger: str | None = None
    danger_foreground: str | None = None
    dimension: str | None = None
    dimension_foreground: str | None = None
    measure: str | None = None
    measure_foreground: str | None = None
    primary_background: str | None = None
    primary_foreground: str | None = None
    secondary_background: str | None = None
    secondary_foreground: str | None = None
    success: str | None = None
    success_foreground: str | None = None
    warning: str | None = None
    warning_foreground: str | None = None
