"""PropertyTypes for AWS::QBusiness::WebExperience."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BrowserExtensionConfiguration(PropertyType):
    enabled_browser_extensions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CustomizationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_css_url": "CustomCSSUrl",
    }

    custom_css_url: DslValue[str] | None = None
    favicon_url: DslValue[str] | None = None
    font_url: DslValue[str] | None = None
    logo_url: DslValue[str] | None = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_configuration": "OpenIDConnectConfiguration",
    }

    open_id_connect_configuration: (
        DslValue[OpenIDConnectProviderConfiguration] | None
    ) = None
    saml_configuration: DslValue[SamlProviderConfiguration] | None = None


@dataclass
class OpenIDConnectProviderConfiguration(PropertyType):
    secrets_arn: DslValue[str] | None = None
    secrets_role: DslValue[str] | None = None


@dataclass
class SamlProviderConfiguration(PropertyType):
    authentication_url: DslValue[str] | None = None
