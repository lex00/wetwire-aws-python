"""PropertyTypes for AWS::DataBrew::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Sample(PropertyType):
    type_: DslValue[str] | None = None
    size: DslValue[int] | None = None
