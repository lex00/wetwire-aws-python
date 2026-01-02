"""PropertyTypes for AWS::Forecast::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributesItems(PropertyType):
    attribute_name: str | None = None
    attribute_type: str | None = None


@dataclass
class EncryptionConfig(PropertyType):
    kms_key_arn: str | None = None
    role_arn: str | None = None


@dataclass
class Schema(PropertyType):
    attributes: list[AttributesItems] = field(default_factory=list)


@dataclass
class TagsItems(PropertyType):
    key: str | None = None
    value: str | None = None
