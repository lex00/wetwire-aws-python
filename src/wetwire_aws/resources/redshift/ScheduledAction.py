"""PropertyTypes for AWS::Redshift::ScheduledAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PauseClusterMessage(PropertyType):
    cluster_identifier: DslValue[str] | None = None


@dataclass
class ResizeClusterMessage(PropertyType):
    cluster_identifier: DslValue[str] | None = None
    classic: DslValue[bool] | None = None
    cluster_type: DslValue[str] | None = None
    node_type: DslValue[str] | None = None
    number_of_nodes: DslValue[int] | None = None


@dataclass
class ResumeClusterMessage(PropertyType):
    cluster_identifier: DslValue[str] | None = None


@dataclass
class ScheduledActionType(PropertyType):
    pause_cluster: DslValue[PauseClusterMessage] | None = None
    resize_cluster: DslValue[ResizeClusterMessage] | None = None
    resume_cluster: DslValue[ResumeClusterMessage] | None = None
