"""PropertyTypes for AWS::Budgets::BudgetsAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionThreshold(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class Definition(PropertyType):
    iam_action_definition: DslValue[IamActionDefinition] | None = None
    scp_action_definition: DslValue[ScpActionDefinition] | None = None
    ssm_action_definition: DslValue[SsmActionDefinition] | None = None


@dataclass
class IamActionDefinition(PropertyType):
    policy_arn: DslValue[str] | None = None
    groups: list[DslValue[str]] = field(default_factory=list)
    roles: list[DslValue[str]] = field(default_factory=list)
    users: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ResourceTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ScpActionDefinition(PropertyType):
    policy_id: DslValue[str] | None = None
    target_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SsmActionDefinition(PropertyType):
    instance_ids: list[DslValue[str]] = field(default_factory=list)
    region: DslValue[str] | None = None
    subtype: DslValue[str] | None = None


@dataclass
class Subscriber(PropertyType):
    address: DslValue[str] | None = None
    type_: DslValue[str] | None = None
