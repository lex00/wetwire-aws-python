"""PropertyTypes for AWS::ResourceExplorer2::View."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IncludedProperty(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class SearchFilter(PropertyType):
    filter_string: DslValue[str] | None = None
