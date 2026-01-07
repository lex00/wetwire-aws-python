"""PropertyTypes for AWS::Signer::SigningProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SignatureValidityPeriod(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None
