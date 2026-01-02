"""PropertyTypes for AWS::Greengrass::LoggerDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Logger(PropertyType):
    component: str | None = None
    id: str | None = None
    level: str | None = None
    type_: str | None = None
    space: int | None = None
