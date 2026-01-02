"""PropertyTypes for AWS::NetworkFirewall::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LogDestinationConfig(PropertyType):
    log_destination: dict[str, String] = field(default_factory=dict)
    log_destination_type: str | None = None
    log_type: str | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    log_destination_configs: list[LogDestinationConfig] = field(default_factory=list)
