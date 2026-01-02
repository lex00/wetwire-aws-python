"""PropertyTypes for AWS::DataSync::LocationNFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MountOptions(PropertyType):
    version: str | None = None


@dataclass
class OnPremConfig(PropertyType):
    agent_arns: list[String] = field(default_factory=list)
