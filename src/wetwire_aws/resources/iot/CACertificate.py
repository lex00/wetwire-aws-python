"""PropertyTypes for AWS::IoT::CACertificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RegistrationConfig(PropertyType):
    role_arn: str | None = None
    template_body: str | None = None
    template_name: str | None = None
