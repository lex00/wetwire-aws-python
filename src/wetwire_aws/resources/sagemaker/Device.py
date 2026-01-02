"""PropertyTypes for AWS::SageMaker::Device."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Device(PropertyType):
    device_name: str | None = None
    description: str | None = None
    iot_thing_name: str | None = None
