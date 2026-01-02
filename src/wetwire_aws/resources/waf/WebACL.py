"""PropertyTypes for AWS::WAF::WebACL."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActivatedRule(PropertyType):
    priority: int | None = None
    rule_id: str | None = None
    action: WafAction | None = None


@dataclass
class WafAction(PropertyType):
    type_: str | None = None
