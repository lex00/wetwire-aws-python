"""PropertyTypes for AWS::Glue::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IntegrationConfig(PropertyType):
    continuous_sync: DslValue[bool] | None = None
    refresh_interval: DslValue[str] | None = None
    source_properties: dict[str, DslValue[str]] = field(default_factory=dict)
