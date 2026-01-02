"""PropertyTypes for AWS::DataZone::ProjectMembership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Member(PropertyType):
    group_identifier: str | None = None
    user_identifier: str | None = None
