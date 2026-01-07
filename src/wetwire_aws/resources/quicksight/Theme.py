"""PropertyTypes for AWS::QuickSight::Theme."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BorderStyle(PropertyType):
    show: DslValue[bool] | None = None


@dataclass
class DataColorPalette(PropertyType):
    colors: list[DslValue[str]] = field(default_factory=list)
    empty_fill_color: DslValue[str] | None = None
    min_max_gradient: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Font(PropertyType):
    font_family: DslValue[str] | None = None


@dataclass
class GutterStyle(PropertyType):
    show: DslValue[bool] | None = None


@dataclass
class MarginStyle(PropertyType):
    show: DslValue[bool] | None = None


@dataclass
class ResourcePermission(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[str] | None = None


@dataclass
class SheetStyle(PropertyType):
    tile: DslValue[TileStyle] | None = None
    tile_layout: DslValue[TileLayoutStyle] | None = None


@dataclass
class ThemeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ui_color_palette": "UIColorPalette",
    }

    data_color_palette: DslValue[DataColorPalette] | None = None
    sheet: DslValue[SheetStyle] | None = None
    typography: DslValue[Typography] | None = None
    ui_color_palette: DslValue[UIColorPalette] | None = None


@dataclass
class ThemeError(PropertyType):
    message: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ThemeVersion(PropertyType):
    arn: DslValue[str] | None = None
    base_theme_id: DslValue[str] | None = None
    configuration: DslValue[ThemeConfiguration] | None = None
    created_time: DslValue[str] | None = None
    description: DslValue[str] | None = None
    errors: list[DslValue[ThemeError]] = field(default_factory=list)
    status: DslValue[str] | None = None
    version_number: DslValue[float] | None = None


@dataclass
class TileLayoutStyle(PropertyType):
    gutter: DslValue[GutterStyle] | None = None
    margin: DslValue[MarginStyle] | None = None


@dataclass
class TileStyle(PropertyType):
    border: DslValue[BorderStyle] | None = None


@dataclass
class Typography(PropertyType):
    font_families: list[DslValue[Font]] = field(default_factory=list)


@dataclass
class UIColorPalette(PropertyType):
    accent: DslValue[str] | None = None
    accent_foreground: DslValue[str] | None = None
    danger: DslValue[str] | None = None
    danger_foreground: DslValue[str] | None = None
    dimension: DslValue[str] | None = None
    dimension_foreground: DslValue[str] | None = None
    measure: DslValue[str] | None = None
    measure_foreground: DslValue[str] | None = None
    primary_background: DslValue[str] | None = None
    primary_foreground: DslValue[str] | None = None
    secondary_background: DslValue[str] | None = None
    secondary_foreground: DslValue[str] | None = None
    success: DslValue[str] | None = None
    success_foreground: DslValue[str] | None = None
    warning: DslValue[str] | None = None
    warning_foreground: DslValue[str] | None = None
