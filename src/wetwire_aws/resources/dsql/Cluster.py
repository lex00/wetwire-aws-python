"""PropertyTypes for AWS::DSQL::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionDetails(PropertyType):
    encryption_status: DslValue[str] | None = None
    encryption_type: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class MultiRegionProperties(PropertyType):
    clusters: list[DslValue[str]] = field(default_factory=list)
    witness_region: DslValue[str] | None = None
