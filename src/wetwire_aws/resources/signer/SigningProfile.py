"""PropertyTypes for AWS::Signer::SigningProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SignatureValidityPeriod(PropertyType):
    type_: str | None = None
    value: int | None = None
