"""PropertyTypes for AWS::Logs::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OpenSearchResourceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_arn": "ApplicationARN",
    }

    dashboard_viewer_principals: list[DslValue[str]] = field(default_factory=list)
    data_source_role_arn: DslValue[str] | None = None
    application_arn: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None
    retention_days: DslValue[int] | None = None


@dataclass
class ResourceConfig(PropertyType):
    open_search_resource_config: DslValue[OpenSearchResourceConfig] | None = None
