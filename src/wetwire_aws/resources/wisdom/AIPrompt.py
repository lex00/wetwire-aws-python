"""PropertyTypes for AWS::Wisdom::AIPrompt."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AIPromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_full_ai_prompt_edit_template_configuration": "TextFullAIPromptEditTemplateConfiguration",
    }

    text_full_ai_prompt_edit_template_configuration: (
        DslValue[TextFullAIPromptEditTemplateConfiguration] | None
    ) = None


@dataclass
class TextFullAIPromptEditTemplateConfiguration(PropertyType):
    text: DslValue[str] | None = None
