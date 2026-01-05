"""PropertyTypes for AWS::Wisdom::AssistantAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssociationData(PropertyType):
    external_bedrock_knowledge_base_config: (
        ExternalBedrockKnowledgeBaseConfig | None
    ) = None
    knowledge_base_id: str | None = None


@dataclass
class ExternalBedrockKnowledgeBaseConfig(PropertyType):
    access_role_arn: str | None = None
    bedrock_knowledge_base_arn: str | None = None
