"""PropertyTypes for AWS::Redshift::ScheduledAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PauseClusterMessage(PropertyType):
    cluster_identifier: str | None = None


@dataclass
class ResizeClusterMessage(PropertyType):
    cluster_identifier: str | None = None
    classic: bool | None = None
    cluster_type: str | None = None
    node_type: str | None = None
    number_of_nodes: int | None = None


@dataclass
class ResumeClusterMessage(PropertyType):
    cluster_identifier: str | None = None


@dataclass
class ScheduledActionType(PropertyType):
    pause_cluster: PauseClusterMessage | None = None
    resize_cluster: ResizeClusterMessage | None = None
    resume_cluster: ResumeClusterMessage | None = None
