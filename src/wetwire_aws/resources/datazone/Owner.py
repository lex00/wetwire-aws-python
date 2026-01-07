"""PropertyTypes for AWS::DataZone::Owner."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OwnerGroupProperties(PropertyType):
    group_identifier: DslValue[str] | None = None


@dataclass
class OwnerProperties(PropertyType):
    group: DslValue[OwnerGroupProperties] | None = None
    user: DslValue[OwnerUserProperties] | None = None


@dataclass
class OwnerUserProperties(PropertyType):
    user_identifier: DslValue[str] | None = None
