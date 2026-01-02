"""PropertyTypes for AWS::ApiGatewayV2::RouteResponse."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ParameterConstraints(PropertyType):
    required: bool | None = None
