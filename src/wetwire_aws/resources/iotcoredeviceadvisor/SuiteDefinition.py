"""PropertyTypes for AWS::IoTCoreDeviceAdvisor::SuiteDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeviceUnderTest(PropertyType):
    certificate_arn: DslValue[str] | None = None
    thing_arn: DslValue[str] | None = None


@dataclass
class SuiteDefinitionConfiguration(PropertyType):
    device_permission_role_arn: DslValue[str] | None = None
    root_group: DslValue[str] | None = None
    devices: list[DslValue[DeviceUnderTest]] = field(default_factory=list)
    intended_for_qualification: DslValue[bool] | None = None
    suite_definition_name: DslValue[str] | None = None
