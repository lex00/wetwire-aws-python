"""PropertyTypes for AWS::S3::StorageLensGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class And(PropertyType):
    match_any_prefix: list[DslValue[str]] = field(default_factory=list)
    match_any_suffix: list[DslValue[str]] = field(default_factory=list)
    match_any_tag: list[DslValue[Tag]] = field(default_factory=list)
    match_object_age: DslValue[MatchObjectAge] | None = None
    match_object_size: DslValue[MatchObjectSize] | None = None


@dataclass
class Filter(PropertyType):
    and_: DslValue[And] | None = None
    match_any_prefix: list[DslValue[str]] = field(default_factory=list)
    match_any_suffix: list[DslValue[str]] = field(default_factory=list)
    match_any_tag: list[DslValue[Tag]] = field(default_factory=list)
    match_object_age: DslValue[MatchObjectAge] | None = None
    match_object_size: DslValue[MatchObjectSize] | None = None
    or_: DslValue[Or] | None = None


@dataclass
class MatchObjectAge(PropertyType):
    days_greater_than: DslValue[int] | None = None
    days_less_than: DslValue[int] | None = None


@dataclass
class MatchObjectSize(PropertyType):
    bytes_greater_than: DslValue[int] | None = None
    bytes_less_than: DslValue[int] | None = None


@dataclass
class Or(PropertyType):
    match_any_prefix: list[DslValue[str]] = field(default_factory=list)
    match_any_suffix: list[DslValue[str]] = field(default_factory=list)
    match_any_tag: list[DslValue[Tag]] = field(default_factory=list)
    match_object_age: DslValue[MatchObjectAge] | None = None
    match_object_size: DslValue[MatchObjectSize] | None = None
