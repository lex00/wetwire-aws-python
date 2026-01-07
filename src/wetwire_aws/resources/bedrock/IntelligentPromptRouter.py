"""PropertyTypes for AWS::Bedrock::IntelligentPromptRouter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PromptRouterTargetModel(PropertyType):
    model_arn: DslValue[str] | None = None


@dataclass
class RoutingCriteria(PropertyType):
    response_quality_difference: DslValue[float] | None = None
