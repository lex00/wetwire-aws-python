"""PropertyTypes for AWS::IoTCoreDeviceAdvisor::SuiteDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeviceUnderTest(PropertyType):
    certificate_arn: str | None = None
    thing_arn: str | None = None


@dataclass
class SuiteDefinitionConfiguration(PropertyType):
    device_permission_role_arn: str | None = None
    root_group: str | None = None
    devices: list[DeviceUnderTest] = field(default_factory=list)
    intended_for_qualification: bool | None = None
    suite_definition_name: str | None = None
