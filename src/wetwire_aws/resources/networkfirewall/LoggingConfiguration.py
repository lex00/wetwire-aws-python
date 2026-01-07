"""PropertyTypes for AWS::NetworkFirewall::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LogDestinationConfig(PropertyType):
    log_destination: dict[str, DslValue[str]] = field(default_factory=dict)
    log_destination_type: DslValue[str] | None = None
    log_type: DslValue[str] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    log_destination_configs: list[DslValue[LogDestinationConfig]] = field(
        default_factory=list
    )
