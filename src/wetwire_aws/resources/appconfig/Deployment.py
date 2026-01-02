"""PropertyTypes for AWS::AppConfig::Deployment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DynamicExtensionParameters(PropertyType):
    extension_reference: str | None = None
    parameter_name: str | None = None
    parameter_value: str | None = None
