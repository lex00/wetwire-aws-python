"""PropertyTypes for AWS::ManagedBlockchain::Node."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NodeConfiguration(PropertyType):
    availability_zone: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
