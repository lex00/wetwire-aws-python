"""PropertyTypes for AWS::Greengrass::DeviceDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Device(PropertyType):
    certificate_arn: DslValue[str] | None = None
    id: DslValue[str] | None = None
    thing_arn: DslValue[str] | None = None
    sync_shadow: DslValue[bool] | None = None


@dataclass
class DeviceDefinitionVersion(PropertyType):
    devices: list[DslValue[Device]] = field(default_factory=list)
