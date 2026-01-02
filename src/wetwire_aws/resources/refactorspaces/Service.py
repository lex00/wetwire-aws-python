"""PropertyTypes for AWS::RefactorSpaces::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LambdaEndpointInput(PropertyType):
    arn: str | None = None


@dataclass
class UrlEndpointInput(PropertyType):
    url: str | None = None
    health_url: str | None = None
