"""PropertyTypes for AWS::NetworkManager::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Bandwidth(PropertyType):
    download_speed: int | None = None
    upload_speed: int | None = None
