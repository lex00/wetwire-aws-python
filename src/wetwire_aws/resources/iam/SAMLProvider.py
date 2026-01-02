"""PropertyTypes for AWS::IAM::SAMLProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SAMLPrivateKey(PropertyType):
    key_id: str | None = None
    timestamp: str | None = None
