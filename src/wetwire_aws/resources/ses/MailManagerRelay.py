"""PropertyTypes for AWS::SES::MailManagerRelay."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RelayAuthentication(PropertyType):
    no_authentication: dict[str, Any] | None = None
    secret_arn: str | None = None
