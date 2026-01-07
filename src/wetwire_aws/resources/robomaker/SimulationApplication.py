"""PropertyTypes for AWS::RoboMaker::SimulationApplication."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RenderingEngine(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class RobotSoftwareSuite(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class SimulationSoftwareSuite(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class SourceConfig(PropertyType):
    architecture: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
