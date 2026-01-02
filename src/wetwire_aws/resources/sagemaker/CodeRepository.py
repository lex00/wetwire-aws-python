"""PropertyTypes for AWS::SageMaker::CodeRepository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GitConfig(PropertyType):
    repository_url: str | None = None
    branch: str | None = None
    secret_arn: str | None = None
