"""PropertyTypes for AWS::Connect::DataTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LockVersion(PropertyType):
    data_table: DslValue[str] | None = None
