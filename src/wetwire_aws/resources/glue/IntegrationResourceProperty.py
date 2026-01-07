"""PropertyTypes for AWS::Glue::IntegrationResourceProperty."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SourceProcessingProperties(PropertyType):
    role_arn: DslValue[str] | None = None


@dataclass
class TargetProcessingProperties(PropertyType):
    role_arn: DslValue[str] | None = None
    connection_name: DslValue[str] | None = None
    event_bus_arn: DslValue[str] | None = None
    kms_arn: DslValue[str] | None = None
