"""PropertyTypes for AWS::SecretsManager::Secret."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GenerateSecretString(PropertyType):
    exclude_characters: str | None = None
    exclude_lowercase: bool | None = None
    exclude_numbers: bool | None = None
    exclude_punctuation: bool | None = None
    exclude_uppercase: bool | None = None
    generate_string_key: str | None = None
    include_space: bool | None = None
    password_length: int | None = None
    require_each_included_type: bool | None = None
    secret_string_template: str | None = None


@dataclass
class ReplicaRegion(PropertyType):
    region: str | None = None
    kms_key_id: str | None = None
