"""PropertyTypes for AWS::CertificateManager::Account."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ExpiryEventsConfiguration(PropertyType):
    days_before_expiry: DslValue[int] | None = None
