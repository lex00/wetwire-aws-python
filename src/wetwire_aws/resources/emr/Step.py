"""PropertyTypes for AWS::EMR::Step."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HadoopJarStepConfig(PropertyType):
    jar: DslValue[str] | None = None
    args: list[DslValue[str]] = field(default_factory=list)
    main_class: DslValue[str] | None = None
    step_properties: list[DslValue[KeyValue]] = field(default_factory=list)


@dataclass
class KeyValue(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
