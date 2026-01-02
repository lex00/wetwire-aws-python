"""PropertyTypes for AWS::S3::StorageLensGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class And(PropertyType):
    match_any_prefix: list[String] = field(default_factory=list)
    match_any_suffix: list[String] = field(default_factory=list)
    match_any_tag: list[Tag] = field(default_factory=list)
    match_object_age: MatchObjectAge | None = None
    match_object_size: MatchObjectSize | None = None


@dataclass
class Filter(PropertyType):
    and_: And | None = None
    match_any_prefix: list[String] = field(default_factory=list)
    match_any_suffix: list[String] = field(default_factory=list)
    match_any_tag: list[Tag] = field(default_factory=list)
    match_object_age: MatchObjectAge | None = None
    match_object_size: MatchObjectSize | None = None
    or_: Or | None = None


@dataclass
class MatchObjectAge(PropertyType):
    days_greater_than: int | None = None
    days_less_than: int | None = None


@dataclass
class MatchObjectSize(PropertyType):
    bytes_greater_than: int | None = None
    bytes_less_than: int | None = None


@dataclass
class Or(PropertyType):
    match_any_prefix: list[String] = field(default_factory=list)
    match_any_suffix: list[String] = field(default_factory=list)
    match_any_tag: list[Tag] = field(default_factory=list)
    match_object_age: MatchObjectAge | None = None
    match_object_size: MatchObjectSize | None = None
