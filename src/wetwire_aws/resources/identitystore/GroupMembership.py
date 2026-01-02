"""PropertyTypes for AWS::IdentityStore::GroupMembership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MemberId(PropertyType):
    user_id: str | None = None
