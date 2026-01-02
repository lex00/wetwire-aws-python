"""PropertyTypes for AWS::WorkSpacesWeb::BrowserSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class WebContentFilteringPolicy(PropertyType):
    allowed_urls: list[String] = field(default_factory=list)
    blocked_categories: list[String] = field(default_factory=list)
    blocked_urls: list[String] = field(default_factory=list)
