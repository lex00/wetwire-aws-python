"""PropertyTypes for AWS::SecurityHub::Standard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class StandardsControl(PropertyType):
    standards_control_arn: str | None = None
    reason: str | None = None
