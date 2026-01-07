"""PropertyTypes for AWS::DMS::MigrationProject."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataProviderDescriptor(PropertyType):
    data_provider_arn: DslValue[str] | None = None
    data_provider_identifier: DslValue[str] | None = None
    data_provider_name: DslValue[str] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None


@dataclass
class SchemaConversionApplicationAttributes(PropertyType):
    s3_bucket_path: DslValue[str] | None = None
    s3_bucket_role_arn: DslValue[str] | None = None
