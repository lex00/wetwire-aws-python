"""PropertyTypes for AWS::Bedrock::AutomatedReasoningPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PolicyDefinition(PropertyType):
    rules: list[PolicyDefinitionRule] = field(default_factory=list)
    types: list[PolicyDefinitionType] = field(default_factory=list)
    variables: list[PolicyDefinitionVariable] = field(default_factory=list)
    version: str | None = None


@dataclass
class PolicyDefinitionRule(PropertyType):
    expression: str | None = None
    id: str | None = None
    alternate_expression: str | None = None


@dataclass
class PolicyDefinitionType(PropertyType):
    name: str | None = None
    values: list[PolicyDefinitionTypeValue] = field(default_factory=list)
    description: str | None = None


@dataclass
class PolicyDefinitionTypeValue(PropertyType):
    value: str | None = None
    description: str | None = None


@dataclass
class PolicyDefinitionVariable(PropertyType):
    description: str | None = None
    name: str | None = None
    type_: str | None = None
