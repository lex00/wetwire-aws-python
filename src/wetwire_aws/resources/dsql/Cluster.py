"""PropertyTypes for AWS::DSQL::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionDetails(PropertyType):
    encryption_status: str | None = None
    encryption_type: str | None = None
    kms_key_arn: str | None = None


@dataclass
class MultiRegionProperties(PropertyType):
    clusters: list[String] = field(default_factory=list)
    witness_region: str | None = None
