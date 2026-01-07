"""PropertyTypes for AWS::SecretsManager::Secret."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GenerateSecretString(PropertyType):
    exclude_characters: DslValue[str] | None = None
    exclude_lowercase: DslValue[bool] | None = None
    exclude_numbers: DslValue[bool] | None = None
    exclude_punctuation: DslValue[bool] | None = None
    exclude_uppercase: DslValue[bool] | None = None
    generate_string_key: DslValue[str] | None = None
    include_space: DslValue[bool] | None = None
    password_length: DslValue[int] | None = None
    require_each_included_type: DslValue[bool] | None = None
    secret_string_template: DslValue[str] | None = None


@dataclass
class ReplicaRegion(PropertyType):
    region: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
