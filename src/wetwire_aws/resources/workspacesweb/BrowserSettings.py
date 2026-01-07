"""PropertyTypes for AWS::WorkSpacesWeb::BrowserSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class WebContentFilteringPolicy(PropertyType):
    allowed_urls: list[DslValue[str]] = field(default_factory=list)
    blocked_categories: list[DslValue[str]] = field(default_factory=list)
    blocked_urls: list[DslValue[str]] = field(default_factory=list)
