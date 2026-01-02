"""PropertyTypes for AWS::SSMIncidents::ReplicationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RegionConfiguration(PropertyType):
    sse_kms_key_id: str | None = None


@dataclass
class ReplicationRegion(PropertyType):
    region_configuration: RegionConfiguration | None = None
    region_name: str | None = None
