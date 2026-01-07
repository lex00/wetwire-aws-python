"""PropertyTypes for AWS::SSM::ResourceDataSync."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsOrganizationsSource(PropertyType):
    organization_source_type: DslValue[str] | None = None
    organizational_units: list[DslValue[str]] = field(default_factory=list)


@dataclass
class S3Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
    }

    bucket_name: DslValue[str] | None = None
    bucket_region: DslValue[str] | None = None
    sync_format: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class SyncSource(PropertyType):
    source_regions: list[DslValue[str]] = field(default_factory=list)
    source_type: DslValue[str] | None = None
    aws_organizations_source: DslValue[AwsOrganizationsSource] | None = None
    include_future_regions: DslValue[bool] | None = None
