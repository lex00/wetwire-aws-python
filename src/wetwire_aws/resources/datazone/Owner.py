"""PropertyTypes for AWS::DataZone::Owner."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OwnerGroupProperties(PropertyType):
    group_identifier: str | None = None


@dataclass
class OwnerProperties(PropertyType):
    group: OwnerGroupProperties | None = None
    user: OwnerUserProperties | None = None


@dataclass
class OwnerUserProperties(PropertyType):
    user_identifier: str | None = None
