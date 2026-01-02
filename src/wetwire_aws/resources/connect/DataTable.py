"""PropertyTypes for AWS::Connect::DataTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LockVersion(PropertyType):
    data_table: str | None = None
