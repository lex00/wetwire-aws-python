"""PropertyTypes for AWS::ApiGatewayV2::RouteResponse."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ParameterConstraints(PropertyType):
    required: DslValue[bool] | None = None
