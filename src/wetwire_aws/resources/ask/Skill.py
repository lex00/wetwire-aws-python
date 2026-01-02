"""PropertyTypes for Alexa::ASK::Skill."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthenticationConfiguration(PropertyType):
    client_id: str | None = None
    client_secret: str | None = None
    refresh_token: str | None = None


@dataclass
class Overrides(PropertyType):
    manifest: dict[str, Any] | None = None


@dataclass
class SkillPackage(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None
    overrides: Overrides | None = None
    s3_bucket_role: str | None = None
    s3_object_version: str | None = None
