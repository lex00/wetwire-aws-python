"""PropertyTypes for AWS::SSM::ResourceDataSync."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsOrganizationsSource(PropertyType):
    organization_source_type: str | None = None
    organizational_units: list[String] = field(default_factory=list)


@dataclass
class S3Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
    }

    bucket_name: str | None = None
    bucket_region: str | None = None
    sync_format: str | None = None
    bucket_prefix: str | None = None
    kms_key_arn: str | None = None


@dataclass
class SyncSource(PropertyType):
    source_regions: list[String] = field(default_factory=list)
    source_type: str | None = None
    aws_organizations_source: AwsOrganizationsSource | None = None
    include_future_regions: bool | None = None
