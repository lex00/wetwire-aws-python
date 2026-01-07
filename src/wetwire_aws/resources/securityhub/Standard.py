"""PropertyTypes for AWS::SecurityHub::Standard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class StandardsControl(PropertyType):
    standards_control_arn: DslValue[str] | None = None
    reason: DslValue[str] | None = None
