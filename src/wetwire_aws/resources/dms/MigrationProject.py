"""PropertyTypes for AWS::DMS::MigrationProject."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataProviderDescriptor(PropertyType):
    data_provider_arn: str | None = None
    data_provider_identifier: str | None = None
    data_provider_name: str | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None


@dataclass
class SchemaConversionApplicationAttributes(PropertyType):
    s3_bucket_path: str | None = None
    s3_bucket_role_arn: str | None = None
