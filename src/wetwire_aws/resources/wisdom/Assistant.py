"""PropertyTypes for AWS::Wisdom::Assistant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None
