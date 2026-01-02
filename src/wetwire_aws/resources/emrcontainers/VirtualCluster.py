"""PropertyTypes for AWS::EMRContainers::VirtualCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ContainerInfo(PropertyType):
    eks_info: EksInfo | None = None


@dataclass
class ContainerProvider(PropertyType):
    id: str | None = None
    info: ContainerInfo | None = None
    type_: str | None = None


@dataclass
class EksInfo(PropertyType):
    namespace: str | None = None
