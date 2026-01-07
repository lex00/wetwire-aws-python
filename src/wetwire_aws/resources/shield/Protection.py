"""PropertyTypes for AWS::Shield::Protection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    block: DslValue[dict[str, Any]] | None = None
    count: DslValue[dict[str, Any]] | None = None


@dataclass
class ApplicationLayerAutomaticResponseConfiguration(PropertyType):
    action: DslValue[Action] | None = None
    status: DslValue[str] | None = None
