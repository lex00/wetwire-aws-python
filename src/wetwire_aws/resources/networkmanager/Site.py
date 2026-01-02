"""PropertyTypes for AWS::NetworkManager::Site."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Location(PropertyType):
    address: str | None = None
    latitude: str | None = None
    longitude: str | None = None
