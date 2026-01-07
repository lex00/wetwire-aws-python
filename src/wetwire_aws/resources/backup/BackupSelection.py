"""PropertyTypes for AWS::Backup::BackupSelection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BackupSelectionResourceType(PropertyType):
    iam_role_arn: DslValue[str] | None = None
    selection_name: DslValue[str] | None = None
    conditions: DslValue[Conditions] | None = None
    list_of_tags: list[DslValue[ConditionResourceType]] = field(default_factory=list)
    not_resources: list[DslValue[str]] = field(default_factory=list)
    resources: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ConditionParameter(PropertyType):
    condition_key: DslValue[str] | None = None
    condition_value: DslValue[str] | None = None


@dataclass
class ConditionResourceType(PropertyType):
    condition_key: DslValue[str] | None = None
    condition_type: DslValue[str] | None = None
    condition_value: DslValue[str] | None = None


@dataclass
class Conditions(PropertyType):
    string_equals: list[DslValue[ConditionParameter]] = field(default_factory=list)
    string_like: list[DslValue[ConditionParameter]] = field(default_factory=list)
    string_not_equals: list[DslValue[ConditionParameter]] = field(default_factory=list)
    string_not_like: list[DslValue[ConditionParameter]] = field(default_factory=list)
