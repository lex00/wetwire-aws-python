"""PropertyTypes for AWS::SSMIncidents::ReplicationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RegionConfiguration(PropertyType):
    sse_kms_key_id: DslValue[str] | None = None


@dataclass
class ReplicationRegion(PropertyType):
    region_configuration: DslValue[RegionConfiguration] | None = None
    region_name: DslValue[str] | None = None
