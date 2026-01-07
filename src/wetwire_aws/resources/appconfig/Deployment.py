"""PropertyTypes for AWS::AppConfig::Deployment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DynamicExtensionParameters(PropertyType):
    extension_reference: DslValue[str] | None = None
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None
