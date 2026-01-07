"""PropertyTypes for AWS::IoT::CACertificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RegistrationConfig(PropertyType):
    role_arn: DslValue[str] | None = None
    template_body: DslValue[str] | None = None
    template_name: DslValue[str] | None = None
