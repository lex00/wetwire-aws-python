"""PropertyTypes for AWS::Forecast::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributesItems(PropertyType):
    attribute_name: DslValue[str] | None = None
    attribute_type: DslValue[str] | None = None


@dataclass
class EncryptionConfig(PropertyType):
    kms_key_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class Schema(PropertyType):
    attributes: list[DslValue[AttributesItems]] = field(default_factory=list)


@dataclass
class TagsItems(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
