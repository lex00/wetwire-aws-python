"""PropertyTypes for AWS::ElasticLoadBalancingV2::TrustStoreRevocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RevocationContent(PropertyType):
    revocation_type: str | None = None
    s3_bucket: str | None = None
    s3_key: str | None = None
    s3_object_version: str | None = None


@dataclass
class TrustStoreRevocation(PropertyType):
    number_of_revoked_entries: int | None = None
    revocation_id: str | None = None
    revocation_type: str | None = None
    trust_store_arn: str | None = None
