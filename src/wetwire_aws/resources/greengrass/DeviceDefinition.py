"""PropertyTypes for AWS::Greengrass::DeviceDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Device(PropertyType):
    certificate_arn: str | None = None
    id: str | None = None
    thing_arn: str | None = None
    sync_shadow: bool | None = None


@dataclass
class DeviceDefinitionVersion(PropertyType):
    devices: list[Device] = field(default_factory=list)
