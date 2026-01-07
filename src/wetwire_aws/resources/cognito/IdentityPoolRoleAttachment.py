"""PropertyTypes for AWS::Cognito::IdentityPoolRoleAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MappingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    claim: DslValue[str] | None = None
    match_type: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class RoleMapping(PropertyType):
    type_: DslValue[str] | None = None
    ambiguous_role_resolution: DslValue[str] | None = None
    identity_provider: DslValue[str] | None = None
    rules_configuration: DslValue[RulesConfigurationType] | None = None


@dataclass
class RulesConfigurationType(PropertyType):
    rules: list[DslValue[MappingRule]] = field(default_factory=list)
