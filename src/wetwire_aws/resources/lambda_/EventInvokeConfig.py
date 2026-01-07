"""PropertyTypes for AWS::Lambda::EventInvokeConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationConfig(PropertyType):
    on_failure: DslValue[OnFailure] | None = None
    on_success: DslValue[OnSuccess] | None = None


@dataclass
class OnFailure(PropertyType):
    destination: DslValue[str] | None = None


@dataclass
class OnSuccess(PropertyType):
    destination: DslValue[str] | None = None
