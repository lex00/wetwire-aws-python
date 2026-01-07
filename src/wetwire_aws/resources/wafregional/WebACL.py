"""PropertyTypes for AWS::WAFRegional::WebACL."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class Rule(PropertyType):
    action: DslValue[Action] | None = None
    priority: DslValue[int] | None = None
    rule_id: DslValue[str] | None = None
