"""PropertyTypes for AWS::AppSync::SourceApiAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SourceApiAssociationConfig(PropertyType):
    merge_type: str | None = None
