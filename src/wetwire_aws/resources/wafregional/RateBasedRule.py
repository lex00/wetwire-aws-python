"""PropertyTypes for AWS::WAFRegional::RateBasedRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Predicate(PropertyType):
    data_id: DslValue[str] | None = None
    negated: DslValue[bool] | None = None
    type_: DslValue[str] | None = None
