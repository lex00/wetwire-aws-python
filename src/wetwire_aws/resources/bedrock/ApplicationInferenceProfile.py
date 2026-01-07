"""PropertyTypes for AWS::Bedrock::ApplicationInferenceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InferenceProfileModel(PropertyType):
    model_arn: DslValue[str] | None = None


@dataclass
class InferenceProfileModelSource(PropertyType):
    copy_from: DslValue[str] | None = None
