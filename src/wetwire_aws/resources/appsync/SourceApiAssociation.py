"""PropertyTypes for AWS::AppSync::SourceApiAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SourceApiAssociationConfig(PropertyType):
    merge_type: DslValue[str] | None = None
