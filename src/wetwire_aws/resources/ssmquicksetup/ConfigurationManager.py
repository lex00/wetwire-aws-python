"""PropertyTypes for AWS::SSMQuickSetup::ConfigurationManager."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    parameters: dict[str, String] = field(default_factory=dict)
    type_: str | None = None
    id: str | None = None
    local_deployment_administration_role_arn: str | None = None
    local_deployment_execution_role_name: str | None = None
    type_version: str | None = None


@dataclass
class StatusSummary(PropertyType):
    last_updated_at: str | None = None
    status_type: str | None = None
    status: str | None = None
    status_details: dict[str, String] = field(default_factory=dict)
    status_message: str | None = None
