"""PropertyTypes for AWS::QBusiness::WebExperience."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BrowserExtensionConfiguration(PropertyType):
    enabled_browser_extensions: list[String] = field(default_factory=list)


@dataclass
class CustomizationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_css_url": "CustomCSSUrl",
    }

    custom_css_url: str | None = None
    favicon_url: str | None = None
    font_url: str | None = None
    logo_url: str | None = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_configuration": "OpenIDConnectConfiguration",
    }

    open_id_connect_configuration: OpenIDConnectProviderConfiguration | None = None
    saml_configuration: SamlProviderConfiguration | None = None


@dataclass
class OpenIDConnectProviderConfiguration(PropertyType):
    secrets_arn: str | None = None
    secrets_role: str | None = None


@dataclass
class SamlProviderConfiguration(PropertyType):
    authentication_url: str | None = None
