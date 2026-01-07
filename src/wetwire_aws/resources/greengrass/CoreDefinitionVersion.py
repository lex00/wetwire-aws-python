"""PropertyTypes for AWS::Greengrass::CoreDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Core(PropertyType):
    certificate_arn: DslValue[str] | None = None
    id: DslValue[str] | None = None
    thing_arn: DslValue[str] | None = None
    sync_shadow: DslValue[bool] | None = None
