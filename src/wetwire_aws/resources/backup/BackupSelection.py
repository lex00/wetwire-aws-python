"""PropertyTypes for AWS::Backup::BackupSelection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BackupSelectionResourceType(PropertyType):
    iam_role_arn: str | None = None
    selection_name: str | None = None
    conditions: Conditions | None = None
    list_of_tags: list[ConditionResourceType] = field(default_factory=list)
    not_resources: list[String] = field(default_factory=list)
    resources: list[String] = field(default_factory=list)


@dataclass
class ConditionParameter(PropertyType):
    condition_key: str | None = None
    condition_value: str | None = None


@dataclass
class ConditionResourceType(PropertyType):
    condition_key: str | None = None
    condition_type: str | None = None
    condition_value: str | None = None


@dataclass
class Conditions(PropertyType):
    string_equals: list[ConditionParameter] = field(default_factory=list)
    string_like: list[ConditionParameter] = field(default_factory=list)
    string_not_equals: list[ConditionParameter] = field(default_factory=list)
    string_not_like: list[ConditionParameter] = field(default_factory=list)
