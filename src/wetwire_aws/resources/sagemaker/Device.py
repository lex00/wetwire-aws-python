"""PropertyTypes for AWS::SageMaker::Device."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Device(PropertyType):
    device_name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    iot_thing_name: DslValue[str] | None = None
