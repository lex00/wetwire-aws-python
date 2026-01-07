"""PropertyTypes for AWS::NetworkManager::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Bandwidth(PropertyType):
    download_speed: DslValue[int] | None = None
    upload_speed: DslValue[int] | None = None
