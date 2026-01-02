"""PropertyTypes for AWS::IoT::EncryptionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationDetails(PropertyType):
    configuration_status: str | None = None
    error_code: str | None = None
    error_message: str | None = None
