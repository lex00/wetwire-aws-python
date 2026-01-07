"""PropertyTypes for AWS::StepFunctions::Activity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    kms_data_key_reuse_period_seconds: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class TagsEntry(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
