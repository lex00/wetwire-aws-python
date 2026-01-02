"""PropertyTypes for AWS::Evidently::Feature."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EntityOverride(PropertyType):
    entity_id: str | None = None
    variation: str | None = None


@dataclass
class VariationObject(PropertyType):
    variation_name: str | None = None
    boolean_value: bool | None = None
    double_value: float | None = None
    long_value: float | None = None
    string_value: str | None = None
