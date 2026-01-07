"""PropertyTypes for AWS::ElasticLoadBalancingV2::TrustStoreRevocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RevocationContent(PropertyType):
    revocation_type: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None


@dataclass
class TrustStoreRevocation(PropertyType):
    number_of_revoked_entries: DslValue[int] | None = None
    revocation_id: DslValue[str] | None = None
    revocation_type: DslValue[str] | None = None
    trust_store_arn: DslValue[str] | None = None
