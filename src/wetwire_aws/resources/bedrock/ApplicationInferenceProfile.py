"""PropertyTypes for AWS::Bedrock::ApplicationInferenceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InferenceProfileModel(PropertyType):
    model_arn: str | None = None


@dataclass
class InferenceProfileModelSource(PropertyType):
    copy_from: str | None = None
