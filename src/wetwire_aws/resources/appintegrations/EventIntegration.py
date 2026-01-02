"""PropertyTypes for AWS::AppIntegrations::EventIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EventFilter(PropertyType):
    source: str | None = None
