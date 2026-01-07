"""PropertyTypes for AWS::VerifiedPermissions::PolicyStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeletionProtection(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class SchemaDefinition(PropertyType):
    cedar_format: DslValue[str] | None = None
    cedar_json: DslValue[str] | None = None


@dataclass
class ValidationSettings(PropertyType):
    mode: DslValue[str] | None = None
