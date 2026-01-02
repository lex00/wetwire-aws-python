"""PropertyTypes for AWS::IAM::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Policy(PropertyType):
    policy_document: dict[str, Any] | None = None
    policy_name: str | None = None
