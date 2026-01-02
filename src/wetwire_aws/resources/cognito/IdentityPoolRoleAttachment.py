"""PropertyTypes for AWS::Cognito::IdentityPoolRoleAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MappingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    claim: str | None = None
    match_type: str | None = None
    role_arn: str | None = None
    value: str | None = None


@dataclass
class RoleMapping(PropertyType):
    type_: str | None = None
    ambiguous_role_resolution: str | None = None
    identity_provider: str | None = None
    rules_configuration: RulesConfigurationType | None = None


@dataclass
class RulesConfigurationType(PropertyType):
    rules: list[MappingRule] = field(default_factory=list)
