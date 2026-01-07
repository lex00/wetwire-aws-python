"""PropertyTypes for AWS::Oam::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LinkConfiguration(PropertyType):
    log_group_configuration: DslValue[LinkFilter] | None = None
    metric_configuration: DslValue[LinkFilter] | None = None


@dataclass
class LinkFilter(PropertyType):
    filter: DslValue[str] | None = None
