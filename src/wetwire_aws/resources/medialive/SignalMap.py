"""PropertyTypes for AWS::MediaLive::SignalMap."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MediaResource(PropertyType):
    destinations: list[DslValue[MediaResourceNeighbor]] = field(default_factory=list)
    name: DslValue[str] | None = None
    sources: list[DslValue[MediaResourceNeighbor]] = field(default_factory=list)


@dataclass
class MediaResourceNeighbor(PropertyType):
    arn: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class MonitorDeployment(PropertyType):
    status: DslValue[str] | None = None
    details_uri: DslValue[str] | None = None
    error_message: DslValue[str] | None = None


@dataclass
class SuccessfulMonitorDeployment(PropertyType):
    details_uri: DslValue[str] | None = None
    status: DslValue[str] | None = None
