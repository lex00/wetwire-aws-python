"""PropertyTypes for AWS::StepFunctions::Activity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    type_: str | None = None
    kms_data_key_reuse_period_seconds: int | None = None
    kms_key_id: str | None = None


@dataclass
class TagsEntry(PropertyType):
    key: str | None = None
    value: str | None = None
