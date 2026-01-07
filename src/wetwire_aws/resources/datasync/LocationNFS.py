"""PropertyTypes for AWS::DataSync::LocationNFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MountOptions(PropertyType):
    version: DslValue[str] | None = None


@dataclass
class OnPremConfig(PropertyType):
    agent_arns: list[DslValue[str]] = field(default_factory=list)
