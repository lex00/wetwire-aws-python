"""PropertyTypes for AWS::Oam::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LinkConfiguration(PropertyType):
    log_group_configuration: LinkFilter | None = None
    metric_configuration: LinkFilter | None = None


@dataclass
class LinkFilter(PropertyType):
    filter: str | None = None
