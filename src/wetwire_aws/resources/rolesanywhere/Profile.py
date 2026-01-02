"""PropertyTypes for AWS::RolesAnywhere::Profile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeMapping(PropertyType):
    certificate_field: str | None = None
    mapping_rules: list[MappingRule] = field(default_factory=list)


@dataclass
class MappingRule(PropertyType):
    specifier: str | None = None
