"""PropertyTypes for AWS::OpenSearchService::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppConfig(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class DataSource(PropertyType):
    data_source_arn: str | None = None
    data_source_description: str | None = None


@dataclass
class IamIdentityCenterOptions(PropertyType):
    enabled: bool | None = None
    iam_identity_center_instance_arn: str | None = None
    iam_role_for_identity_center_application_arn: str | None = None
