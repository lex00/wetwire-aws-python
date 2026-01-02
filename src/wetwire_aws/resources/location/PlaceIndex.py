"""PropertyTypes for AWS::Location::PlaceIndex."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataSourceConfiguration(PropertyType):
    intended_use: str | None = None
