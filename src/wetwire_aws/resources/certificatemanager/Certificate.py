"""PropertyTypes for AWS::CertificateManager::Certificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DomainValidationOption(PropertyType):
    domain_name: DslValue[str] | None = None
    hosted_zone_id: DslValue[str] | None = None
    validation_domain: DslValue[str] | None = None
