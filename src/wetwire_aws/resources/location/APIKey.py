"""PropertyTypes for AWS::Location::APIKey."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AndroidApp(PropertyType):
    certificate_fingerprint: DslValue[str] | None = None
    package: DslValue[str] | None = None


@dataclass
class ApiKeyRestrictions(PropertyType):
    allow_actions: list[DslValue[str]] = field(default_factory=list)
    allow_resources: list[DslValue[str]] = field(default_factory=list)
    allow_android_apps: list[DslValue[AndroidApp]] = field(default_factory=list)
    allow_apple_apps: list[DslValue[AppleApp]] = field(default_factory=list)
    allow_referers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AppleApp(PropertyType):
    bundle_id: DslValue[str] | None = None
