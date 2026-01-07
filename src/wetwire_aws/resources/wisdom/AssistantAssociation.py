"""PropertyTypes for AWS::Wisdom::AssistantAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssociationData(PropertyType):
    external_bedrock_knowledge_base_config: (
        DslValue[ExternalBedrockKnowledgeBaseConfig] | None
    ) = None
    knowledge_base_id: DslValue[str] | None = None


@dataclass
class ExternalBedrockKnowledgeBaseConfig(PropertyType):
    access_role_arn: DslValue[str] | None = None
    bedrock_knowledge_base_arn: DslValue[str] | None = None
