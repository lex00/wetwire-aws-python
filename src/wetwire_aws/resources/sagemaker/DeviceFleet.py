"""PropertyTypes for AWS::SageMaker::DeviceFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EdgeOutputConfig(PropertyType):
    s3_output_location: str | None = None
    kms_key_id: str | None = None
