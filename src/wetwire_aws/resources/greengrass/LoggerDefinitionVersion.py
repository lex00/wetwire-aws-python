"""PropertyTypes for AWS::Greengrass::LoggerDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Logger(PropertyType):
    component: DslValue[str] | None = None
    id: DslValue[str] | None = None
    level: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    space: DslValue[int] | None = None
