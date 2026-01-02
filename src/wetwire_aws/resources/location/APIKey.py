"""PropertyTypes for AWS::Location::APIKey."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AndroidApp(PropertyType):
    certificate_fingerprint: str | None = None
    package: str | None = None


@dataclass
class ApiKeyRestrictions(PropertyType):
    allow_actions: list[String] = field(default_factory=list)
    allow_resources: list[String] = field(default_factory=list)
    allow_android_apps: list[AndroidApp] = field(default_factory=list)
    allow_apple_apps: list[AppleApp] = field(default_factory=list)
    allow_referers: list[String] = field(default_factory=list)


@dataclass
class AppleApp(PropertyType):
    bundle_id: str | None = None
