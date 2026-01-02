"""PropertyTypes for AWS::Lambda::EventInvokeConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationConfig(PropertyType):
    on_failure: OnFailure | None = None
    on_success: OnSuccess | None = None


@dataclass
class OnFailure(PropertyType):
    destination: str | None = None


@dataclass
class OnSuccess(PropertyType):
    destination: str | None = None
