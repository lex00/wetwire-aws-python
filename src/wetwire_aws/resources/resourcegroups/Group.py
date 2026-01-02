"""PropertyTypes for AWS::ResourceGroups::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationItem(PropertyType):
    parameters: list[ConfigurationParameter] = field(default_factory=list)
    type_: str | None = None


@dataclass
class ConfigurationParameter(PropertyType):
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Query(PropertyType):
    resource_type_filters: list[String] = field(default_factory=list)
    stack_identifier: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class ResourceQuery(PropertyType):
    query: Query | None = None
    type_: str | None = None


@dataclass
class TagFilter(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)
