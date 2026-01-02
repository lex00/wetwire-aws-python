"""PropertyTypes for AWS::EMR::Step."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HadoopJarStepConfig(PropertyType):
    jar: str | None = None
    args: list[String] = field(default_factory=list)
    main_class: str | None = None
    step_properties: list[KeyValue] = field(default_factory=list)


@dataclass
class KeyValue(PropertyType):
    key: str | None = None
    value: str | None = None
