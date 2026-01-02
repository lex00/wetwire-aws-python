"""PropertyTypes for AWS::Glue::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IntegrationConfig(PropertyType):
    continuous_sync: bool | None = None
    refresh_interval: str | None = None
    source_properties: dict[str, String] = field(default_factory=dict)
