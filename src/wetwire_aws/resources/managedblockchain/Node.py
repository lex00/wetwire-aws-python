"""PropertyTypes for AWS::ManagedBlockchain::Node."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NodeConfiguration(PropertyType):
    availability_zone: str | None = None
    instance_type: str | None = None
