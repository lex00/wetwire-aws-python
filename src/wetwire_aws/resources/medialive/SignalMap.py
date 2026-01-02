"""PropertyTypes for AWS::MediaLive::SignalMap."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MediaResource(PropertyType):
    destinations: list[MediaResourceNeighbor] = field(default_factory=list)
    name: str | None = None
    sources: list[MediaResourceNeighbor] = field(default_factory=list)


@dataclass
class MediaResourceNeighbor(PropertyType):
    arn: str | None = None
    name: str | None = None


@dataclass
class MonitorDeployment(PropertyType):
    status: str | None = None
    details_uri: str | None = None
    error_message: str | None = None


@dataclass
class SuccessfulMonitorDeployment(PropertyType):
    details_uri: str | None = None
    status: str | None = None
