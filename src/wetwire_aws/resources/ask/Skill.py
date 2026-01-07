"""PropertyTypes for Alexa::ASK::Skill."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthenticationConfiguration(PropertyType):
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class Overrides(PropertyType):
    manifest: DslValue[dict[str, Any]] | None = None


@dataclass
class SkillPackage(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
    overrides: DslValue[Overrides] | None = None
    s3_bucket_role: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None
