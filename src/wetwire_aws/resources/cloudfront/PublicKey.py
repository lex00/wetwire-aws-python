"""PropertyTypes for AWS::CloudFront::PublicKey."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PublicKeyConfig(PropertyType):
    caller_reference: DslValue[str] | None = None
    encoded_key: DslValue[str] | None = None
    name: DslValue[str] | None = None
    comment: DslValue[str] | None = None
