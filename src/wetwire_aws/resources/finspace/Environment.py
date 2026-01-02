"""PropertyTypes for AWS::FinSpace::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeMapItems(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class FederationParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_call_back_url": "ApplicationCallBackURL",
        "federation_urn": "FederationURN",
        "saml_metadata_url": "SamlMetadataURL",
    }

    application_call_back_url: str | None = None
    attribute_map: list[AttributeMapItems] = field(default_factory=list)
    federation_provider_name: str | None = None
    federation_urn: str | None = None
    saml_metadata_document: str | None = None
    saml_metadata_url: str | None = None


@dataclass
class SuperuserParameters(PropertyType):
    email_address: str | None = None
    first_name: str | None = None
    last_name: str | None = None
