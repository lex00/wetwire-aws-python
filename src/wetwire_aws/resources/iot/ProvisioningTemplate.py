"""PropertyTypes for AWS::IoT::ProvisioningTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ProvisioningHook(PropertyType):
    payload_version: DslValue[str] | None = None
    target_arn: DslValue[str] | None = None
