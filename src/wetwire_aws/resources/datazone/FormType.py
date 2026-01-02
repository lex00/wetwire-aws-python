"""PropertyTypes for AWS::DataZone::FormType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Model(PropertyType):
    smithy: str | None = None
