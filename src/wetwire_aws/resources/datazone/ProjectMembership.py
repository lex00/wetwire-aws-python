"""PropertyTypes for AWS::DataZone::ProjectMembership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Member(PropertyType):
    group_identifier: DslValue[str] | None = None
    user_identifier: DslValue[str] | None = None
