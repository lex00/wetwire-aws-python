"""PropertyTypes for AWS::VerifiedPermissions::PolicyStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeletionProtection(PropertyType):
    mode: str | None = None


@dataclass
class SchemaDefinition(PropertyType):
    cedar_format: str | None = None
    cedar_json: str | None = None


@dataclass
class ValidationSettings(PropertyType):
    mode: str | None = None
