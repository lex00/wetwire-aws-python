"""PropertyTypes for AWS::Connect::UserHierarchyStructure."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LevelFive(PropertyType):
    name: str | None = None
    hierarchy_level_arn: str | None = None
    hierarchy_level_id: str | None = None


@dataclass
class LevelFour(PropertyType):
    name: str | None = None
    hierarchy_level_arn: str | None = None
    hierarchy_level_id: str | None = None


@dataclass
class LevelOne(PropertyType):
    name: str | None = None
    hierarchy_level_arn: str | None = None
    hierarchy_level_id: str | None = None


@dataclass
class LevelThree(PropertyType):
    name: str | None = None
    hierarchy_level_arn: str | None = None
    hierarchy_level_id: str | None = None


@dataclass
class LevelTwo(PropertyType):
    name: str | None = None
    hierarchy_level_arn: str | None = None
    hierarchy_level_id: str | None = None


@dataclass
class UserHierarchyStructure(PropertyType):
    level_five: LevelFive | None = None
    level_four: LevelFour | None = None
    level_one: LevelOne | None = None
    level_three: LevelThree | None = None
    level_two: LevelTwo | None = None
