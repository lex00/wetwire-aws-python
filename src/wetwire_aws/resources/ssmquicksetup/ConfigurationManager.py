"""PropertyTypes for AWS::SSMQuickSetup::ConfigurationManager."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    type_: DslValue[str] | None = None
    id: DslValue[str] | None = None
    local_deployment_administration_role_arn: DslValue[str] | None = None
    local_deployment_execution_role_name: DslValue[str] | None = None
    type_version: DslValue[str] | None = None


@dataclass
class StatusSummary(PropertyType):
    last_updated_at: DslValue[str] | None = None
    status_type: DslValue[str] | None = None
    status: DslValue[str] | None = None
    status_details: dict[str, DslValue[str]] = field(default_factory=dict)
    status_message: DslValue[str] | None = None
