"""PropertyTypes for AWS::Connect::ContactFlowModule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ExternalInvocationConfiguration(PropertyType):
    enabled: bool | None = None
