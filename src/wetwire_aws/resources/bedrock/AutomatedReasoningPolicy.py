"""PropertyTypes for AWS::Bedrock::AutomatedReasoningPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PolicyDefinition(PropertyType):
    rules: list[DslValue[PolicyDefinitionRule]] = field(default_factory=list)
    types: list[DslValue[PolicyDefinitionType]] = field(default_factory=list)
    variables: list[DslValue[PolicyDefinitionVariable]] = field(default_factory=list)
    version: DslValue[str] | None = None


@dataclass
class PolicyDefinitionRule(PropertyType):
    expression: DslValue[str] | None = None
    id: DslValue[str] | None = None
    alternate_expression: DslValue[str] | None = None


@dataclass
class PolicyDefinitionType(PropertyType):
    name: DslValue[str] | None = None
    values: list[DslValue[PolicyDefinitionTypeValue]] = field(default_factory=list)
    description: DslValue[str] | None = None


@dataclass
class PolicyDefinitionTypeValue(PropertyType):
    value: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class PolicyDefinitionVariable(PropertyType):
    description: DslValue[str] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
