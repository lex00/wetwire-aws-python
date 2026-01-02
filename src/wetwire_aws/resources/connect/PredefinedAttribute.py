"""PropertyTypes for AWS::Connect::PredefinedAttribute."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeConfiguration(PropertyType):
    enable_value_validation_on_association: bool | None = None
    is_read_only: bool | None = None


@dataclass
class Values(PropertyType):
    string_list: list[String] = field(default_factory=list)
