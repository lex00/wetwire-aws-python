"""PropertyTypes for AWS::VerifiedPermissions::Policy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EntityIdentifier(PropertyType):
    entity_id: DslValue[str] | None = None
    entity_type: DslValue[str] | None = None


@dataclass
class PolicyDefinition(PropertyType):
    static: DslValue[StaticPolicyDefinition] | None = None
    template_linked: DslValue[TemplateLinkedPolicyDefinition] | None = None


@dataclass
class StaticPolicyDefinition(PropertyType):
    statement: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class TemplateLinkedPolicyDefinition(PropertyType):
    policy_template_id: DslValue[str] | None = None
    principal: DslValue[EntityIdentifier] | None = None
    resource: DslValue[EntityIdentifier] | None = None
