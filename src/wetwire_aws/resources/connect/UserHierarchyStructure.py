"""PropertyTypes for AWS::Connect::UserHierarchyStructure."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LevelFive(PropertyType):
    name: DslValue[str] | None = None
    hierarchy_level_arn: DslValue[str] | None = None
    hierarchy_level_id: DslValue[str] | None = None


@dataclass
class LevelFour(PropertyType):
    name: DslValue[str] | None = None
    hierarchy_level_arn: DslValue[str] | None = None
    hierarchy_level_id: DslValue[str] | None = None


@dataclass
class LevelOne(PropertyType):
    name: DslValue[str] | None = None
    hierarchy_level_arn: DslValue[str] | None = None
    hierarchy_level_id: DslValue[str] | None = None


@dataclass
class LevelThree(PropertyType):
    name: DslValue[str] | None = None
    hierarchy_level_arn: DslValue[str] | None = None
    hierarchy_level_id: DslValue[str] | None = None


@dataclass
class LevelTwo(PropertyType):
    name: DslValue[str] | None = None
    hierarchy_level_arn: DslValue[str] | None = None
    hierarchy_level_id: DslValue[str] | None = None


@dataclass
class UserHierarchyStructure(PropertyType):
    level_five: DslValue[LevelFive] | None = None
    level_four: DslValue[LevelFour] | None = None
    level_one: DslValue[LevelOne] | None = None
    level_three: DslValue[LevelThree] | None = None
    level_two: DslValue[LevelTwo] | None = None
