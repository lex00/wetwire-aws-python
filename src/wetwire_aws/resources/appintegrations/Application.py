"""PropertyTypes for AWS::AppIntegrations::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationConfig(PropertyType):
    contact_handling: DslValue[ContactHandling] | None = None


@dataclass
class ApplicationSourceConfig(PropertyType):
    external_url_config: DslValue[ExternalUrlConfig] | None = None


@dataclass
class ContactHandling(PropertyType):
    scope: DslValue[str] | None = None


@dataclass
class ExternalUrlConfig(PropertyType):
    access_url: DslValue[str] | None = None
    approved_origins: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IframeConfig(PropertyType):
    allow: list[DslValue[str]] = field(default_factory=list)
    sandbox: list[DslValue[str]] = field(default_factory=list)
