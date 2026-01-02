"""PropertyTypes for AWS::VerifiedPermissions::Policy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EntityIdentifier(PropertyType):
    entity_id: str | None = None
    entity_type: str | None = None


@dataclass
class PolicyDefinition(PropertyType):
    static: StaticPolicyDefinition | None = None
    template_linked: TemplateLinkedPolicyDefinition | None = None


@dataclass
class StaticPolicyDefinition(PropertyType):
    statement: str | None = None
    description: str | None = None


@dataclass
class TemplateLinkedPolicyDefinition(PropertyType):
    policy_template_id: str | None = None
    principal: EntityIdentifier | None = None
    resource: EntityIdentifier | None = None
