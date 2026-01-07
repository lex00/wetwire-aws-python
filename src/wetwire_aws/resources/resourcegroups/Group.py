"""PropertyTypes for AWS::ResourceGroups::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationItem(PropertyType):
    parameters: list[DslValue[ConfigurationParameter]] = field(default_factory=list)
    type_: DslValue[str] | None = None


@dataclass
class ConfigurationParameter(PropertyType):
    name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Query(PropertyType):
    resource_type_filters: list[DslValue[str]] = field(default_factory=list)
    stack_identifier: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class ResourceQuery(PropertyType):
    query: DslValue[Query] | None = None
    type_: DslValue[str] | None = None


@dataclass
class TagFilter(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
