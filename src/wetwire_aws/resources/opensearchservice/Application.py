"""PropertyTypes for AWS::OpenSearchService::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppConfig(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class DataSource(PropertyType):
    data_source_arn: DslValue[str] | None = None
    data_source_description: DslValue[str] | None = None


@dataclass
class IamIdentityCenterOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    iam_identity_center_instance_arn: DslValue[str] | None = None
    iam_role_for_identity_center_application_arn: DslValue[str] | None = None
