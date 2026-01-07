"""PropertyTypes for AWS::SES::MailManagerRelay."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RelayAuthentication(PropertyType):
    no_authentication: DslValue[dict[str, Any]] | None = None
    secret_arn: DslValue[str] | None = None
