"""PropertyTypes for AWS::SageMaker::DeviceFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EdgeOutputConfig(PropertyType):
    s3_output_location: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
