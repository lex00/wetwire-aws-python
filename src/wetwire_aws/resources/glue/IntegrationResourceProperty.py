"""PropertyTypes for AWS::Glue::IntegrationResourceProperty."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SourceProcessingProperties(PropertyType):
    role_arn: str | None = None


@dataclass
class TargetProcessingProperties(PropertyType):
    role_arn: str | None = None
    connection_name: str | None = None
    event_bus_arn: str | None = None
    kms_arn: str | None = None
