"""PropertyTypes for AWS::IVS::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MultitrackInputConfiguration(PropertyType):
    enabled: bool | None = None
    maximum_resolution: str | None = None
    policy: str | None = None
