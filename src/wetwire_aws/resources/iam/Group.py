"""PropertyTypes for AWS::IAM::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Policy(PropertyType):
    policy_document: DslValue[dict[str, Any]] | None = None
    policy_name: DslValue[str] | None = None
