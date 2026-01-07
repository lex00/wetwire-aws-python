"""PropertyTypes for AWS::NetworkManager::Site."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Location(PropertyType):
    address: DslValue[str] | None = None
    latitude: DslValue[str] | None = None
    longitude: DslValue[str] | None = None
