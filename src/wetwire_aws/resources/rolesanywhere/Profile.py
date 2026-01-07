"""PropertyTypes for AWS::RolesAnywhere::Profile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeMapping(PropertyType):
    certificate_field: DslValue[str] | None = None
    mapping_rules: list[DslValue[MappingRule]] = field(default_factory=list)


@dataclass
class MappingRule(PropertyType):
    specifier: DslValue[str] | None = None
