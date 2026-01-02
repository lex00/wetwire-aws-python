"""PropertyTypes for AWS::AppIntegrations::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationConfig(PropertyType):
    contact_handling: ContactHandling | None = None


@dataclass
class ApplicationSourceConfig(PropertyType):
    external_url_config: ExternalUrlConfig | None = None


@dataclass
class ContactHandling(PropertyType):
    scope: str | None = None


@dataclass
class ExternalUrlConfig(PropertyType):
    access_url: str | None = None
    approved_origins: list[String] = field(default_factory=list)


@dataclass
class IframeConfig(PropertyType):
    allow: list[String] = field(default_factory=list)
    sandbox: list[String] = field(default_factory=list)
