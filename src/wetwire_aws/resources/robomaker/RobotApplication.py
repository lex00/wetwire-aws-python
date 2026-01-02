"""PropertyTypes for AWS::RoboMaker::RobotApplication."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RobotSoftwareSuite(PropertyType):
    name: str | None = None
    version: str | None = None


@dataclass
class SourceConfig(PropertyType):
    architecture: str | None = None
    s3_bucket: str | None = None
    s3_key: str | None = None
