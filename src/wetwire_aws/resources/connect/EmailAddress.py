"""PropertyTypes for AWS::Connect::EmailAddress."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AliasConfiguration(PropertyType):
    email_address_arn: DslValue[str] | None = None
