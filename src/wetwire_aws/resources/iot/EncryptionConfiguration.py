"""PropertyTypes for AWS::IoT::EncryptionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationDetails(PropertyType):
    configuration_status: DslValue[str] | None = None
    error_code: DslValue[str] | None = None
    error_message: DslValue[str] | None = None
