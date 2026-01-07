"""PropertyTypes for AWS::EMRContainers::VirtualCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ContainerInfo(PropertyType):
    eks_info: DslValue[EksInfo] | None = None


@dataclass
class ContainerProvider(PropertyType):
    id: DslValue[str] | None = None
    info: DslValue[ContainerInfo] | None = None
    type_: DslValue[str] | None = None


@dataclass
class EksInfo(PropertyType):
    namespace: DslValue[str] | None = None
