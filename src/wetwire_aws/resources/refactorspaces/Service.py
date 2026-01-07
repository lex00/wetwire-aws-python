"""PropertyTypes for AWS::RefactorSpaces::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LambdaEndpointInput(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class UrlEndpointInput(PropertyType):
    url: DslValue[str] | None = None
    health_url: DslValue[str] | None = None
