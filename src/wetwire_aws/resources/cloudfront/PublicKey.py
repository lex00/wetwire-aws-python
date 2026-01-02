"""PropertyTypes for AWS::CloudFront::PublicKey."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PublicKeyConfig(PropertyType):
    caller_reference: str | None = None
    encoded_key: str | None = None
    name: str | None = None
    comment: str | None = None
