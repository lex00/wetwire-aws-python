"""PropertyTypes for AWS::Budgets::BudgetsAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionThreshold(PropertyType):
    type_: str | None = None
    value: float | None = None


@dataclass
class Definition(PropertyType):
    iam_action_definition: IamActionDefinition | None = None
    scp_action_definition: ScpActionDefinition | None = None
    ssm_action_definition: SsmActionDefinition | None = None


@dataclass
class IamActionDefinition(PropertyType):
    policy_arn: str | None = None
    groups: list[String] = field(default_factory=list)
    roles: list[String] = field(default_factory=list)
    users: list[String] = field(default_factory=list)


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ScpActionDefinition(PropertyType):
    policy_id: str | None = None
    target_ids: list[String] = field(default_factory=list)


@dataclass
class SsmActionDefinition(PropertyType):
    instance_ids: list[String] = field(default_factory=list)
    region: str | None = None
    subtype: str | None = None


@dataclass
class Subscriber(PropertyType):
    address: str | None = None
    type_: str | None = None
