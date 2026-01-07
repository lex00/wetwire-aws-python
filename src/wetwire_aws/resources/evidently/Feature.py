"""PropertyTypes for AWS::Evidently::Feature."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EntityOverride(PropertyType):
    entity_id: DslValue[str] | None = None
    variation: DslValue[str] | None = None


@dataclass
class VariationObject(PropertyType):
    variation_name: DslValue[str] | None = None
    boolean_value: DslValue[bool] | None = None
    double_value: DslValue[float] | None = None
    long_value: DslValue[float] | None = None
    string_value: DslValue[str] | None = None
