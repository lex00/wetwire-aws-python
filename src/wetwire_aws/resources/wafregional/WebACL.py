"""PropertyTypes for AWS::WAFRegional::WebACL."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    type_: str | None = None


@dataclass
class Rule(PropertyType):
    action: Action | None = None
    priority: int | None = None
    rule_id: str | None = None
