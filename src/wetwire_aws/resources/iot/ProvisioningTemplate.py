"""PropertyTypes for AWS::IoT::ProvisioningTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ProvisioningHook(PropertyType):
    payload_version: str | None = None
    target_arn: str | None = None
