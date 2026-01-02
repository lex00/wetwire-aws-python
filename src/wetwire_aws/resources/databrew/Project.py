"""PropertyTypes for AWS::DataBrew::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Sample(PropertyType):
    type_: str | None = None
    size: int | None = None
