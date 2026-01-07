"""PropertyTypes for AWS::IVS::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MultitrackInputConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    maximum_resolution: DslValue[str] | None = None
    policy: DslValue[str] | None = None
