"""PropertyTypes for AWS::AutoScaling::WarmPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InstanceReusePolicy(PropertyType):
    reuse_on_scale_in: DslValue[bool] | None = None
