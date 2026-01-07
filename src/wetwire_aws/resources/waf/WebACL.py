"""PropertyTypes for AWS::WAF::WebACL."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActivatedRule(PropertyType):
    priority: DslValue[int] | None = None
    rule_id: DslValue[str] | None = None
    action: DslValue[WafAction] | None = None


@dataclass
class WafAction(PropertyType):
    type_: DslValue[str] | None = None
